from moviepy.video.io.VideoFileClip import VideoFileClip

# Open the video file
video = VideoFileClip("C:/Users/sandeep/Downloads/Y2meta.app - Hrithik with Priyanka best performance(360p).mp4")

# Get the frames per second (fps)
fps = video.fps

# Get the frame width and height
width = video.w
height = video.h

# Get the codec
codec = video.fps

# Get the duration
duration = video.duration



# Print the properties
print("FPS:", fps)
print("Resolution:", width, "x", height)
print("Codec:", codec)
print("Duration:", duration)
