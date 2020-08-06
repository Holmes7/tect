import pytube
import argparse
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy

parser = argparse.ArgumentParser()
parser.add_argument("url", help="link to the video")
parser.add_argument("--info", "-i", help='''get information on different files
	available''', action="store_true")
parser.add_argument("--download", "-d", help='''downloads the file from the url
	with the provided itag''')
args = parser.parse_args()

url = args.url

if args.info:
	try:
		vid = pytube.YouTube(url)
		print(vid.title)
		streams = vid.streams
		for stream in streams:
			# print(stream)
			print(f'''itag={stream.itag} type={stream.mime_type} abr={stream.abr}''')

	except Exception as e:
		print(e)

if args.download:
	try:
		vid = pytube.YouTube(url)
		stream = vid.streams.get_by_itag(args.download)
		print(f'''itag={stream.itag} type={stream.mime_type} abr={stream.abr}''')
		# stream.download()
		len = vid.length
		old_mp4_file = f'{vid.title}.mp4'
		mp4_file = f'{vid.title}1.mp4'
		mp3_file = f'{vid.title}.mp3'
		mp3_file = f'{vid.title}.mp3'
		ffmpeg_extract_subclip(old_mp4_file, 0, len - 1, targetname=mp4_file)

	except Exception as e:
		print(e)
