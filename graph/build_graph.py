import networkx as nx
import pandas as pd

def build_entity_graph(df: pd.DataFrame) -> nx.DiGraph:
    G = nx.DiGraph()
    for _, row in df.iterrows():
        sender = row["sender_name"]
        receiver = row["receiver_name"]
        amount = row["amount"]
        G.add_node(sender)
        G.add_node(receiver)
        G.add_edge(sender, receiver, weight=amount)
    return G
