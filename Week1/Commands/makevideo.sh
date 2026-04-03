ffmpeg -framerate 30 -i ~/Downloads/frames_30fps/frame_%04d.png -c:v libx264 -pix_fmt yuv420p output.mp4
