from googleapiclient.discovery import build
from config import get_api_key
import pandas as pd

def get_channel_videos(channel_id):
    api_key = get_api_key()
    youtube = build('youtube', 'v3', developerKey=api_key)

    video_ids = []
    next_page_token = None

    # Step 1: Get uploads playlist ID
    channel_res = youtube.channels().list(id='UCeVMnSShP_Iviwkknt83cww', part='contentDetails').execute()
    uploads_id = channel_res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Step 2: Get all video IDs from the uploads playlist
    while True:
        pl_request = youtube.playlistItems().list(
            playlistId=uploads_id,
            part='contentDetails',
            maxResults=50,
            pageToken=next_page_token
        )
        pl_response = pl_request.execute()

        for item in pl_response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        next_page_token = pl_response.get('nextPageToken')
        if not next_page_token or len(video_ids) >= 1000:
            break

    # Step 3: Fetch stats for each video
    videos = []
    for i in range(0, len(video_ids), 50):
        video_request = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            id=','.join(video_ids[i:i+50])
        )
        video_response = video_request.execute()

        for video in video_response['items']:
            videos.append({
                'title': video['snippet']['title'],
                'publishedAt': video['snippet']['publishedAt'],
                'duration': video['contentDetails']['duration'],
                'views': int(video['statistics'].get('viewCount', 0)),
                'likes': int(video['statistics'].get('likeCount', 0)),
                'comments': int(video['statistics'].get('commentCount', 0)),
            })

    df = pd.DataFrame(videos)
    df.to_csv("youtube_data.csv", index=False)
    print("Data saved to youtube_data.csv")
