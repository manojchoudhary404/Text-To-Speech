# 🗣️ Speech Recognition System  

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?logo=github)](https://github.com/manojchoudhary99/speech-recognition/pulls)  
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/manojchoudhary99)  

A Python-based **Speech Recognition and Text-to-Speech System** powered by [OpenAI Whisper](https://github.com/openai/whisper).  
This project allows you to **transcribe audio (speech-to-text)** with high accuracy and optionally **convert text back into speech** for interactive applications.  

---

## 🚀 Features
- 🎤 Convert **speech to text** using OpenAI’s Whisper model  
- 🔊 Generate **speech from text** with TTS (Text-to-Speech) engines  
- ⚡ High accuracy with multilingual support  
- 🖥️ Easy-to-use Python script  
- 📂 Supports multiple audio formats (`.mp3`, `.wav`, etc.)  

---

## 🛠️ Tech Stack
- **Python 3.12+**  
- **OpenAI Whisper** for transcription  
- **PyTorch** for deep learning backend  
- **FFmpeg** for audio processing  
- (Optional) **pyttsx3 / gTTS** for text-to-speech  

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/manojchoudhary99/speech-recognition.git
cd speech-recognition
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg
(Required for Whisper to process audio)

**Mac (Homebrew):**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**Windows:**  
Download FFmpeg and add it to PATH.

---

## ▶️ Usage

### 🎤 Speech-to-Text
```bash
python transcribe.py
```
This will transcribe `what.mp3` (or any input file you provide) into text.

### 🔊 Text-to-Speech (Optional)
If you have TTS integrated (e.g., pyttsx3 or gTTS):
```bash
python tts.py
```

---

## 📂 Project Structure
```bash
speech-recognition/
│── demo/               # Demo gifs/screenshots
│── transcribe.py       # Speech-to-text script
│── tts.py              # Optional text-to-speech script
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
└── venv/               # Virtual environment (ignored in git)
```

---

## 🎯 Future Enhancements
- 🌐 Real-time speech recognition (live mic input)  
- 📱 Deploy as a simple web/mobile app  
- 🎙️ Support for speaker identification  

---

## 🤝 Contributing
Contributions are welcome!  
If you’d like to improve this project, please fork the repo and create a pull request.  

---

## 📜 License
This project is licensed under the MIT License.  
© 2025 Manoj Choudhary.  

---

## 👨‍💻 Author
**Manoj Choudhary**  
📌 MCA Student | Backend Developer | AI & ML Enthusiast  

🌐 Connect with me:  
- [GitHub](https://github.com/manojchoudhary404)  
- [LinkedIn](https://www.linkedin.com/in/manojchoudhary)  
- 📧 Email: **manojchoudhary.7.in@gmail.com

---

✨ With this project, you can turn your computer into a voice-powered assistant!  
