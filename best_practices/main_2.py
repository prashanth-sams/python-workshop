print("am in main function")


def game(data):
    print(f"You're watching {data}")
    return data


def main():
    print("You're in game mode...")


if __name__ == '__main__':
    main()
    game('football')
