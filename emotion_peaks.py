import librosa
import numpy as np

def detect_audio_peaks(video_path):
    audio, sr = librosa.load(video_path, sr=None)
    energy = librosa.feature.rms(y=audio)[0]

    threshold = np.mean(energy) + np.std(energy)
    peak_frames = np.where(energy > threshold)[0]

    peak_times = librosa.frames_to_time(peak_frames, sr=sr)
    return peak_times
