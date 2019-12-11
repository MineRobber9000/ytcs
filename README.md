# YouTube Caption Search

Searches captions of indexed YouTube videos.

## Setup

Get a YouTube API key, and put it in `~/.config/ytsts.ini`. The INI file should look like:

```
[auth]
api_key=THISISNOT_ANAPIKEY0SILLY
```

# How to use

## How to index videos

To index a video, give a list of URLs to `python indexer.py`.

Types of URLs you can feed the indexer:

* `https://www.youtube.com/watch?v=<VIDEO_ID>`
* `https://m.youtube.com/watch?v=<VIDEO_ID>`
* `https://youtu.be/<VIDEO_ID>`

Alternatively, you can supply raw video IDs.

## How to search your index

Once you've indexed your videos, there are 2 ways to search.

### Method 1: Command-line

```
$ python search.py "the glitch"
1) Sonic Adventure 2 (Hero Story) | Real-Time Fandub Games (https://youtu.be/po1qdT7mj-s)
```

### Method 2: Python import

```python
import index

results = index.search("the glitch")
# [{'description': 'A group of voice actors dub the dialogue from Sonic Adventure 2... in one take... with zero rehearsal. This is the result.\n(CAST AND MORE INFO BELOW)\n\nVOICE CAST:\nSonic - https://twitter.com/SnapsCube\nShadow - http://www.youtube.com/chongoshow/\nTails and Rouge - http://www.twitter.com/bluespacequeen/\nKnuckles and Amy - http://www.youtube.com/hayleycopter/\nEggman - http://www.twitter.com/paperboxhouse/\n\nReal-Time Fandub created by Charley Marlowe\nhttps://www.youtube.com/channel/UC6PRvqd1opmIPrWbcq-SiCA\n\nSpecial thanks to Windii and Cobanermani456 for the footage from this game!\nhttps://www.youtube.com/user/WindiiGitlord\nhttps://www.youtube.com/user/cobanermani456\n\n♥ New videos or streams on weekdays! ♥\n\nI have a Patreon for those who would be interested in supporting me financially! ► https://www.patreon.com/SnapCube\n\nSpecial thanks to my already existing Patrons! ► \nhttps://docs.google.com/document/d/1O63BNueCkYfo847dUD76-CBaIMAw9jIjTsWObMGLles/edit?usp=sharing\n\nMain Channel ► https://www.youtube.com/channel/UCY0sI1rSrXJQOFlTuh3UsxA\nTwitter ► https://twitter.com/SnapsCube\nTumblr ► http://snapscube.tumblr.com/\nTwitch ► https://www.twitch.tv/snapscube\n\nIntro Art/Animation by \nhttp://www.twitter.com/katidoj/\n\nOutro Music \nhttps://youtu.be/yzIw_g7F0uE?t=6m1s\n\nOutro Penny art by\nhttp://www.twitter.com/hynorin/', 'title': 'Sonic Adventure 2 (Hero Story) | Real-Time Fandub Games', 'url': 'https://youtu.be/po1qdT7mj-s'}]
```
