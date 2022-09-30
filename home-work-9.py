CONTACTS = {}


def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            handler(*args, **kwargs)
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("Give me name and phone please")

    return wrapper
@input_error
def main():
    while True:
        user_input = input("Enter command: ")

        if user_input not in COMMANDS:
            print("Wrong command, try again.")
            continue
        COMMANDS[user_input]()


@input_error
def hello_func():
    print("How can I help you?")

@input_error
def quit_func():
    print("Good bye!")
    quit()

@input_error
def add_contact():
    contact = input("Enter your name and phone: ")
    split_contct = contact.split()
    name = split_contct[0]
    phone = split_contct[1]
    CONTACTS.update({name: phone})
    print(CONTACTS)
    print("New contact added.")

@input_error
def chandler():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    CONTACTS[name] = phone
    print("Contact changed.")

@input_error
def get_phone():
    name = input("Enter name: ")
    phone = CONTACTS.get(name)
    print(phone)

@input_error
def find_contact():
    name = input("Enter name: ")
    print(name, CONTACTS[name])

@input_error
def show_all():
    for contact in CONTACTS:
        print(contact)

COMMANDS = {
    "good bye": quit_func,
    "close": quit_func,
    "exit": quit_func,
    "add": add_contact,
    "hello": hello_func,
    "find": find_contact,
    "change": chandler,
    "phone": get_phone,
    "show all": show_all
}


if __name__ == "__main__":
    main()