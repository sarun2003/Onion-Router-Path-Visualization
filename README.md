# Onion Router Path Visualization

This project simulates an Onion Router, a secure data routing system where messages are forwarded through multiple nodes (Client → Entry Node → Relay Node → Exit Node) to ensure privacy and anonymity. The GUI provides a dynamic visualization of the routing path.

## Features
1. **Dynamic Path Visualization**:
   - Simulates message forwarding through four nodes: Client → Entry Node → Relay Node → Exit Node.
   - Highlights each edge in **red** dynamically as the message progresses.

2. **Interactive GUI**:
   - A graphical interface built using `tkinter` and `matplotlib`.
   - Includes a "Start Routing" button to begin the simulation.

3. **Status Updates**:
   - Displays real-time updates on the routing progress:
     - "Message forwarded to Entry Node."
     - "Routing Complete!"

4. **Threading for Responsiveness**:
   - Ensures the GUI remains interactive while the simulation runs.

### Key Features
- **Dynamic Path Visualization**: Highlight edges in red as messages progress through the nodes.
- **Real-Time Updates**: Status messages display routing progress step-by-step.
- **Interactive GUI**: Built using `tkinter` and `matplotlib` for visualization.

## Technologies Used
- **Python 3.x**
- **tkinter**: For GUI development.
- **matplotlib**: For visualizing the graph dynamically.
- **networkx**: For creating and managing the graph structure.
- **customtkinter**: For enhanced modern UI elements.

### Prerequisites
- Python 3.8+ (Tested on Python 3.11)
- Virtual Environment (venv)

## File Structure
- **Onion/**
  - `client.py`
  - `key_exchange.py`
  - `onion_router.log`
  - `shared_key.key`
  - **nodes/**
    - `entry_node.py` 
    - `relay_node.py` 
    - `exit_node.py` 
  - **utils/**
    - `encryption_utils.py`
    - `key_generator.py`
    - `logger.py`
    - `config.py`
    - `__ini__.py`
    - `__pycache__`
  - **gui/**
    - `router_gui.py`
  - **venv/**

## How to Run the Project

### Step 1: Setup the Virtual Environment
1. Open your terminal.
2. Navigate to the project folder:
   ```bash
   cd /path/to/Onion
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

### Step 2: Install Dependencies
Run the following command to install all required libraries:
- pip install networkx matplotlib customtkinter

### Step 3: Generate Encryption Keys
Run the key generator script:
- python3 utils/key_generator.py

### Step 4: Run the Nodes
1. Start the Exit Node:
- python3 nodes/exit_node.py
2. Start the Relay Node:
- python3 nodes/relay_node.py
3. Start the Entry Node:
- python3 nodes/entry_node.py

### Step 5: Run the GUI
Run the router visualization GUI:
- python3 gui/router_gui.py

### Step 6: Interact with the Simulation
**In the GUI window:**
- Click "Start Routing" to begin the simulation.
- Watch the edges highlight dynamically, and observe the real-time status updates.

## Demo
- When it starts, it will give you a proper graph with nodes: Client, Entry Node, Relay Node, and Exit Node.
- The edges will turn red one-by-one to simulate routing.
- The status label at the top will show real-time updates.
- A clear visualization of how data/message is routed through intermediate nodes securely.
- A responsive GUI that highlights routing progress dynamically.

## Contributing
- Contributions are welcome! Feel free to open an issue or submit a pull request if you'd like to add features or improve the project.

## Area of use
1. Cybersecurity Education
2. Networking Concepts
3. Visualization of Routing Algorithms
4. Privacy and Anonymity Research
5. Simulation and Debugging of Network Systems
6. Research and Prototyping

## Contact
For any questions or suggestions, feel free to contact me:
- **Email**: sarunshrestha03@gmail.com
- **GitHub**: sarun2003

### Project by Sarun Shrestha 
