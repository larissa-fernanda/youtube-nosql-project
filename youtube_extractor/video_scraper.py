from youtool import YouTube

def extract_video_details(yt: YouTube, video_id: str) -> dict:
    comments = list(yt.video_comments(video_id))
    # Fetch live chat messages if available
    if not yt.video_livechat(video_id):
        livechat = []
    else:
        livechat = list(yt.video_livechat(video_id))
    transcript_path = yt.download_transcriptions([video_id], language_code="pt")
    return {
        "video_id": video_id,
        "comments": comments,
        "livechat": livechat,
        "transcript_info": transcript_path
        }
