from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from typing import Annotated
from agent.extractor import get_attributes
from transcritor import transcritor
from amadeus import search_flights
from mcp_server_airbnb.airbnbmcpclient import airbnb_search

class State(TypedDict):
    messages: Annotated[list, add_messages]
    content: dict
    flightsContent: dict
    airbnbContent: dict

def process_audio(state: State):
    informations = get_attributes(transcritor(state['messages'][0].content))
    return {"content": informations}

def search_in_airbnb(state: State):
    return {"airbnbContent": airbnb_search(state['content']['host'])}

def search_in_flights(state: State):
    return {"flightsContent": search_flights(state['content']['flight'])}

def get_response(state: State):
    return {'messages': [{
        'role': 'assistant',
        'content': [{
            'airbnb_results': state['airbnbContent'],
            'flight_results': state['flightsContent']
        }]
    }]}

graph_builder = StateGraph(State)

graph_builder.add_node('process_audio', process_audio)
graph_builder.add_node("search_airbnb", search_in_airbnb)
graph_builder.add_node("search_flights", search_in_flights)
graph_builder.add_node('get_response', get_response)

graph_builder.add_edge(START, 'process_audio')
graph_builder.add_edge('process_audio', "search_airbnb")
graph_builder.add_edge('process_audio', "search_flights")
graph_builder.add_edge("search_airbnb", 'get_response')
graph_builder.add_edge("search_flights", 'get_response')
graph_builder.add_edge('get_response', END)


graph = graph_builder.compile()

def stream_graph_updates(audio_path: str):
    for event in graph.stream({"messages": [{'role': 'user', 'content': audio_path}]}):
        for value in event.values():
            print("Assistant:", value)


