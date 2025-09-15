from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
import os
from werkzeug.utils import secure_filename

from app.forms.upload_forms import YoloUploadForm
from app.utils.yolo_utils import run_detection, run_video_detection
from uuid import uuid4

bp = Blueprint('yolo', __name__, url_prefix='/yolo')

UPLOAD_FOLDER = 'app/static/uploads'
RESULT_FOLDER = 'app/static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = YoloUploadForm()
    result_image = None
    result_video = None

    if form.validate_on_submit():
        file = form.image.data
        filename = secure_filename(file.filename)
        save_name = f"{uuid4().hex}_{filename}"
        file_path = os.path.join(UPLOAD_FOLDER, save_name)
        file.save(file_path)

        ext = os.path.splitext(filename)[1].lower()

        if ext in ['.jpg', '.jpeg', '.png', '.bmp']:
            result_path = run_detection(file_path, save_name)
            result_image = url_for('static', filename=f'results/{os.path.splitext(save_name)[0]}/{os.path.basename(result_path)}')

        elif ext in ['.mp4', '.avi']:
            result_path = run_video_detection(file_path)
            result_filename = os.path.basename(result_path)
            result_video = url_for('static', filename='results/predict/' + result_filename)

    return render_template('yolo_upload.html', form=form,
                           result_image=result_image, result_video=result_video)

