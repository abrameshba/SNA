import json

import networkx as nx
from matplotlib import pyplot as plt

if __name__ == "__main__":
    graph = nx.Graph()
    file = open("/home/ramesh/Downloads/facebook-abrameshba-json/accounts_center/accounts_and_profiles.json", )
    data1 = json.load(file)
    graph.add_node(data1["linked_accounts"][0]["name"])
    file = open("/home/ramesh/Downloads/facebook-abrameshba-json/friends/friends.json", )
    data2 = json.load(file)
    for i in data2['friends']:
        graph.add_node(i["name"])
        graph.add_edge(data1["linked_accounts"][0]["name"], i["name"])
    nx.draw(graph, with_labels=True)
    plt.show()
