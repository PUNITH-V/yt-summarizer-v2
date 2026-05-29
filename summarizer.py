from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()


def summarize_text(chunks):

    llm = ChatGroq(
    model= "llama-3.1-8b-instant",
    temperature=0.7
)

    list_data = []

    for chunk in chunks:

        messages = [
            SystemMessage(
                content="You are a helpful assistant that summarizes text concisely"
            ),
            HumanMessage(
                content=f"Summarize this following text in 3-4 concise sentences:\n\n{chunk}"
            )
        ]

        response = llm.invoke(messages)

        list_data.append(response.content)

    return list_data


def combine_text(list_data):

    llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

    final_text = "\n\n".join(list_data)

    messages = [
        SystemMessage(
            content="You are a helpful assistant that combines summaries into one coherent summary."
        ),
        HumanMessage(
            content=f"Combine these summaries into one coherent final summary:\n\n{final_text}"
        )
    ]

    response = llm.invoke(messages)

    return response.content
