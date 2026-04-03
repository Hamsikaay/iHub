mkdir -p ~/Downloads/frames_30fps && ffmpeg -ss 0 -t 60 -i "input.mp4" -vf fps=30 ~/Downloads/frames_30fps/frame_%04d.png
