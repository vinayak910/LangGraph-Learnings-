from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
)


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state:ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages":[response]}

checkpointer = InMemorySaver()
graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node",END)


chatbot = graph.compile(checkpointer= checkpointer)

if __name__ == "__main__":
  # usage example of stream 

    # chatbot.stream will return a generator 
    stream = chatbot.stream(
        # initial state 
        {'messages':[HumanMessage(content = "What is the 5 interesting things about black hole" )]},
        config= {'configurable': {'thread_id': 'thread-1'}},
        stream_mode= "messages"

    )
    print(type(stream))

    for message_chunk, metadata in stream:
        if message_chunk.content:
            print(message_chunk.content , end = " ", flush = True)



