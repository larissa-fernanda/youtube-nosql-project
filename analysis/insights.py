import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from collections import Counter

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

def plot_comment_count():
    videos = db.videos.aggregate([
        {"$group": {"_id": "$title", "comments": {"$last": "$comments"}, "comments_count": {"$last": {"$size": "$comments"}}}},
        {"$project": {"title": "$_id", "comments": 1, "comments_count": 1}},
        {"$sort": {"comments_count": -1}},
        {"$limit": 5}
    ])
    labels = []
    values = []
    for v in videos:
        labels.append(v['title'][:20])
        values.append(len(v['comments']))
    plt.barh(labels, values)
    for i, v in enumerate(values):
        plt.text(v, i, str(v), va='center')
    plt.title("Nº de comentários por vídeo")
    plt.tight_layout()
    plt.show()

def plot_wordcloud():
    videos = db.videos.aggregate([
        {"$group": {"_id": "$title", "comments": {"$last": "$comments"}, "comments_count": {"$last": {"$size": "$comments"}}}},
        {"$project": {"title": "$_id", "comments": 1, "comments_count": 1}},
        {"$sort": {"comments_count": -1}},
        {"$limit": 5}
    ])
    comments = []
    for v in videos:
        comments += [c['text'] for c in v['comments'] if 'text' in c]
        text = " ".join(comments)
    wc = WordCloud(width=800, height=400).generate(text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Palavras mais frequentes")
    plt.show()
