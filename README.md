# Emotion Detection Demo

A simple web-based emotion detection application built with Python, Flask, and an open-source AI approach. The app accepts user-entered text, analyzes its emotional tone, and displays the most likely emotion along with confidence-style scores for multiple emotion categories.

## Project Overview

This project demonstrates how to build a lightweight emotion detection demo that can be run locally or deployed as a public web app. It uses:

- Flask for the web application
- HTML/CSS/JavaScript for the user interface
- Python for the backend logic
- A Hugging Face-compatible model path when available
- A local fallback approach for environments where a model is unavailable

## Features

- Simple text input interface
- Real-time emotion analysis through a Flask backend
- Support for multiple emotion categories:
  - anger
  - disgust
  - fear
  - joy
  - sadness
- A polished front-end experience for demo purposes
- Test coverage using pytest

## Project Structure

- [app.py](app.py) - Main application entry point for local running and deployment
- [server.py](server.py) - Flask app and route definitions
- [templates/index.html](templates/index.html) - Main HTML UI
- [static/mywebscript.js](static/mywebscript.js) - JavaScript for sending requests and updating the page
- [EmotionDetection/emotion_detection.py](EmotionDetection/emotion_detection.py) - Emotion detection logic
- [EmotionDetection/__init__.py](EmotionDetection/__init__.py) - Package export
- [test_emotion_detection.py](test_emotion_detection.py) - Pytest-based tests
- [requirements.txt](requirements.txt) - Python dependencies
- [README_HF.md](README_HF.md) - Hugging Face deployment notes

## How It Works

1. The user enters text into the web form.
2. The frontend sends the text to the Flask backend.
3. The backend calls the emotion detection logic.
4. The detector returns scores for the supported emotions and identifies the dominant emotion.
5. The server sends the result back to the browser, where it is shown in the UI.

<img width="682" height="460" alt="image" src="https://github.com/user-attachments/assets/38424fac-885c-4b33-ad93-f4f7af311fb4" />


## Local Setup

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

Then open:

```text
http://localhost:7860
```

## Running Tests

Run the test suite with:

```bash
python -m pytest -q
```

## Example Input

Try entering text such as:

- "I am so happy today"
- "I feel scared about this"
- "I am really angry"
- "I had a terrible day and feel sad"

## Deployment Notes

This project is prepared for a simple public demo deployment. A Hugging Face Spaces-friendly entry point is included in [app.py](app.py), and deployment guidance is available in [README_HF.md](README_HF.md).

## Notes

- The app is designed for demo and educational purposes.
- The current implementation supports a Hugging Face-based model path when available and falls back to a local rule-based approach if needed.
- For production use, you may want to improve accuracy with a more specialized emotion model or a larger language model.

## Future Improvements

Possible enhancements include:

- Better emotion classification accuracy
- A more polished UI with charts and visual indicators
- Support for multiple languages
- Logging and analytics for demo usage
