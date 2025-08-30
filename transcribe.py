# ----------------------------------------------------
# Setup (install required packages)
# ----------------------------------------------------
# Run these commands in terminal if not already installed:
# pip install git+https://github.com/openai/whisper.git
# pip install pydub SpeechRecognition gradio openai
# sudo apt install ffmpeg

# ----------------------------------------------------
# Method 1 : Simple Whisper Transcription
# ----------------------------------------------------
import whisper

print("\n=== Method 1: Simple Transcription ===")
model = whisper.load_model("base")
result = model.transcribe("what.mp3", fp16=False)

print("Transcription Result Keys:", result.keys())
print("Transcribed Text:", result["text"])

# ----------------------------------------------------
# Method 2 : Low-level Whisper Access
# ----------------------------------------------------
print("\n=== Method 2: Low-level Access ===")
audio = whisper.load_audio("what.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions(fp16=False)
low_result = whisper.decode(model, mel, options)
print("Decoded Text:", low_result.text)

# ----------------------------------------------------
# Method 3 : Google SpeechRecognition
# ----------------------------------------------------
print("\n=== Method 3: Google SpeechRecognition ===")
import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile("what.wav") as source:
    audio_text = r.listen(source)

g = r.recognize_google(audio_text, show_all=True)
print("Google Recognition Keys:", g.keys())
print("Google Transcribed Text:", g['alternative'][0]['transcript'])

# ----------------------------------------------------
# Handling Longer Inputs (Whisper has 25MB file limit)
# ----------------------------------------------------
print("\n=== Splitting Long Audio ===")
from pydub import AudioSegment

song = AudioSegment.from_mp3("good_morning.mp3")

# PyDub handles time in milliseconds
ten_minutes = 10 * 60 * 1000
first_10_minutes = song[:ten_minutes]

first_10_minutes.export("good_morning_10.mp3", format="mp3")
print("Exported first 10 minutes of audio -> good_morning_10.mp3")

