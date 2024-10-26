# 🧭 Nautical Waypoint Relative Calcs

**Nautical Waypoint Relative Calcs** is a CLI tool designed to calculate essential nautical navigation metrics, including course, distance, and speed in knots. This tool takes in multiple waypoints with timestamps and outputs the relative course, distance in nautical miles, and speed between each pair of points.

## 🌊 Purpose

The purpose of this tool is to assist sailors, navigators, and enthusiasts in calculating navigation metrics between multiple waypoints, using standard nautical formats. By taking in waypoints and timestamps, it transforms relative positional data into actionable navigation insights. This can be particularly helpful for voyaging, navigation planning, and real-time route assessments.

## 🚀 Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/username/nautical-waypoint-relative-calcs.git
    cd nautical-waypoint-relative-calcs
    ```

2. **Run the Script**:
    The script `main.py` accepts a series of waypoints as command-line arguments, each in the format:
    
    ```
    YYYY-MM-DDTHH:MM@00°00'N,000°00'E
    ```
    
    Example command to calculate course, distance, and speed between positions:
    
    ```bash
    python main.py 2024-10-26T08:00@52°22'N,004°54'E 2024-10-26T12:00@51°30'N,000°07'W 2024-10-26T16:30@50°05'N,001°30'W
    ```
   
    Each position will be processed in sequence, providing outputs of course, distance, and speed between each waypoint.

## 👤 Author

Created by [Kevin Veen-Birkenbach](https://github.com/KevinVeen-Birkenbach). 

For more information about Kevin's Yachtmaster services, visit 🌐 [yachtmaster.world](https://yachtmaster.world/).  
For details about his IT solutions, check out 🌐 [cybermaster.space](https://cybermaster.space/).

This project was created with the assistance of AI. [Link to conversation](https://chat.openai.com/).

## 📜 License

This software is licensed under the **[GNU Affero General Public License, Version 3](./LICENSE)**. 

---

⚓️ Happy navigating!
