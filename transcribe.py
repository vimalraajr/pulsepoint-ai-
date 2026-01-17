import whisper

def transcribe_video(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)

    segments = []
    for seg in result["segments"]:
        segments.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"]
        })

    return segments
