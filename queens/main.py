import board as lib

def print_board(board:lib.board) -> None:
    print_hline("┌", "───┬", "┐", board.size)
    for j in range(board.size):
        for i in range(board.size):
            print("│ X ", end="") if board.queens[i] == j else print("│   ", end="")
        print("│")
        print_hline("├", "───┼", "┤", board.size) if j != board.size - 1 else print_hline("└", "───┴", "┘", board.size)
def print_hline(first:str, middle:str, last:str, size:int) -> str:
    line:str = first
    line += middle * size
    print(line[0:-1] + last)
    
def main() -> None:
    print("\n== N-QUEENS ==\n")

    flag = True
    while flag:
        try:
            size = int(input("Board size: "))
            flag = False
        except:
            flag = True
    print("\nAlgorithms:\n" +
            "  1.- Breadth-First Search\n" +
            "  2.- Depth-First Search\n" +
            "  3.- Depth-Limited Search\n" +
            "  4.- Iterated Depth-Limited Search\n" +
            "  5.- Greedy Search\n" +
            "  0.- Exit")
    flag = True
    while flag:
        try:
            option = int(input("Select algorithm: "))
            if option > -1 and option < 6:
                flag = False
        except:
            flag = True
    print()

    visited:list[list[int]] = []
    game = lib.board(visited=visited, size=size)
    frontier:list[lib.board] = []
    frontier.append(game)
    if option == 1:
        message, goal = lib.bf_s(frontier)
    elif option == 2:
        message, goal = lib.df_s(frontier)
    elif option == 3:
        flag = True
        while flag:
            try:
                limit = int(input(" Enter limit: "))
                if limit > -1:
                    flag = False
            except:
                flag = True
        message, goal = lib.dl_s(frontier, limit)
    elif option == 4:
        flag = True
        while flag:
            try:
                increment = int(input(" Enter increment: "))
                if increment > -1:
                    flag = False
            except:
                flag = True
        message, goal = lib.idl_s(game, 2, increment)
    elif option == 5:
        message, goal = lib.g_s(frontier)

    print(message)
    if goal != None: print_board(goal) 

    print("\nExecution ended...\n")

if __name__ == "__main__":
    main()