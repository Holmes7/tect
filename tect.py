import pytube

url = "https://www.youtube.com/watch?v=wAtKRPX0RO4"

try:
	video_obj = pytube.YouTube(url)
	stream = video_obj.streams.filter(only_audio=True)
	for i in stream:
		print(i)

except:
	print("The video probably isn't downloadable")
