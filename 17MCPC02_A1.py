#!/usr/bin/python3
# coding: utf-8


# import pdb
import networkx as nx
import matplotlib.pyplot as plt
import collections
import time
from scipy.optimize import curve_fit
import numpy as np
# from pandas import read_csv
# fit a line to the economic data
# from numpy import sin
# from numpy import sqrt
from numpy import arange


# pdb.set_trace()

def show_head(lst):
    for val in lst[:5]:
        print(val)


# define the true objective function
def objective(alpha, a, b):
    return a * (alpha ** b)


start = time.time()

# graph.name = "fb-pages-media"
# with open("/home/cilab/Downloads/SNA/fb-pages-media.nodes", "r") as file:
#    for line in file:
#        words = line.strip("\n ").split(",")
#        if len(words)==3:
#            graph.add_node(words[2],nname=words[1],sid=words[0])
#        else:
#            pass
# with open("/home/cilab/Downloads/SNA/fb-pages-media.edges", "r") as file:
#    for line in file:
#        words = line.strip("\n ").split(",")
#        if len(words)==2 and words[0] in graph and words[1] in graph:
#            graph.add_edge(words[0],words[1])


# undirected network
graph = nx.read_gml("../geom.gml")
graph.name = "Collaboration network in computational geometry"

# graph = nx.read_gml("/home/cilab/Downloads/SNA/netscience.gml")
# graph.name = "Newman coauthorship"


# Directed network
# graph = nx.read_gml("DaysAll.gml")
# graph.name = "Reuters terror news network"

print(nx.info(graph))
print("Directed : " + str(nx.is_directed(graph)))
print("Weighted : " + str(nx.is_weighted(graph)))
print("Loops : True") if nx.number_of_selfloops(graph) > 0 else print("self loops : False")
print("Clustering :" + str(nx.transitivity(graph)))
print("Number of Components : ", nx.number_connected_components(graph))

gcc = graph.subgraph(max(nx.connected_components(graph), key=len)).copy()
degree_sequence = sorted([d for n, d in gcc.degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
# a = 2480.4587
# b = -1.8219
# with open("geom.txt", "w") as file:
#     for i in range(len(deg)):
#         y = a * (deg[i] ** b)
#         file.write(str(deg[i]) + " " + str(cnt[i]) + " " + str(y) + "\n")
#         file.write(str(deg[i]) + " " + str(cnt[i]) + "\n")
plt.bar(deg, cnt)
plt.xlabel("Degree of scientists")
plt.ylabel("Number of scientists")
plt.title("Degree Histogram")
plt.savefig('17MCPC02-01.png')
plt.show()
# while nx.is_connected(gcc):
for _ in range(5):
    print("\n")
    print(nx.info(gcc))
    #    l_start = time.time()
    print("Radius of GCC : ", nx.radius(gcc))
    #    print(time.time()-l_start)
    #    l_start = time.time()
    print("Diameter of GCC : ", nx.diameter(gcc))
    #    print(time.time()-l_start)
    #    l_start = time.time()
    print("Density of GCC : ", nx.density(gcc))
    #    print(time.time()-l_start)
    #    l_start = time.time()
    dc_dict = nx.degree_centrality(gcc)
    print("Degree centrality : ")
    #    print(time.time()-l_start)
    dc_list = sorted([(key, dc_dict[key]) for key in dc_dict], key=lambda v: v[1], reverse=True)
    show_head(dc_list)
    #    l_start = time.time()
    cc_dict = nx.closeness_centrality(gcc)
    print("Closeness centrality : ")
    #    print(time.time()-l_start)
    cc_list = sorted([(key, cc_dict[key]) for key in cc_dict], key=lambda v: v[1], reverse=True)
    show_head(cc_list)
    #    l_start = time.time()
    c_dict = nx.clustering(gcc)
    print("Clustering : " + str(nx.transitivity(gcc)))
    #    print(time.time()-l_start)
    c_list = sorted([(key, c_dict[key]) for key in c_dict], key=lambda v: v[1], reverse=True)
    # nx.draw(gcc, with_labels=True)
    # plt.show()
    #    l_start = time.time()
    bc_dict = nx.betweenness_centrality(gcc)
    print("Betweenness centrality :")
    #    print(time.time()-l_start)
    bc_list = sorted([(key, bc_dict[key]) for key in bc_dict], key=lambda v: v[1], reverse=True)
    show_head(bc_list)
    gcc.remove_node(bc_list[0][0])
    print("Removing :")
    print(bc_list[0][0], bc_list[0][1])
    # nx.draw(gcc, with_labels=True)
    # plt.show()
    print("Number of Components : ", nx.number_connected_components(gcc))
    gcc = gcc.subgraph(max(nx.connected_components(gcc), key=len)).copy()
print("Total run time in sec")
print(time.time() - start)

# curve fit
popt, _ = curve_fit(objective, np.array(deg), np.array(cnt))
# summarize the parameter values
x, y = popt
# print(popt)
# print(pcov)
# plot input vs output
plt.scatter(deg, cnt)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(np.array(deg)), max(np.array(deg)), 1)
# calculate the output for the range
y_line = objective(x_line, x, y)
# create a line plot for the mapping function
plt.xlabel("Degree of scientists")
plt.ylabel("Number of scientists")
plt.plot(x_line, y_line, '--', color='red')
plt.savefig('17MCPC02-02.png')
plt.show()
