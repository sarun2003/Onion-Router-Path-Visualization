# Onion Router Path Visualization

This project demonstrates a simplified version of an **Onion Router**, focusing on visualizing how messages are routed through intermediate nodes securely. The program provides a dynamic and interactive GUI to highlight the routing path from the **Client** to the **Exit Node**.

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

## Technologies Used
- **Python 3.x**
- **tkinter**: For GUI development.
- **matplotlib**: For visualizing the graph dynamically.
- **networkx**: For creating and managing the graph structure.
- **customtkinter**: For enhanced modern UI elements.

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
   cd /path/to/TOR
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
     ```bash
   source venv/bin/activate

### Step 2: Install Dependencies
Run the following command to install all required libraries:
```bash
pip install networkx matplotlib customtkinter

### Step 3: Generate Encryption Keys
Run the key generator script:
```bash
python3 utils/key_generator.py

### Step 4: Run the Nodes
1. Start the Exit Node:
     ```bash
     python3 nodes/exit_node.py
2. Start the Relay Node:
    ```bash
     python3 nodes/relay_node.py
3. Start the Entry Node:
     ```bash
     python3 nodes/entry_node.py

### Step 5: Run the GUI
Run the router visualization GUI:
```bash
python3 gui/router_gui.py

### Step 6: Interact with the Simulation
**In the GUI window:**
- Click "Start Routing" to begin the simulation.
- Watch the edges highlight dynamically, and observe the real-time status updates.

---

## Demo
