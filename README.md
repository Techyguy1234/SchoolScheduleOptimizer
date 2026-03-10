# School Schedule Optimizer

A Python tool that minimizes hallway congestion in a school by optimally rearranging student class schedules. It models the campus as a graph, simulates student traffic during class transitions, and uses a local search algorithm to find schedule arrangements that distribute hallway usage more evenly.

## Features

- **CSV schedule parsing** – Reads student schedules from a CSV file
- **Graph-based pathfinding** – Models the campus hallway layout using NetworkX and routes students via Dijkstra's algorithm
- **Congestion evaluation** – Simulates all student transitions between consecutive periods and measures traffic on each hallway segment
- **Schedule optimization** – Applies a local search heuristic (random period swaps with escape logic) to minimize overall congestion
- **ASCII heatmap visualization** – Displays per-period hallway usage with color-coded congestion levels
- **Optimized schedule output** – Saves the best schedule found back to CSV

## Requirements

- Python 3.x
- [NetworkX](https://networkx.org/)

Install the dependency with:

```bash
pip install networkx
```

No other external packages are required.

## Input Data

The optimizer reads student schedules from:

```
Student_Schedules - Student_Schedules.csv
```

Each row represents one class for one student, with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `Grade` | Student grade level | `11` |
| `Course Name` | Name of the class | `ENGLISH 11` |
| `Period` | Class period (1–10) | `2` |
| `Teacher` | Instructor name | `S. Emert` |
| `Location` | Room or location code | `122`, `GYM`, `CAFE` |
| `Term` | Duration of the class | `ALYR`, `SEM1`, `SEM2` |

**Term values:**
- `ALYR` – All year
- `SEM1` – First semester only
- `SEM2` – Second semester only

## Usage

### Run the optimizer

Runs an infinite optimization loop, continuously trying to improve the schedule. Prints progress whenever a lower-congestion arrangement is found and saves the result to `optimized_schedule.csv`.

```bash
python optimizer.py
```

### Evaluate the current schedule

Prints congestion scores for each period and the overall average, then displays ASCII heatmaps of hallway usage.

```bash
python main.py
```

## Output

- **Console** – Congestion averages per period and overall score; ASCII campus map with color-coded hallway segments:
  - 🟢 **Green** – Fewer than 20 students (low congestion)
  - 🟡 **Yellow** – 20–50 students (moderate congestion)
  - 🔴 **Red** – More than 50 students (high congestion)
- **`optimized_schedule.csv`** – The best schedule found, in the same format as the input CSV

## How It Works

1. **Parse** – `csvparser.py` reads the CSV and builds a course list and per-student schedule arrays.
2. **Model** – `NetworkPathfinding.py` constructs a weighted graph of hallway intersections (`H0`–`H11`) and room nodes. Edge weights reflect walking time (e.g., 10 for most hallways, 25 for slower library access).
3. **Evaluate** – For each period transition, `main.py` calculates the shortest path between each student's consecutive classes and tallies how many students traverse each hallway segment.
4. **Optimize** – `optimizer.py` repeatedly:
   - Picks a random student and two periods where the same class is offered
   - Swaps those periods and evaluates the new congestion score
   - Keeps the swap if it improves the score
   - After 300 consecutive failed attempts, performs a multi-student random escape swap to avoid local minima
5. **Visualize** – `gLib.py` renders an ASCII map of the campus overlaid with per-segment student counts.
6. **Save** – `save.py` writes the current best schedule to `optimized_schedule.csv`.

## Project Structure

```
SchoolScheduleOptimizer/
├── main.py                          # Entry point and congestion evaluation
├── optimizer.py                     # Optimization loop (run this to optimize)
├── csvparser.py                     # CSV data loading and parsing
├── NetworkPathfinding.py            # Graph-based hallway routing
├── gLib.py                          # ASCII heatmap visualization
├── save.py                          # CSV output utility
├── visualizer.py                    # Visualization stub (future use)
├── Student_Schedules - Student_Schedules.csv   # Input schedule data
└── optimized_schedule.csv           # Output: best schedule found
```

## Notes

- The optimizer runs **indefinitely** – press `Ctrl+C` to stop it once you are satisfied with the result.
- Optimization currently targets **Semester 2** classes. Adjust the `notSemester` parameter in `optimizer.py` to target Semester 1 instead.
- Period 10 (typically lunch/activity) is excluded from period swaps.
- The algorithm is a heuristic local search and is **not** guaranteed to find the global optimum.
