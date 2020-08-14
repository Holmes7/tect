import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="link to the video")
parser.add_argument("--info", "-i", help='''get information on different files
	available''', action="store_true")
parser.add_argument("--download", "-d", help='''downloads the file from the url
	with the provided itag''')
args = parser.parse_args()
