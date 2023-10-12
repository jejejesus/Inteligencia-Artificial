from board import board, dls

def iterated_dls():
    limit = 2

    for i in range(20):
        game = board(size=4, queens=[0, 0, 0, 0])
        frontier = []
        frontier.append(game)
        print(dls(frontier, limit=limit))
        game.visited = []

def main():
    game = board(size=4, queens=[0, 0, 0, 0])
    frontier = []
    frontier.append(game)

    print(dls(frontier, 100))

if __name__ == "__main__":
    main()