from flask import Blueprint, render_template, request
from app.forms.audio_forms import AudioUploadForm
from app.forms.nlp_forms import TextAnalysisForm
from app.utils.audio_utils import convert_mp3_to_wav, recognize_audio, convert_webm_to_wav
from werkzeug.utils import secure_filename
import os
from uuid import uuid4

bp = Blueprint('speech', __name__, url_prefix='/speech')

AUDIO_FOLDER = 'app/static/audio'
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = AudioUploadForm()
    nlp_form = TextAnalysisForm()
    result = None
    audio_url = None

    if form.validate_on_submit():
        file = form.audio.data
        filename = secure_filename(file.filename)
        unique_name = f"{uuid4().hex}_{filename}"
        save_path = os.path.join(AUDIO_FOLDER, unique_name)
        file.save(save_path)

        ext = os.path.splitext(filename)[1].lower()
        if ext == '.mp3':
            wav_path = save_path.replace('.mp3', '.wav')
            convert_mp3_to_wav(save_path, wav_path)
        elif ext == '.webm':
            wav_path = save_path.replace('.webm', '.wav')
            convert_webm_to_wav(save_path, wav_path)
        else:
            wav_path = save_path

        result = recognize_audio(wav_path)
        audio_url = f"audio/{os.path.basename(wav_path)}"
        print(f"✅ 收到上传文件: {filename}, 保存路径: {save_path}")

    return render_template('speech.html', form=form, result=result, audio_url=audio_url, nlp_form=nlp_form)

