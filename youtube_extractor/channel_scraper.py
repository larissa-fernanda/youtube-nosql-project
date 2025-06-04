from youtool import YouTube
import os

def create_youtube_instance():
    api_keys = os.getenv("YT_API_KEYS").split(",")
    return YouTube(api_keys, disable_ipv6=True)

def get_channel_id_from_url(yt: YouTube, channel_url: str) -> str:
    return yt.channel_id_from_url(channel_url)

def get_upload_playlist_id(channel_id: str) -> str:
    assert channel_id.startswith("UC")
    return "UU" + channel_id[2:]

def get_uploads_videos(yt: YouTube, playlist_id: str, max_results=5):
    videos = []
    for video in yt.playlist_videos(playlist_id):
        videos.append(video)
        if len(videos) >= max_results:
            break
    video_ids = [v["id"] for v in videos]
    return yt.videos_infos(video_ids)
