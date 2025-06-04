import os
from dotenv import load_dotenv
from database.mongo_handler import save_to_collection
from youtube_extractor.channel_scraper import (
create_youtube_instance,
get_channel_id_from_url,
get_upload_playlist_id,
get_uploads_videos
)
from youtube_extractor.video_scraper import extract_video_details
from analysis.insights import plot_comment_count, plot_wordcloud

def main():
    load_dotenv()
    yt = create_youtube_instance()
    channel_url = input("URL do canal: ")
    channel_id = get_channel_id_from_url(yt, channel_url)
    playlist_id = get_upload_playlist_id(channel_id)
    print("🎥 Coletando vídeos do canal...")
    videos = get_uploads_videos(yt, playlist_id, max_results=5)

    for video in videos:
        print(f"📥 Coletando dados de: {video['title']}")
        details = extract_video_details(yt, video["id"])
        record = {
            **video,
            **details
        }
        save_to_collection("videos", record)

    print("✅ Dados salvos no MongoDB.")
    plot_comment_count()
    plot_wordcloud()

if __name__ == "__main__":
    main()
