import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import threading

# Simulated Node Details
NODES = [
    {"name": "Client", "ip": "127.0.0.1:8000"},
    {"name": "Entry Node", "ip": "127.0.0.1:8001"},
    {"name": "Relay Node", "ip": "127.0.0.1:9001"},
    {"name": "Exit Node", "ip": "127.0.0.1:10001"},
]

# Create the Network Graph
def create_graph():
    G = nx.DiGraph()
    for i in range(len(NODES) - 1):
        G.add_edge(NODES[i]["name"], NODES[i + 1]["name"])
    return G

# Highlight the Edge in the Graph
def highlight_edge(graph_canvas, fig, ax, start_idx, end_idx):
    G = create_graph()
    pos = nx.spring_layout(G)  # Positions for nodes in the graph

    # Clear the figure and redraw the graph
    ax.clear()
    nx.draw(
        G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10, ax=ax
    )

    # Highlight the current edge
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=[(NODES[start_idx]["name"], NODES[end_idx]["name"])],
        edge_color="red",
        width=2,
        ax=ax,
    )

    ax.set_title("Onion Router Path Visualization", fontsize=16)
    graph_canvas.draw()

# Simulate Routing Path
def simulate_routing(graph_canvas, fig, ax, status_label):
    status_label.config(text="Routing in progress...")
    for i in range(len(NODES) - 1):
        time.sleep(1)  # Simulate delay between nodes
        highlight_edge(graph_canvas, fig, ax, i, i + 1)
        status_label.config(text=f"Message forwarded to {NODES[i + 1]['name']} ({NODES[i + 1]['ip']})")
    status_label.config(text="Routing Complete!")

# Start Routing in a Separate Thread
def start_routing_thread(graph_canvas, fig, ax, status_label):
    # Start the simulation in a separate thread
    thread = threading.Thread(target=simulate_routing, args=(graph_canvas, fig, ax, status_label))
    thread.daemon = True  # Ensure the thread closes with the main program
    thread.start()

# Main GUI Application
def main():
    root = tk.Tk()
    root.title("Onion Router Visualization")
    root.geometry("800x600")

    # Title Label
    title_label = ttk.Label(root, text="Onion Router Path Visualization", font=("Helvetica", 18, "bold"))
    title_label.pack(pady=10)

    # Status Label
    status_label = ttk.Label(root, text="Waiting to start...", font=("Helvetica", 12))
    status_label.pack(pady=5)

    # Graph Canvas
    graph_canvas_frame = ttk.Frame(root)
    graph_canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Create the Matplotlib figure and axes
    fig, ax = plt.subplots(figsize=(6, 4))
    graph_canvas = FigureCanvasTkAgg(fig, master=graph_canvas_frame)
    graph_canvas.draw()
    graph_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Start Button
    start_button = ttk.Button(
        root,
        text="Start Routing",
        command=lambda: start_routing_thread(graph_canvas, fig, ax, status_label),
    )
    start_button.pack(pady=10)

    # Quit Button
    quit_button = ttk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
