# Use Cases
- Create a todo
- Show all the todo
- Edit, delete, mark as complete, incomplete, etc

# Command to use the CLI
=> prefixes for the commands: list, to
- Todo show => show all the todo 
- add to do => create a todo
- todo edit TaskID
- todo remove TaskID
- todo complete Status => Status = True is todo complete
- todo incomplete Status => Status = False is todo incomplete
- Created Date
- help => print all the command can use in app
- quit => exit the application

# Data

## ToDo.json
- store as dict of to do   
{
    'TaskID':
    {
        'Task': text,
        'Created Date': DateTime,
        'Status': False
    }
}

data['TaskID']['Description]