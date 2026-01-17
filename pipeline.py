from transcribe import transcribe_video
from emotion_peaks import detect_audio_peaks
from video_utils import create_clip

def generate_reels(video_path):
    transcript = transcribe_video(video_path)
    peaks = detect_audio_peaks(video_path)

    reels = []
    for i, peak in enumerate(peaks[:3]):
        start = max(0, peak - 10)
        end = peak + 20
        output = f"reel_{i+1}.mp4"
        create_clip(video_path, start, end, output)
        reels.append(output)

    return reels
