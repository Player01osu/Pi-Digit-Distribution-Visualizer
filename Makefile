all:
	./generator.py
	ffmpeg -framerate 30 -pattern_type glob -i 'images/*.png' -c:v libx264 -pix_fmt yuv420p out.mp4
