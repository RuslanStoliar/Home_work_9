USERS = {}

def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again.'
        except ValueError as exception:
            return 'Bad imput! Give me name and phone please'
        except IndexError:
            return 'This contact cannot be added, it exists already'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
    return inner

@error_handler
def add_user(args):
    name, phone = args
    if name not in USERS:
        USERS[name] = phone
        return f"User {name} added"
    return f'{name} alredy in contact book'
    

@error_handler
def change_phone(args):
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f"User {name} have a new phone number, old was: {old_phone}"

@error_handler
def show_number(args):
    user = args[0]
    phone = USERS[user]
    return f"{user}: {phone}"

def show_all(_):
    result = ""
    for name, phone in USERS.items():
        result += f"{name} : {phone }\n" 
    return result

def hello(_):
    return "How can I help you?"

def exit(_):
    return "Good bye!"

HANDLERS = {
    "hello": hello,
    "good_bye": exit,
    "close": exit,
    "exit": exit,
    "add": add_user,
    "change": change_phone,
    "show_all": show_all,
    "phone": show_number,
}
@error_handler
def parser_input(user_input):
    cmd, *args = user_input.split()
    try:
        handler = HANDLERS[cmd.lower()]
    except KeyError:
        if args:
            cmd = f"{cmd} {args[0]}"
            args = args[1:]

        handler = HANDLERS[cmd.lower(), "Unknown command"]
    return handler, args

def main():
    while True:
        user_input = input(">>>")
        handler, *args = parser_input(user_input)
        try:
            result = handler(*args)
        except TypeError:
            print('Unknown command, please try again.')
            continue
        if result == "Good bye!":
            print(result)
            break
        print(result)

if __name__ == "__main__":
    main()
    