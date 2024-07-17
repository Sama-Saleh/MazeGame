import tkinter as tk

# Define the maze as a list of lists
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Define the window size and square size
WINDOW_SIZE = 400
SQUARE_SIZE = WINDOW_SIZE // len(maze)

# Define the player's starting position
player_pos = (1, 1)

# Define the GUI
root = tk.Tk()
root.title("Maze Game")

# Define the function to draw the maze
def draw_maze():
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            x1 = j * SQUARE_SIZE
            y1 = i * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            if maze[i][j] == 1:
                # wall
                rectangle = tk.Label(root, bg='grey', width=SQUARE_SIZE, height=SQUARE_SIZE)
                rectangle.place(x=x1, y=y1)
            elif (i, j) == player_pos:
                # player
                oval = tk.Label(root, bg='purple', width=SQUARE_SIZE, height=SQUARE_SIZE, borderwidth=0)
                oval.place(x=x1, y=y1)
            else:
                # path
                rectangle = tk.Label(root, bg='white', width=SQUARE_SIZE, height=SQUARE_SIZE, borderwidth=0)
                rectangle.place(x=x1, y=y1)

# Define the function to move the player
def move_player(event):
    global player_pos
    new_pos = None
    if event.keysym == 'Up':
        new_pos = (player_pos[0]-1, player_pos[1])
    elif event.keysym == 'Down':
        new_pos = (player_pos[0]+1, player_pos[1])
    elif event.keysym == 'Left':
        new_pos = (player_pos[0], player_pos[1]-1)
    elif event.keysym == 'Right':
        new_pos = (player_pos[0], player_pos[1]+1)
    if new_pos and maze[new_pos[0]][new_pos[1]] == 0:
        player_pos = new_pos
    if player_pos== (len(maze)-2,len(maze[0])-2):
        win_label=tk.Label(root, text='You Win!',font=('Arial',24),fg='purple')
        win_label.place(x=WINDOW_SIZE//2,y=WINDOW_SIZE//3, anchor='center')
        win_labe2=tk.Label(root, text='press any arrow to play again',font=('Arial',24),fg='black')
        win_labe2.place(x=WINDOW_SIZE//2,y=WINDOW_SIZE//2, anchor='center')
        player_pos = (1, 1) 
    else:
        draw_maze()

# Call the draw_maze() function to initialize the maze
draw_maze()

# Bind the arrow keys to move the player
root.bind('<Up>', move_player)
root.bind('<Down>', move_player)
root.bind('<Left>', move_player)
root.bind('<Right>', move_player)

# Start the GUI loop
root.mainloop()
