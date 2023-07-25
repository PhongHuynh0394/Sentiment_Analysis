import os
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv


load_dotenv()
def get_comments(youtube, url, max_cmts = 150, comments = [], token='') -> list:
    vid_id = url.split("v=")[-1]
    if "&t=" in vid_id:
       vid_id = vid_id.split('&t')[0]

    request = (youtube.commentThreads().list(
              part='snippet',
              textFormat='plainText',
              maxResults=max_cmts,
              pageToken=token,
              videoId=vid_id
              ))
    response = request.execute()
    for item in response['items']:
      comments.append(item['snippet']['topLevelComment']['snippet']['textOriginal'])
    if 'nextPageToken' in response:
      return get_comments(youtube, url, max_cmts, comments, response['nextPageToken'])

    return comments

def crawl_youtube_comments(url: str):
  #load_dotenv()
  api_service_name = "youtube"
  API_KEY = os.getenv('API_KEY') 
  api_version = "v3"
  youtube = build(api_service_name, api_version, developerKey = API_KEY)
  return get_comments(youtube, url)
