from aifc import Error
from re import L

# moves value to the right
# use on pointer value
# triggers for the ">" token
def move_right(cell_pointer, cells_size):
    if cell_pointer < cells_size:  
        cell_pointer += 1
    else:
        raise Exception("Pointer size cannot go above " + cells_size)

# moves value to the left
# use on pointer value
# triggers for the "<" token
def move_left():
    if cell_pointer > 0:
        cell_pointer -= 1
    else:
        raise Exception("Pointer size cannot go below 0")




# takes a char as input for the current cell for unix
def take_char_unix():
    import tty, sys, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# takes a char as input for the current cell for unix
def take_char_windows():
    import msvcrt
    return msvcrt.getch()

# take char universal safe call trigger with the ',' token
def take_char():
    try:
        return take_char_unix()
    except ImportError:
        return take_char_windows()
    


# recursive function returns cell_pointer back to the last '[' token
def loop_back(cell_pointer, cells):
    cell_pointer -= 1
    if cells[cell_pointer] != '[':
        loop_back(cell_pointer, cells)
    else:
        return cell_pointer

def jump_to_close(cell_pointer, cells):
    cell_pointer += 1
    if cells[cell_pointer] != ']':
        jump_to_close(cell_pointer, cells)
    else:
        return cell_pointer

def main(instructions):

    # pointer to the current instruction in instructions array
    instruction_pointer = 0

    # pointer to the current cell
    # whenever the pointer changes the current_cell variable needs updated
    cell_pointer = 0

    # holds the current instruction
    current_instruction = 0 # place holder value

    # reading and writing to cells only when necessary
    # updated with the read_current_cell() function
    # push to the current_cell with push_current_cell() function
    current_cell = 0 # place holder value

    # limits the size of the cells array
    cells_size = 1000

    # the value that each cell starts with
    # should be 0
    cells_initial_val = 0

    # the array of cells
    cells = []

    # populate cells
    for x in range(0, cells_size):
        cells.append(cells_initial_val)

    while instruction_pointer < len(instructions):
        current_instruction = instructions[instruction_pointer]
        if current_instruction == '>': 
            cells[cell_pointer] = current_cell
            if cell_pointer < cells_size:  
                cell_pointer += 1
                current_cell = cells[cell_pointer]
            else:
                raise Exception("Pointer size cannot go above " + cells_size)
        elif current_instruction == '<': 
            cells[cell_pointer] = current_cell
            if cell_pointer > 0:
                cell_pointer -= 1
                current_cell = cells[cell_pointer]
            else:
                raise Exception("Pointer size cannot go below 0")
        elif current_instruction == '+':
            current_cell += 1
        elif current_instruction == '-':
            current_cell -= 1
        elif current_instruction == '.':
            print(current_cell)
        elif current_instruction == ',':
            current_cell = take_char()
        elif current_instruction == '[':
            if current_cell == 0:
                cell_pointer = jump_to_close(cell_pointer, cells)
        elif current_instruction == ']':
            if current_cell == 0:
                cell_pointer = loop_back(cell_pointer, cells)
        else: 
            raise Exception
        instruction_pointer += 1


