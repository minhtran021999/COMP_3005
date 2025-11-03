import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
import seaborn as sns

# Set up the plotting style
plt.style.use('default')
fig_size = (12, 8)

# Function to plot a directed graph with labels and degrees
def plot_directed_graph(G, title, pos=None, node_colors=None, edge_colors=None, ax=None):
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=fig_size)
    
    if pos is None:
        pos = nx.spring_layout(G, k=3, iterations=50)  # Layout for better spacing
    
    # Draw nodes
    if node_colors is None:
        node_colors = ['lightblue'] * len(G.nodes)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000, ax=ax)
    
    # Draw edges
    if edge_colors is None:
        edge_colors = ['gray'] * len(G.edges)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, arrows=True, arrowsize=20, ax=ax)
    
    # Labels
    nx.draw_networkx_labels(G, pos, font_size=12, ax=ax)
    
    # Degrees as badges (text)
    for node in G.nodes:
        in_deg = G.in_degree(node)
        out_deg = G.out_degree(node)
        ax.text(pos[node][0], pos[node][1] + 0.1, f'In:{in_deg}/Out:{out_deg}', 
                ha='center', va='center', fontsize=8, bbox=dict(boxstyle="round,pad=0.3", facecolor='white'))
    
    ax.set_title(title)
    ax.axis('off')
    plt.tight_layout()
    return fig, ax

# Function to plot adjacency matrix as heatmap
def plot_adjacency_matrix(A, title, labels=None, ax=None):
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    
    # Create heatmap
    cmap = ListedColormap(['white', 'red'])
    sns.heatmap(A, annot=True, fmt='d', cmap=cmap, cbar=True, ax=ax,
                xticklabels=labels, yticklabels=labels)
    ax.set_title(title)
    plt.tight_layout()
    return fig, ax

# Example 1: Minimal 2-Node Graph (Mutual Linking)
print("Generating Example 1: 2-Node Mutual Graph")
G1 = nx.DiGraph()
G1.add_nodes_from(['A', 'B'])
G1.add_edge('A', 'B')
G1.add_edge('B', 'A')

fig1, ax1 = plt.subplots(1, 2, figsize=(15, 6))
plot_directed_graph(G1, "2-Node Mutual Linking Graph", ax=ax1[0])

# Adjacency Matrix
A1 = nx.to_numpy_array(G1)
labels1 = ['A', 'B']
plot_adjacency_matrix(A1, "Adjacency Matrix", labels1, ax=ax1[1])

plt.savefig('example1.png')
plt.show()  # In REPL, this displays; save for files
plt.close()

# Example 2: 4-Node Chain
print("Generating Example 2: 4-Node Chain")
G2 = nx.DiGraph()
G2.add_nodes_from(['A', 'B', 'C', 'D'])
G2.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'A')])  # Chain + back-link

node_colors2 = ['red', 'orange', 'yellow', 'purple']
edge_colors2 = ['gray', 'gray', 'gray', 'blue']  # Back-link different

fig2, ax2 = plt.subplots(1, 2, figsize=(15, 6))
plot_directed_graph(G2, "4-Node Chain Graph", node_colors=node_colors2, edge_colors=edge_colors2, ax=ax2[0])

# Adjacency Matrix
A2 = nx.to_numpy_array(G2)
labels2 = ['A', 'B', 'C', 'D']
plot_adjacency_matrix(A2, "Adjacency Matrix", labels2, ax=ax2[1])

plt.savefig('example2.png')
plt.show()
plt.close()

# Example 3: 6-Node Hub-and-Spoke
print("Generating Example 3: 6-Node Hub-and-Spoke")
G3 = nx.DiGraph()
G3.add_nodes_from(['H', 'S1', 'S2', 'S3', 'S4', 'S5'])
# Hub incoming from spokes
G3.add_edges_from([('S1', 'H'), ('S2', 'H'), ('S3', 'H'), ('S4', 'H'), ('S5', 'H')])
# Hub out to one spoke
G3.add_edge('H', 'S3')
# Cross-links
G3.add_edge('S1', 'S2')
G3.add_edge('S4', 'S5')

node_colors3 = ['gold'] + ['lightgray'] * 5
edge_colors3 = ['green'] * 5 + ['blue'] + ['purple'] * 2

fig3, ax3 = plt.subplots(1, 1, figsize=(10, 8))  # Single plot for larger graph
plot_directed_graph(G3, "6-Node Hub-and-Spoke Graph", node_colors=node_colors3, edge_colors=edge_colors3, ax=ax3)

# For matrix, show as sparse summary instead of full 6x6 for brevity
A3 = nx.to_numpy_array(G3)
print("Adjacency Matrix for Example 3 (sparse summary):")
print(A3)
# To plot full: plot_adjacency_matrix(A3, "Adjacency Matrix (6x6)", ['H','S1','S2','S3','S4','S5'])

plt.savefig('example3.png')
plt.show()
plt.close()

# Optional: Degree Table
print("\nDegree Summary Across Examples:")
for i, G in enumerate([G1, G2, G3], 1):
    print(f"Example {i}:")
    for node in sorted(G.nodes):
        print(f"  {node}: In-degree={G.in_degree(node)}, Out-degree={G.out_degree(node)}")