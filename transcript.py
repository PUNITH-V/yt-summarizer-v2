from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def extract_video_id(url):
    return url[-11:]

def get_transcript(url):
    try:
        video_id = extract_video_id(url)
        transcript_list = YouTubeTranscriptApi().fetch(video_id)
        full_text = " ".join([item.text for item in transcript_list])
        return full_text
    except TranscriptsDisabled:
        return "error: transcripts disabled for this video"
    except NoTranscriptFound:
        return "error: no transcript found for this video"
    except Exception as e:
        return f"error:{str(e)}"
    