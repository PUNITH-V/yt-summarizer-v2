import streamlit as st
from transcript import get_transcript
from chunker import chunk_text
from summarizer import summarize_text, combine_text
from evaluator import eval

st.title("YouTube Video Summarizer")
st.write("Paste a YouTube URL to get a concise summary")

url = st.text_input("YouTube URL")

if st.button("Summarize"):
    if url:
        with st.spinner("Fetching transcript..."):
            transcript = get_transcript(url)
        
        if transcript.startswith("error"):
            st.error(transcript)
        else:
            with st.spinner("Summarizing..."):
                chunks = chunk_text(transcript)
                partial_summaries = summarize_text(chunks)
                final_summary = combine_text(partial_summaries)
            
            st.subheader("Summary")
            st.write(final_summary)
            
            st.subheader("Evaluation")
            metrics = eval(transcript, final_summary)
            col1, col2, col3 = st.columns(3)
            col1.metric("Original Words", f"{metrics['original_words']:,}")
            col2.metric("Summary Words", f"{metrics['summary_words']:,}")
            col3.metric("Compression", f"{metrics['compression']:.1f}%")
    else:
        st.warning("Please enter a YouTube URL")