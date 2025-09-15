from flask import Blueprint, render_template, request
from app.forms.nlp_forms import TextAnalysisForm
from app.utils.nlp_utils import analyze_sentiment

bp = Blueprint('nlp', __name__, url_prefix='/nlp')

@bp.route('/text', methods=['GET', 'POST'])
def text():
    form = TextAnalysisForm()
    sentiment = None
    if form.validate_on_submit():
        content = form.content.data
        sentiment = analyze_sentiment(content)
    return render_template('nlp.html', form=form, sentiment=sentiment)


@bp.route('/from_speech', methods=['POST'])
def from_speech():
    from app.forms.nlp_forms import TextAnalysisForm
    form = TextAnalysisForm()
    sentiment = None
    if request.method == 'POST':
        content = request.form.get('content')
        form.content.data = content
        sentiment = analyze_sentiment(content)
    return render_template('nlp.html', form=form, sentiment=sentiment)
