import board as lib

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

    game = lib.board(size=size)
    game.visited = [game.queens]
    frontier = []
    frontier.append(game)
    if option == 1:
        print(lib.bf_s(frontier))
    elif option == 2:
        print(lib.df_s(frontier))
    elif option == 3:
        limit = int(input(" Enter limit: "))
        print(lib.dl_s(frontier, limit))
    elif option == 4:
        print(lib.idl_s(frontier, 2))
    elif option == 5:
        print(lib.g_s(frontier))
    print("\nExecution ended...\n")

if __name__ == "__main__":
    main()