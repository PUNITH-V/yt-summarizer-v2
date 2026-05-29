from dotenv import load_dotenv
import os
from transcript import get_transcript
from chunker import chunk_text
from summarizer import summarize_text, combine_text
from evaluator import eval

load_dotenv()\

api_key = os.getenv("GROQ_API_KEY")

url = "https://www.youtube.com/watch?v=ECHRc3Oan_U"
transcript = get_transcript(url)
chunks = chunk_text(transcript)
partial_summaries = summarize_text(chunks)
final_summary = combine_text(partial_summaries)

print(final_summary)
eval(transcript, final_summary)

