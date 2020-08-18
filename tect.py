import pytube
import subprocess
import os


def change_duration(old_file, new_file, start, duration, delete_old_file):
	subprocess.run([
		'ffmpeg',
		'-i',
		old_file,
		'-ss',
		start,
		'-t',
		duration,
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
		return e


def mp4_to_mp3(mp4_file, mp3_file, delete_old_file):
	inter_file = "inter_file.mp3"
	subprocess.run([
		'ffmpeg',
		'-i',
		mp4_file,
		'-f',
		'mp3',
		'-vn',
		inter_file],
		capture_output=True)

	''' The second subprocess is run to solve the itunes problems. Not yet sure why this problem actually occurs as no resources avalaible but this works just fine for now'''
	subprocess.run([
		'ffmpeg',
		'-i',
		inter_file,
		'-acodec',
		'copy',
		mp3_file],
		capture_output=True)

	os.remove(inter_file)
	if delete_old_file:
		os.remove(mp4_file)


def video_info(url):
	info_dict = {}
	try:
		vid = pytube.YouTube(url)
		streams = vid.streams
		# info_dict["title"] = vid.title
		# info_dict["streams"] = [{}]
		for stream in streams:
			print(stream)
			# dic = {}
			# dic["itag"] = stream.itag
			# dic["type"] = stream.mime_type
			# dic["abr"] = stream.abr
			# info_dict["streams"].append(dic)

		# return info_dict

	except Exception as e:
		return e


# video_info('https://www.youtube.com/watch?v=6su62xI2x2Q')
# print(var)
# download_mp4('https://www.youtube.com/watch?v=cfSqTxJNLd8', '18')
mp4_to_mp3('Madoromi.mp4', 'Madoromi1.mp3', False)
# change_duration('Madoromi1.mp4', 'Madoromi_half.mp4', '00:00:00', '00:04:23', False)