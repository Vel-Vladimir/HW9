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

    return inner

def launch_bot():

    while True:
        user_command = input()
        parsed_command = parser(user_command)
        result = handler(parsed_command)
        if result is not None:

            if type(result) == dict:
                if len(result) == 0:
                    print("List of contact is empty")
                    continue
                for k in result:
                    print(k, ": ", result[k], sep="")
            elif type(result) == str:
                print(result)
            if result == "Good bye!":
                quit()


def parser(string: str) -> list:
    res = string.split()
    return res

def hello() -> str:
    return "How can I help you?"

def goodbye() -> str:
    return "Good bye!"

def show_all() -> dict:
    return contacts

@input_error
def change(command: list):
    if command[1] not in contacts:
        return "You try to change a contact that is not in the contact list"
    contacts[command[1]] = command[2]

@input_error
def phone(command: list) -> str:
    return contacts[command[1]]

@input_error
def add(command: list) -> None:
    contacts[command[1]] = command[2]

@input_error
def handler(parsed_command: list):
    """
    command[0] -> name of command
    command[1] -> name of person
    command[2] -> telephone number of person

    """
    parsed_command[0] = parsed_command[0].lower()
    command = parsed_command[0]
    if command in GOODBYE:
        return HANDLERS[GOODBYE]()

    if command not in HANDLERS:
        return "Unknown command.\nEnter a command, please (add, change, phone, show all)."

    if command in ("hello", "show"):
        return HANDLERS[command]()

    return HANDLERS[command](parsed_command)

HANDLERS = {"hello": hello, "add": add, "change": change, "phone": phone, "show": show_all, GOODBYE: goodbye}

def main():
    launch_bot()

if __name__ == '__main__':
    main()
