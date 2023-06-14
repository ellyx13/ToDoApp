from command import command_dict
def parse(command):
    command = command.split(" ")
    cmd_type = command[0]
    cmd_have = ['edit', 'remove', 'complete', 'incomplete', 'deleteAll']
    cmd_1args = ['help', 'quit', 'show', 'deleteAll']
    if cmd_type in cmd_1args:
        return cmd_type, None
    elif cmd_type == 'edit':
        return cmd_type, command[1]
    elif cmd_type == 'add': 
        return cmd_type, command[1:]
    else:
        return 'invalid', None

def main():
    print('Started the Todo application...')
    while True:
        command = input("$ ")
        command_name, command_arg = parse(command)
        if command_name == 'quit':
            break
        elif command_name == 'help':
            with open('help.txt', 'r') as help_file:
                print(help_file.read())
        elif command_name == 'invalid':
            print("Invalid command. Try again or use help")
        else:
            command_dict[command_name](command_arg)

main()

