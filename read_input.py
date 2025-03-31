from typing import Optional


def read_maze_from_file(file_path: str) -> Optional[tuple[list[list[str]], tuple[int, int], tuple[int, int]]]:
    maze: list[list[str]] = []
    start: tuple[int, int]
    goal: tuple[int, int]
    try:
        with open(file_path, 'r') as file:
            first_line_len: int = 0
            for line in file:
                first_line_len = len(line)
                if line[-1] == '\n':
                    line = line[:-1]
                    if len(line) != first_line_len - 1:
                        print("Error: Maze is not rectangular")
                        return None

                row = list(line)
                maze.append(row)

    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    print(maze)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'G':  # start point
                start = (i, j)
            elif maze[i][j] == 'P':  # goal point
                goal = (i, j)

    # print_maze(maze)
    # print(f"Start: {start}")
    # print(f"Goal: {goal}")
    return maze, start, goal


def print_maze(maze):
    for row in maze:
        print(''.join(row))

if __name__ == "__main__":
    maze, start, goal = read_maze_from_file("input.txt")
    print_maze(maze)