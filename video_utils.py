from moviepy.editor import VideoFileClip

def create_clip(video_path, start, end, output_name):
    clip = VideoFileClip(video_path).subclip(start, end)
    clip.write_videofile(
        output_name,
        codec="libx264",
        audio_codec="aac"
    )
