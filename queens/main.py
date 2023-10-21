import board as lib

def print_board(board:lib.board) -> None:
    print_hline("┌", "───┬", "┐", board.size)
    for i in range(board.size):
        for j in range(board.size):
            print("│ X ", end="") if board.queens[i] == j else print("│   ", end="")
        print("│")
        print_hline("├", "───┼", "┤", board.size) if i != board.size - 1 else print_hline("└", "───┴", "┘", board.size)
def print_hline(first:str, middle:str, last:str, size:int) -> str:
    line:str = first
    line += middle * size
    print(line[0:-1] + last)
    


def main():
    print("\n== N QUEENS ==\n")
    size = int(input("Board size: "))
    print("\nAlgorithms:\n" +
            "  1.- Breadth-First Search\n" +
            "  2.- Depth-First Search\n" +
            "  3.- Depth-Limited Search\n" +
            "  4.- Iterated Depth-Limited Search\n" +
            "  5.- Greedy Search\n" +
            "  0.- Exit")
    option = int(input("Select algorithm: "))
    print()

    visited:list[list[int]] = []
    game = lib.board(visited=visited, size=size)
    game.visited = [game.queens]
    frontier:list[lib.board] = []
    frontier.append(game)
    if option == 1:
        message, goal = lib.bf_s(frontier)
    elif option == 2:
        message, goal = lib.df_s(frontier)
    elif option == 3:
        limit = int(input(" Enter limit: "))
        message, goal = lib.dl_s(frontier, limit)
    elif option == 4:
        message, goal = lib.idl_s(game, 2)
    elif option == 5:
        message, goal = lib.g_s(frontier)

    print(message)
    if goal != None: print_board(goal) 

    print("\nExecution ended...\n")

if __name__ == "__main__":
    main()