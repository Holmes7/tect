import pytube
import subprocess
import os


def change_duration(old_file, new_file, start, end, delete_old_file):
	subprocess.run([
		'ffmpeg',
		'-ss',
		start,
		'-i',
		old_file,
		'-to',
		end,
		'-c',
		'copy',
		new_file],
		capture_output=True)

	if delete_old_file:
		os.remove(old_file)


def download_mp4(url, itag):
	try:
		vid = pytube.YouTube(url)
		stream = vid.streams.get_by_itag(itag)
		stream.download()
		return True

	except Exception as e:
		return False


def mp4_to_mp3(mp4_file, mp3_file, delete_old_file):
	subprocess.run([
		'ffmpeg',
		'-i',
		mp4_file,
		mp3_file])

	if delete_old_file:
		os.remove(mp4_file)


def video_info(url):
	info_dict = {}
	try:
		vid = pytube.YouTube(url)
		streams = vid.streams
		info_dict["title"] = vid.title
		info_dict["streams"] = [{}]
		for stream in streams:
			dic = {}
			dic["itag"] = stream.itag
			dic["type"] = stream.mime_type
			dic["abr"] = stream.abr
			info_dict["streams"].append(dic)

		return info_dict

	except Exception as e:
		return e


# var = video_info('https://www.youtube.com/watch?v=6su62xI2x2Q')
# print(var)
# download_mp4('https://www.youtube.com/watch?v=6su62xI2x2Q', '140')
# mp4_to_mp3('123.mp4', '143.mp3', False)
change_duration('143.mp3', '144.mp3', '00:00:00', '00:05:00', False)