from board import board, dls

def main():
    game = board(size=4, queens=[1, 3, 0, 1])
    frontier = []
    frontier.append(game)

    print(dls(frontier, 100))

if __name__ == "__main__":
    main()