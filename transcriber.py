import whisper

model = whisper.load_model("medium")  # You can choose different model sizes like 'tiny', 'base', 'small', 'medium', or 'large'

result = model.transcribe("goat.mp3")
print(result["text"])
