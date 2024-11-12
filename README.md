# Conway's Game of Life

### Project Overview
This project is a Python implementation of **Conway's Game of Life**, a zero-player game that simulates cellular automata based on simple rules. The game demonstrates how complex patterns and behaviors can emerge from simple initial states and rules, making it a classic example in computational science.

### Rules of the Game
Conway's Game of Life operates on a grid of cells, where each cell has two possible states: alive or dead. The state of each cell evolves based on its neighbors according to the following rules:
1. **Underpopulation**: A live cell with fewer than two live neighbors dies.
2. **Overpopulation**: A live cell with more than three live neighbors dies.
3. **Reproduction**: A dead cell with exactly three live neighbors becomes alive.
4. **Stasis**: A live cell with two or three neighbors continues to live to the next generation.

### Key Features
- **Dynamic Grid**: The grid updates in real-time, showing how cells evolve based on their neighbors.
- **User Interaction**: Users can interact with the grid to set initial cell states, creating different patterns and observing their evolution.
- **Patterns and Structures**: The implementation allows for the creation of well-known Game of Life patterns like gliders, oscillators, and still lifes.

### Technologies Used
- **Python**: Core programming language used.
- **Pygame**: Library used for creating the grid, handling user input, and displaying animations.

### Installation
To run the Game of Life on your local machine, follow these steps:
