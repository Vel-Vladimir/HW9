GOODBYE = ('good bye', 'close', 'exit')
contacts = {}

def input_error(func):
    def inner(command):
        try:
            return func(command)
        except KeyError:
            return "This name is absent in the contact list"
        except IndexError:
            if len(command) == 0:
                return "Enter command, please."
            return "Give me name and phone, please"
        except ValueError:
            pass
    return inner

def launch_bot():

    while True:
        user_command = input()
        parsed_command = parser(user_command)

        result = handler(parsed_command)
        if result is not None:

            if type(result) == dict:
                for k in result:
                    print(k, ": ", result[k], sep="")
            elif type(result) == str:
                print(result)
            if result == "Good bye!":
                quit()


def parser(string: str) -> list:
    res = string.split()
    return res


@input_error
def handler(command: list):
    """
    command[0] -> name of command
    command[1] -> name of person
    command[2] -> telephone number of person

    """

    command[0] = command[0].lower()

    if command[0] == "hello":
        return "How can I help you?"
    elif command[0] == "show":
        return contacts
    elif command[0] in GOODBYE:
        return "Good bye!"
    elif command[0] == "add":
        contacts[command[1]] = command[2]
    elif command[0] == "change":
        if command[1] not in contacts:
            return "You try to change a contact that is not in the contact list"
        contacts[command[1]] = command[2]
    elif command[0] == "phone":
        return contacts[command[1]]
    else:
        return "Unknown command.\nEnter a command, please (add, change, phone, show all)."


def main():
    launch_bot()


if __name__ == '__main__':
    main()
