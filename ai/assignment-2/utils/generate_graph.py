"""Please note: AI was used to generated code in this file"""
import matplotlib.pyplot as plt
import networkx as nx


def generate_graph_image_with_highlights(edges, highlight_edges, output_filename='graph.png'):
    # Create a directed graph
    G = nx.DiGraph()

    # Add edges to the graph
    for src, dest, weight in edges:
        G.add_edge(src, dest, weight=weight)

    # Define the layout for the graph with more space
    pos = nx.spring_layout(G, k=2.5, iterations=50)  # Adjust 'k' for more spacing

    # Draw the nodes with larger sizes and colors
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2000)

    # Draw all edges with a lighter color
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), alpha=0.3)

    # Highlight the specified edges with thicker width and bold color
    nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, width=2, edge_color='red')

    # Draw labels for nodes
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

    # Set limits and title
    plt.axis('off')  # Turn off the axis
    plt.title("Graph Visualization with Highlighted Edges", fontsize=14)

    # Save the graph image
    plt.savefig(output_filename, bbox_inches='tight')
    plt.close()
