# bot assistant with error handling and contact management

def input_error(func): # decorator for error handling
    def inner(*args, **kwargs): # inner function to wrap the original function
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."

    return inner

 
def parse_input(user_input): # parse the input
    cmd, *args = user_input.split() # split the input into command and arguments
    cmd = cmd.strip().lower() # remove leading and trailing whitespace and convert to lowercase
    return cmd, args

@input_error
def add_contact(args, contacts): # add contact
    name, phone = args # get name and phone
    contacts[name] = phone # add to contacts dictionary
    return "Contact added."

@input_error
def change_contact(args, contacts): # change contact phone
    name, phone = args
    contacts[name]  # check if contact exists
    contacts[name] = phone # update phone number
    return "Contact updated."
 
@input_error    
def contact_phone(args, contacts):# get contact phone
    name, = args
    return contacts[name]


def all_contacts(contacts): # get all contacts
    if not contacts: # check if contacts dictionary is empty
       return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in sorted(contacts.items())) # return all sorted contacts



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip() # get user input
        if not user_input: # check for empty input
            print("Please enter a command.")
            continue

        command, args = parse_input(user_input) # parse the input

        if command in ["close", "exit"]: # exit commands
            print("Good bye!")
            break
        elif command == "hello": # hello command
            print("How can I help you?")
        elif command == "add": # add command
            print(add_contact(args, contacts))
        elif command == "change": # change command
            print(change_contact(args, contacts))
        elif command == "phone": # phone command
            print(contact_phone(args, contacts))
        elif command == "all": # all command
            print(all_contacts(contacts))
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

