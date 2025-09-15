from snownlp import SnowNLP

def analyze_sentiment(text):
    if not text.strip():
        return '⚠️ 无内容可分析'

    try:
        s = SnowNLP(text)
        score = s.sentiments  # 分数范围 [0, 1]

        if score > 0.7:
            return f"😊 正面情绪（情感分数：{score:.2f}）"
        elif score < 0.3:
            return f"😢 负面情绪（情感分数：{score:.2f}）"
        else:
            return f"😐 中性情绪（情感分数：{score:.2f}）"

    except Exception as e:
        return f"❌ 分析失败：{str(e)}"
