
# https://github.com/Zulko/moviepy/issues/504#issuecomment-288806522

from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.editor as mpe

videoclip = VideoFileClip("cut.mp4")
background_music = mpe.AudioFileClip("Gajban - Sapna Choudhary.mp3")

new_clip = videoclip.set_audio(background_music)
new_clip.write_videofile("audio added.mp4")
