import os
from pydub import AudioSegment
from ultralytics import YOLO
from moviepy import VideoFileClip

MODEL_PATH = r'C:\Users\luolu\runs\detect\train7\weights\best.pt'
RESULT_FOLDER = 'app/static/results'
model = YOLO(MODEL_PATH)

def run_detection(image_path, image_name):
    results = model.predict(
        source=image_path,
        save=True,
        save_txt=False,
        project=RESULT_FOLDER,
        name=os.path.splitext(image_name)[0],
        exist_ok=True
    )

    predict_dir = os.path.join(RESULT_FOLDER, os.path.splitext(image_name)[0])
    result_image_path = os.path.join(predict_dir, os.path.basename(image_path))

    return result_image_path

def run_video_detection(video_path):
    model.predict(
        source=video_path,
        save=True,
        project=RESULT_FOLDER,
        name='predict',
        exist_ok=True
    )
    # 获取输出 avi 路径
    filename = os.path.basename(video_path)
    name_wo_ext = os.path.splitext(filename)[0]
    avi_path = os.path.join(RESULT_FOLDER, 'predict', f"{name_wo_ext}.avi")
    # 转换成 MP4
    mp4_path = convert_avi_to_mp4(avi_path)

    return mp4_path



def convert_avi_to_mp4(avi_path):
    mp4_path = avi_path.replace('.avi', '.mp4')
    clip = VideoFileClip(avi_path)
    clip.write_videofile(mp4_path, codec='libx264')
    return mp4_path

def convert_webm_to_wav(webm_path, wav_path):
    audio = AudioSegment.from_file(webm_path, format='webm')
    audio.export(wav_path, format='wav')
