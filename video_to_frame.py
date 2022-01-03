from video_cut import video_cut
from video_capture import videoCapture

video_path = './video/'
f_save_path = './video_frame/'
count = 1
width = 640
height = 480
videoCapture(video_path, count, width, height)
video_cut(video_path, f_save_path)

