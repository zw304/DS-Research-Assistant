import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

### collect user id history of tweet and retweet: 1372924225162407943
data1 = pd.read_csv("data1.csv")
data2 = pd.read_csv("data2.csv")
data3 = pd.read_csv("data3.csv")

all_data = pd.concat([data1,data2,data3])
## all_data ## 29765

G = nx.from_pandas_edgelist(all_data, 'user_id', 'retweeted_user_id',create_using=nx.Graph())
G.nodes()
nx.draw(G, with_labels = False)
nt = Network('500px', '500px')
nt.from_nx(G)
nt.show('nx.html') 

