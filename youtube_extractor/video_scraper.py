from youtool import YouTube
from chat_downloader.errors import NoChatReplay, ChatDisabled, LoginRequired
import os

def extract_video_details(yt: YouTube, video_id: str) -> dict:
    comments = list(yt.video_comments(video_id))
    livechat = []

    try:
        livechat = list(yt.video_livechat(video_id))
    except (NoChatReplay, ChatDisabled, LoginRequired) as e:
        print(f"⚠️ Skipping livechat for video {video_id}: {e}")

    # Ensure transcript directory exists
    transcript_dir = "./transcripts"
    os.makedirs(transcript_dir, exist_ok=True)

    transcript_path = yt.download_transcriptions([video_id], "pt", transcript_dir)

    return {
        "video_id": video_id,
        "comments": comments,
        "livechat": livechat,
        "transcript_info": transcript_path
    }