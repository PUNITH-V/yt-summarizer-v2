def eval(transcript, final_summary):
    size_t = len(transcript)
    size_s = len(final_summary)
    reduction_percentage = (size_t - size_s) / size_t * 100
    wordc_t = len(transcript.split())
    wordc_s = len(final_summary.split())
    
    return {
        "original_chars": size_t,
        "summary_chars": size_s,
        "compression": reduction_percentage,
        "original_words": wordc_t,
        "summary_words": wordc_s
    }

