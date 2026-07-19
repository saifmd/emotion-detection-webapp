# Emotion Detection Demo

This project can be deployed to Hugging Face Spaces as a simple web app for emotion detection.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:7860

## Notes

The app uses a Hugging Face emotion model when available and falls back to a local rule-based approach if needed.
