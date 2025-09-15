from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import secure_filename
import os
from uuid import uuid4

from app.forms.nlp_forms import TextAnalysisForm
from app.forms.ocr_forms import OCRForm
from app.utils.ocr_utils import run_ocr

bp = Blueprint('ocr', __name__, url_prefix='/ocr')

UPLOAD_FOLDER = 'app/static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = OCRForm()
    nlp_form = TextAnalysisForm()  # ✅ 创建 NLP 表单实例
    text_result = []
    image_url = None

    if form.validate_on_submit():
        file = form.image.data
        filename = secure_filename(file.filename)
        unique_name = f"{uuid4().hex}_{filename}"
        save_path = os.path.join(UPLOAD_FOLDER, unique_name)
        file.save(save_path)

        try:
            text_result = run_ocr(save_path)
            image_url = url_for('static', filename=f'uploads/{unique_name}')
        except Exception as e:
            text_result = [f"❌ 识别失败：{str(e)}"]

    return render_template('ocr.html',
                           form=form,
                           nlp_form=nlp_form,  # ✅ 传入 NLP 表单
                           image_url=image_url,
                           text_result=text_result)