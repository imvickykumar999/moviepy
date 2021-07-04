
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip as vix

# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")

original = "dark love.mp4"
# trimmed = original.split('.')[0]+'_trim.mp4'
trimmed = 'cut.mp4'

vix(original, 76, 300, targetname=trimmed)
