import speech_recognition as sr
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format='wav')

def recognize_audio(wav_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data, language='zh-CN')
        except sr.UnknownValueError:
            return '无法识别音频内容'
        except sr.RequestError:
            return '请求识别服务失败，请稍后重试'

def convert_webm_to_wav(webm_path, wav_path):
    audio = AudioSegment.from_file(webm_path, format='webm')
    audio.export(wav_path, format='wav')



