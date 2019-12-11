from googleapiclient.discovery import build
from configparser import ConfigParser
import os, re, argparse, bs4, requests, index, traceback, html

YT_VIDEO_URL = re.compile(r"https?://(?:(?:www\.|m\.)youtube.com/watch\?v=|youtu.be/)([A-Za-z0-9\-_]+)")

config = ConfigParser()
config.read(os.path.expanduser("~/.config/ytsts.ini"))

yt = build("youtube","v3",developerKey=config["auth"]["api_key"])

def parse_video(v):
	m = YT_VIDEO_URL.match(v)
	if not m: return v
	return m.group(1)

def get_captions(videoId):
	try:
		url = "https://www.youtube.com/api/timedtext?lang=en&v="+videoId
		r = requests.get(url)
		soup = bs4.BeautifulSoup(r.content,"lxml")
		texts = soup("text")
		out = []
		for text in texts:
			out.append(html.unescape(text.text.strip()))
		return "\n\n".join(out)
	except:
		traceback.print_exc()
		return ""

def index_urls(videos):
	videos = [parse_video(x) for x in videos]

	results = yt.videos().list(
		part="snippet",
		id=",".join(videos)
	).execute()

	for item in results.get("items",[]):
		title = item["snippet"]["title"]
		description = item["snippet"]["description"]
		url = "https://youtu.be/"+item["id"]
		transcript = get_captions(item["id"])
		index.add_to_index(title,description,transcript,url)

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("video",help="Video URL or ID",nargs="+")
	args = parser.parse_args()
	index_urls(args.video)

