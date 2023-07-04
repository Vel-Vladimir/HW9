GOODBYE = ('good bye', 'close', 'exit')

def launch_bot():

    while True:
        user_command = input()
        if user_command.lower() in GOODBYE:
            print("Good bye!")
            break




def main():
    launch_bot()


if __name__ == '__main__':
    main()
