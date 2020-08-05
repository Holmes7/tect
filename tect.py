import pytube
import argparse

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
		print(stream)
		stream.download()

	except Exception as e:
		print(e)

