import assemblyai as aai

aai.settings.api_key = "413171643bf74d49ae306dc77946403b"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("test_video.mp4")

subtitles = transcript.export_subtitles_srt()

f = open("subtitles.srt","a")

f.write(subtitles)

f.close()


import subprocess
import os

# Define the path to the video and the subtitle file.
video_path = "test_video.mp4"
subtitle_path = "subtitles.srt"
output_video_path = "video_with_subtitles.mp4"

# Make sure both files exist in the current directory.
if not os.path.exists(video_path):
    print(f"Video file '{video_path}' not found.")
elif not os.path.exists(subtitle_path):
    print(f"Subtitle file '{subtitle_path}' not found.")
else:
    # Construct the FFmpeg command to add subtitles to the video.
    ffmpeg_command = [
        "ffmpeg",
        "-i", video_path,            # Input video file
        "-vf", f"subtitles={subtitle_path}",  # Filter to apply the subtitles
        "-c:a", "copy",              # Copy the audio stream without re-encoding
        output_video_path            # Output video file
    ]

    # Execute the FFmpeg command.
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Subtitles added successfully to '{output_video_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add subtitles: {e}")
