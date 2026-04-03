mkdir -p ~/Downloads/sample_frames && ffmpeg -i "input.mp4" -vf "select='not(mod(n\,1000))'" -fps_mode vfr ~/Downloads/sample_frames/frame_%02d.png
