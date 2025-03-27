from typing import Optional, List, Tuple

def read_maze_from_file(file_path: str) -> Optional[Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]]:

    maze : List[List[str]] = []
    start: Tuple[int, int] = None
    goal: Tuple[int, int] = None
    try:
        with open(file_path, 'r') as file:
            first_line_len: int = 0
            for line in file:
                first_line_len = len(line)
                if(line[-1] == '\n'):
                    line = line[:-1]
                    if len(line) != first_line_len - 1:
                        print("Error: Maze is not rectangular")
                        return None

                row = list(line)
                maze.append(row)

    except Exception as e:
        print(f"Error reading file: {e}")
        return None
        
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S': # start point
                start = (i, j)
            elif maze[i][j] == 'G': # goal point
                goal = (i, j)

    print_maze(maze)
    print(f"Start: {start}")
    print(f"Goal: {goal}")
    return (maze, start, goal)

def print_maze(maze):
    for row in maze:
        print(''.join(row))