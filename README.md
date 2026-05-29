
# YouTube Video Summarizer

Summarizes any YouTube video into a concise summary using map-reduce summarization.

🚀 **Live Demo:** [[Streamlit ](https://youtube-summarizer-v2.streamlit.app/)]

## How It Works
YouTube URL → Fetch Transcript → Chunk Text → Summarize Each Chunk → Combine → Final Summary
1. Fetches transcript using YouTube Transcript API
2. Splits transcript into 1000-char chunks with 100-char overlap
3. Summarizes each chunk individually using Llama3 via Groq
4. Combines partial summaries into one coherent final summary
5. Evaluates compression ratio and word count

## Results
- Tested on 20,538 character transcripts
- Achieves ~67-70% compression consistently
- Reduces 3,000+ words to under 1,000 words

## Tech Stack
- Python
- LangChain
- Groq (Llama3)
- YouTube Transcript API
- Streamlit

## Setup

1. Clone the repo
git clone https://github.com/PUNITH-V/yt-summarizer-v2

2. Install dependencies
pip install -r requirements.txt

3. Add environment variables
Create a .env file:
GROQ_API_KEY=your_key_here

4. Run
streamlit run app.py


## Project Structure
````markdown
## 📂 Project Structure

```text
yt-summarizer-v2/
│
├── streamlit_app.py      # Streamlit frontend UI
├── transcript.py         # Fetches transcripts from YouTube videos
├── chunker.py            # Splits large transcripts into manageable chunks
├── summarizer.py         # Map-Reduce based summarization using Groq LLM
├── evaluator.py          # Calculates summary evaluation metrics
├── main.py               # Command-line interface entry point
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
````

### 📄 File Descriptions

| File                 | Purpose                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| **streamlit_app.py** | Main Streamlit application providing the user interface.                                       |
| **transcript.py**    | Extracts and retrieves transcripts from YouTube videos using the YouTube Transcript API.       |
| **chunker.py**       | Breaks long transcripts into smaller chunks suitable for LLM processing.                       |
| **summarizer.py**    | Implements a Map-Reduce summarization pipeline using Groq's LLMs.                              |
| **evaluator.py**     | Computes summary statistics such as compression ratio and word counts.                         |
| **main.py**          | CLI-based entry point for running the summarizer from the terminal.                            |
| **requirements.txt** | Contains all Python dependencies required by the project.                                      |
| **README.md**        | Documentation, setup instructions, and project overview.                                       |
| **.gitignore**       | Excludes unnecessary files and directories (e.g., `venv`, `__pycache__`) from version control. |

---

## 🔄 Workflow

```text
YouTube URL
     │
     ▼
Transcript Extraction
     │
     ▼
Text Chunking
     │
     ▼
Chunk Summarization (Map Phase)
     │
     ▼
Summary Combination (Reduce Phase)
     │
     ▼
Final Summary
     │
     ▼
Evaluation Metrics
```

---

## 🏗️ Architecture Overview

1. **User Input**

   * User provides a YouTube video URL through the Streamlit interface.

2. **Transcript Retrieval**

   * The application extracts the video ID and fetches the transcript using the YouTube Transcript API.

3. **Text Chunking**

   * Long transcripts are divided into smaller chunks using LangChain's Recursive Character Text Splitter.

4. **Map Phase**

   * Each chunk is independently summarized using Groq's Llama model.

5. **Reduce Phase**

   * Individual summaries are merged into a coherent final summary.

6. **Evaluation**

   * Metrics such as original word count, summary word count, and compression ratio are calculated and displayed.

7. **Output**

   * The final summary and evaluation metrics are presented in the Streamlit dashboard.

---
## Limitations

Only works on videos with captions enabled
Very long videos may hit API rate limits
Auto-generated captions may have transcription errors

## Author

Punith V | [LinkedIn](https://www.linkedin.com/in/punith-v1/) | [GitHub](https://github.com/PUNITH-V/yt-summarizer-v2)
