import moviepy.editor as mp

clip = mp.VideoFileClip("cut.mp4")
# clip = clip.subclip(0,20)

clip.audio.write_audiofile("audio.mp3")
