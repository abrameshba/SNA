import json

import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # create self node in the graph
    graph = nx.Graph()
    file = open("/home/ramesh/Downloads/facebook-abrameshba-json/accounts_center/accounts_and_profiles.json", )
    data1 = json.load(file)
    graph.add_node(data1["linked_accounts"][0]["name"])
    # create friend nodes as recieved rejected and sent
    file = open("/home/ramesh/Downloads/facebook-abrameshba-json/friends/received_friend_requests.json", )
    data = json.load(file)
    received_requests = []
    for i in data["received_requests"]:
        received_requests.append(i['name'])
        graph.add_node(i["name"], color="#0000FF")
        graph.add_edge(data1["linked_accounts"][0]["name"], i["name"])
    file = open("/home/ramesh/Downloads/facebook-abrameshba-json/friends/rejected_friend_requests.json", )
    data = json.load(file)
    rejected_requests = []
    for i in data["rejected_requests"]:
        rejected_requests.append(i['name'])
        graph.add_node(i["name"],color="#FF0000")
        graph.add_edge(data1["linked_accounts"][0]["name"], i["name"])
    file = open("/home/ramesh/Downloads/facebook-abrameshba-json/friends/sent_friend_requests.json", )
    data = json.load(file)
    sent_requests = []
    for i in data["sent_requests"]:
        sent_requests.append(i['name'])
        graph.add_node(i["name"],color="#0000FF")
        graph.add_edge(data1["linked_accounts"][0]["name"], i["name"])
    # plot graph as traffic lights
    file = open("/home/ramesh/Downloads/facebook-abrameshba-json/friends/friends.json", )
    data2 = json.load(file)
    existing_friend = []
    for i in data2['friends']:
        graph.add_node(i["name"], color="#00FF00")
        if i['name'] in rejected_requests or i['name'] in received_requests or i['name'] in sent_requests:
            pass
        else:
            existing_friend.append(i['name'])
        graph.add_edge(data1["linked_accounts"][0]["name"], i["name"])
    pos = nx.spring_layout(graph)  # positions for all nodes
    nx.draw_networkx_nodes(graph, pos, nodelist=received_requests, node_size=2, node_color='#0000FF')
    nx.draw_networkx_nodes(graph, pos, nodelist=rejected_requests, node_size=1, node_color='#FF0000')
    nx.draw_networkx_nodes(graph, pos, nodelist=sent_requests, node_size=2, node_color='#0000FF')
    nx.draw_networkx_nodes(graph, pos, nodelist=existing_friend, node_size=3, node_color="#00FF00")
    nx.draw_networkx(graph, pos=pos)
    # nx.draw_networkx(graph.subgraph(received_requests), pos=pos)
    # nx.draw_networkx(graph.subgraph(rejected_requests), pos=pos)
    # nx.draw_networkx(graph.subgraph(sent_requests), pos=pos)
    # plt.savefig('/home/ramesh/Downloads/facebook-abrameshba.eps' , format='eps')
    # plt.savefig('/home/ramesh/Downloads/facebook-abrameshba.svg', format='svg', dpi=1200)
    # nx.write_graphml(graph, '/home/ramesh/Downloads/facebook-abrameshba.graphml')
    nx.write_gml(graph, '/home/ramesh/Downloads/facebook-abrameshba.gml')
    nx.write_graph6(graph, '/home/ramesh/Downloads/facebook-abrameshba.g6')
    nx.write_pajek(graph, '/home/ramesh/Downloads/facebook-abrameshba.pajek')
    plt.show()
    print(received_requests)

