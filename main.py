from connector import ConnectGame

if __name__ == "__main__":
    game = ConnectGame()

    print(game)
    is_finished = False

    while not is_finished:
        column_index = int(input("Enter column index:"))
        is_finished = not game.do_action(column_index)
        print(game)
        print("*****CONNECT4*****")
        print()




