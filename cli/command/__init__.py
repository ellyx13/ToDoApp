from command.todo import Task

task = Task()
command_dict = {
    'show': task.show,
    'add': task.add,
    'edit': task.edit,
    'remove': task.remove,
    'complete': task.complete,
    'incomplete': task.incomplete,
    'deleteAll': task.deleteAll
}