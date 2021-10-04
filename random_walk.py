# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:22:42 2020

@author: krish
"""

import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

G=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)
plt.show()
#x id the random source node
x=random.choice([i for i in range(G.number_of_nodes())])
dict_counter={}
for i in range(G.number_of_nodes()):
    dict_counter[i]=0
dict_counter[x]=dict_counter[x]+1
for i in range(1000000):
    list_n=list(G.neighbors(x))
    if(len(list_n)==0):#if x is a sink
        x=random.choice([i for i in range(G.number_of_nodes())])
        dict_counter[x]=dict_counter[x]+1
    else:
        x=random.choice(list_n)#choose a node randomly from list of neighbors of x
        dict_counter[x]=dict_counter[x]+1

p=nx.pagerank(G)
sorted_p=sorted(p.items(),key=operator.itemgetter(1))
sorted_rw=sorted(dict_counter.items(),key=operator.itemgetter(1))
print(sorted_p)
print(sorted_rw)