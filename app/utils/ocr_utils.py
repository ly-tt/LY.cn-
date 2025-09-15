import easyocr
import cv2

reader = easyocr.Reader(['ch_sim', 'en'])  # 中文简体 + 英文

def run_ocr(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError(f"图片读取失败：{image_path}")

    result = reader.readtext(img, detail=0)  # 直接传 OpenCV 图像
    return result
