# ROS2 Dynamic Parameter System

A professional ROS2 parameter management project demonstrating dynamic parameter handling, YAML-based configuration, runtime parameter updates, and modular ROS2 Python node architecture using `rclpy`.

---

# Overview

This project demonstrates how to build a configurable ROS2 parameter system using:

- ROS2 Parameters
- YAML configuration files
- Dynamic runtime parameter updates
- ROS2 Python nodes (`rclpy`)
- Parameter declaration and retrieval
- Parameter monitoring and modification
- Modular ROS2 workspace organization

The project follows an industry-style ROS2 architecture by separating:

- Configuration files
- Application nodes
- Launch structure

This design improves scalability, maintainability, flexibility, and real-world robotics configuration management.

---

# Project Architecture

```bash
ros2-dynamic-parameter-system/
└── src/
    └── my_parameter_pkg/
        ├── my_parameter_pkg/
        │   ├── __init__.py
        │   └── parameter_node.py
        │
        ├── config/
        │   └── params.yaml
        │
        ├── launch/
        │   └── parameter_launch.py
        │
        ├── package.xml
        ├── setup.py
        └── setup.cfg
````

---

# System Workflow

## Parameter Communication Flow

```text
YAML Configuration File
            │
            ▼
Launch File Loads Parameters
            │
            ▼
ROS2 Node Declares Parameters
            │
            ▼
Parameters Used During Runtime
            │
            ▼
Dynamic Parameter Updates Applied
```

---

# Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| ROS2         | Robotics middleware framework       |
| Python       | ROS2 node implementation            |
| rclpy        | ROS2 Python client library          |
| YAML         | Parameter configuration             |
| colcon       | ROS2 build system                   |
| Git & GitHub | Version control and project hosting |

---

# ROS2 Concepts Demonstrated

This project covers several important ROS2 concepts:

* ROS2 workspaces
* ROS2 package creation
* ROS2 parameters
* Dynamic parameter updates
* YAML configuration files
* Launch files
* ROS2 parameter CLI tools
* Parameter declaration
* Parameter retrieval
* Runtime parameter modification
* Modular ROS2 architecture

---

# YAML Configuration File

File:

```bash
config/params.yaml
```

Example parameter configuration:

```yaml
parameter_node:
  ros__parameters:
    robot_name: "TurtleBot"
    linear_speed: 1.5
    use_sim_time: true
```

---

# Parameter Node

The ROS2 node:

* Declares parameters
* Reads parameters from YAML
* Displays parameter values
* Supports runtime parameter modification
* Handles configurable system behavior

---

# Parameter Responsibilities

* Load configuration values
* Maintain parameter state
* Allow dynamic updates
* Improve runtime flexibility
* Enable reusable configurations

---

# Build Instructions

## Clone Repository

```bash
git clone https://github.com/omkar-robotics/ros2-dynamic-parameter-system.git
```

---


```
## Build Workspace
colcon build
```

---

## Source Workspace

```bash
source install/setup.bash
```

---

# Running the Project

## Run publisher Node

Open terminal:

```bash
source install/setup.bash
ros2 run my_pub_py my_publisher
```

Expected output:

```text
Robot Name: TurtleBot
Linear Speed: 1.5
Use Sim Time: True
```
# Dynamic Parameter Example

This project supports runtime parameter modification without restarting the node.

Example:

```bash
ros2 run my_pub_pkg my_publisher --ros-args -p number:=10 -p publish_period:=0.5```

Updated output:

```text
Robot Name: ROS2_Bot
```

---

# ROS2 Command-Line Verification

## Verify Packages

```bash
ros2 pkg list | grep my_parameter_pkg
```

---

## List Parameters

```bash
ros2 param list
```

---

## Get Parameter Value

```bash
ros2 param get /parameter_node robot_name
```

---

---

# Dynamic Parameter Example

This project supports runtime parameter modification without restarting the node.

Example:

ros2 run my_pub_pkg my_publisher --ros-args -p number:=10 -p publish_period:=0.5```

Updated output:


```

---

# Key Learning Outcomes

By completing this project, the following ROS2 concepts were implemented and understood:

* ROS2 parameter system
* YAML configuration management
* Dynamic runtime configuration
* ROS2 launch system
* ROS2 package structure
* Python ROS2 nodes
* Parameter CLI tools
* Workspace build workflow
* GitHub project deployment

---

# Professional ROS2 Design Principle

This project follows ROS2 best practices by separating:

| Component   | Responsibility        |
| ----------- | --------------------- |
| YAML Config | Parameter storage     |
| Launch File | Runtime configuration |
| ROS2 Node   | Application logic     |

This architecture is commonly used in:

* Industrial robots
* Autonomous mobile robots
* Navigation systems
* Sensor configuration systems
* Multi-node robotics systems
* Simulation environments

---

# Future Improvements

Possible future enhancements:

* Add parameter callback validation
* Add dynamic reconfiguration GUI
* Add multiple parameter profiles
* Add lifecycle nodes
* Add ROS2 Actions integration
* Add sensor parameter management
* Add robot motion tuning
* Add logging system
* Add launch argument support

---

# Author

## Omkar Honrao

Electrical Engineering Student | ROS2 & Robotics Enthusiast

### Areas of Interest

* Robotics
* ROS2
* Autonomous Systems
* Artificial Intelligence
* Machine Learning
* Industrial Automation
* Embedded Systems

---


