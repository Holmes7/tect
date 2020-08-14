import pytube
import subprocess
import os


def change_duration(file, start, end):
	pass


def download_mp4(url, itag):
	try:
		vid = pytube.YouTube(url)
		stream = vid.streams.get_by_itag(itag)
		stream.download()
		return True

	except Exception as e:
		return False


def mp4_to_mp3(mp4_path, new_name, delete):
	pass


def video_info(url):
	info_dict = {}
	try:
		vid = pytube.Youtube(url)
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
		return False
