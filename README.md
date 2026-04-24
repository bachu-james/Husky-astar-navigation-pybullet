#  Husky A* Autonomous Navigation in PyBullet

> Interactive autonomous navigation system for a **Clearpath Husky** mobile robot using **PyBullet** physics simulation, **A\*** path planning, and a **closed-loop motion controller** — built without ROS.

---

##  Demo Video
![alt text](HuskyBot.gif)



### Workflow

```
Launch app → GUI opens → Click Start → Click Goal
→ A* plans path → PyBullet opens → Husky navigates → Robot stops at goal
```

1. Launch `main.py`
2. GUI window opens showing a 2D grid map
3. Click to set **Start** position (green)
4. Click to set **Goal** position (red)
5. A\* planner computes a collision-free path
6. PyBullet simulation window opens
7. Husky robot follows the planned route autonomously
8. Robot stops when the goal is reached within tolerance

---

##  Features

- 🖱️ Interactive Start / Goal selection via GUI
- 🐾 Husky robot simulation in PyBullet
- 🧱 Static obstacle environment
- 🗺️ A\* path planning with occupancy grid
- 📍 Path visualization inside the simulator
- 🔁 Closed-loop autonomous navigation
- 🧭 Heading correction controller
- ⚙️ Linear and angular wheel velocity control
- 🏁 Goal reach tolerance stopping logic
- 🧩 Fully modular code structure

---

## Project Structure

```
husky_nav/
│── README.md
│── requirements.txt
│── .gitignore
│──main.py
└── src/
    ├── simulator/
    │   ├── world.py           # PyBullet environment setup
    │   └── robot.py           # Husky URDF loading
    ├── planner/
    │   ├── gridmap.py         # Occupancy grid representation
    │   └── astar.py           # A* path planning algorithm
    ├── controller/
    │   └── navigator.py       # Closed-loop motion controller
    └── gui/
        └── click_interface.py # OpenCV click-based map GUI
```

---

## System Design

The project is split into five independent modules for clean architecture and maintainability.

### `gui/click_interface.py` — User Interaction
- Displays a 2D grid selection window using OpenCV
- Captures mouse clicks for Start and Goal positions
- Converts pixel coordinates to world (simulation) coordinates

### `planner/gridmap.py` — Environment Mapping
- Creates an occupancy grid representation of the world
- Marks obstacle cells as blocked
- Provides the grid structure for A\* to search over

### `planner/astar.py` — Path Planning
- Computes the shortest collision-free path using A\* graph search
- Returns an ordered list of waypoints from Start to Goal

### `simulator/world.py` — Simulation Environment
- Initializes PyBullet physics engine
- Loads ground plane and static box obstacles
- Draws the planned path visually in the simulation
- Controls the simulation camera

### `simulator/robot.py` — Robot Loading
- Loads the Husky URDF into the simulation
- Sets the initial position and heading of the robot

### `controller/navigator.py` — Motion Control
- Reads the robot's current pose from PyBullet each step
- Computes heading error and drives wheel velocities
- Tracks waypoints sequentially and stops at the goal

---

##  Control Logic

The robot uses a **closed-loop waypoint tracking controller**.

### Step 1 — Localization Feedback
Each simulation step reads the robot's current state from PyBullet:
- X position
- Y position
- Yaw angle (heading)

### Step 2 — Target Waypoint
The controller selects the next waypoint from the A\* path list.

### Step 3 — Heading Error
```
desired_heading = atan2(goal_y - robot_y, goal_x - robot_x)
heading_error   = desired_heading - current_yaw
```

### Step 4 — Angular Velocity Control
If `|heading_error|` is large:
- Left and right wheels spin in **opposite directions**
- Robot turns in place toward the waypoint

### Step 5 — Linear Velocity Control
Once heading error is small:
- Robot drives **forward**
- Small angular correction continues to maintain alignment

### Step 6 — Waypoint Completion
When the robot is within the **distance threshold** of a waypoint:
- Current waypoint is marked complete
- Controller advances to the next waypoint

### Step 7 — Goal Stop Condition
When the **final waypoint** is reached:
- Wheel velocities are set to zero
- Robot stops and the navigation task ends

---

## 🚀 Run Instructions

### Prerequisites

- Python 3.8 or higher
- Windows / Linux / macOS

### Install Dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt`:
```
pybullet
numpy
opencv-python
```

### Run the Application

```bash
cd src
python main.py
```

### How to Use

1. A 2D grid window opens
2. **Left-click** anywhere on the grid to set the **Start** position (shown in green)
3. **Left-click** again to set the **Goal** position (shown in red)
4. Press **Enter** or **Space** to confirm
5. The PyBullet simulation launches automatically
6. Watch the Husky navigate to the goal

---

## ⚙️ Configuration

Key parameters can be adjusted at the top of each module:

| Parameter | Location | Default | Description |
|-----------|----------|---------|-------------|
| `GRID_SIZE` | `gridmap.py` | `50` | Grid resolution (cells) |
| `WORLD_SIZE` | `gridmap.py` | `10.0` | World size in meters |
| `GOAL_TOLERANCE` | `navigator.py` | `0.3` | Stop distance from goal (m) |
| `LINEAR_VEL` | `navigator.py` | `5.0` | Forward wheel velocity |
| `ANGULAR_VEL` | `navigator.py` | `3.0` | Turning wheel velocity |
| `HEADING_THRESHOLD` | `navigator.py` | `0.15` | Angle error to switch to forward drive (rad) |

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `pybullet` | Physics simulation engine |
| `numpy` | Array and math operations |
| `opencv-python` | GUI and path visualization |

---

## 📋 Constraints

### ❌ Not Used
- ROS / ROS2
- Prebuilt navigation stacks
- Any copy-paste tutorial implementations

### ✅ Custom Implementations
- A\* path planning from scratch
- Closed-loop motion controller
- Occupancy grid mapping
- Click-based GUI

---



## 📄 License

This project was built as part of a pre-interview assignment.  
For educational and evaluation purposes only.