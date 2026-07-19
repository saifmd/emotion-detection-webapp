import os
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

try:
    from transformers import pipeline
except ImportError:  # pragma: no cover - optional dependency
    pipeline = None

analyzer = SentimentIntensityAnalyzer()

EMOTION_KEYWORDS = {
    "anger": ["mad", "angry", "annoyed", "furious", "rage", "hate", "upset"],
    "disgust": ["disgusted", "gross", "nasty", "horrible", "awful", "sickened"],
    "fear": ["afraid", "fear", "scared", "nervous", "terrified", "worried"],
    "joy": ["glad", "happy", "joy", "excited", "love", "delighted", "pleased"],
    "sadness": ["sad", "sorrow", "grief", "depressed", "unhappy", "miserable", "lonely"],
}


def emotion_detector(text_to_analyze, use_hf=True):
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    if use_hf and pipeline is not None:
        try:
            model_name = os.getenv("HF_EMOTION_MODEL", "cardiffnlp/twitter-roberta-base-emotion")
            classifier = pipeline("text-classification", model=model_name, tokenizer=model_name, truncation=True)
            result = classifier(text_to_analyze, top_k=None)[0]
            label_map = {
                "anger": "anger",
                "disgust": "disgust",
                "fear": "fear",
                "joy": "joy",
                "sadness": "sadness",
            }
            normalized = {}
            for item in result:
                label = item["label"].lower()
                if label in label_map:
                    normalized[label_map[label]] = item["score"]
            if normalized:
                missing = [emo for emo in ["anger", "disgust", "fear", "joy", "sadness"] if emo not in normalized]
                for emo in missing:
                    normalized[emo] = 0.0
                dominant = max(normalized, key=normalized.get)
                return {
                    "anger": normalized["anger"],
                    "disgust": normalized["disgust"],
                    "fear": normalized["fear"],
                    "joy": normalized["joy"],
                    "sadness": normalized["sadness"],
                    "dominant_emotion": dominant,
                }
        except Exception:
            pass

    text = text_to_analyze.lower()
    scores = {emotion: 0.0 for emotion in EMOTION_KEYWORDS}

    for emotion, keywords in EMOTION_KEYWORDS.items():
        for keyword in keywords:
            if re.search(rf"\b{re.escape(keyword)}\b", text):
                scores[emotion] += 1.0

    vader_scores = analyzer.polarity_scores(text_to_analyze)
    if vader_scores["compound"] >= 0.05:
        scores["joy"] += 0.5
    elif vader_scores["compound"] <= -0.05:
        scores["sadness"] += 0.5
        scores["anger"] += 0.3

    if max(scores.values()) == 0:
        if any(keyword in text for keyword in EMOTION_KEYWORDS["fear"]):
            scores["fear"] = 1.0
        elif any(keyword in text for keyword in EMOTION_KEYWORDS["disgust"]):
            scores["disgust"] = 1.0
        elif any(keyword in text for keyword in EMOTION_KEYWORDS["anger"]):
            scores["anger"] = 1.0
        elif any(keyword in text for keyword in EMOTION_KEYWORDS["sadness"]):
            scores["sadness"] = 1.0
        elif vader_scores["compound"] >= 0.05:
            scores["joy"] = 1.0
        elif vader_scores["compound"] <= -0.05:
            scores["sadness"] = 1.0

    dominant_emotion = max(scores, key=scores.get)
    return {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant_emotion,
    }
