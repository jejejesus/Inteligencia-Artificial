from board import board, gs

def main():
    game = board(size=4)
    frontier = []
    frontier.append(game)
    print(gs(frontier))

if __name__ == "__main__":
    main()