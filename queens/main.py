from board import board, dls    

def main():
    
    game = board(size=5)
    frontier = []
    frontier.append(game)
    print(dls(frontier, 100))
    

if __name__ == "__main__":
    main()