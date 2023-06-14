import datetime
import json
class Task:
    def __init__(self):
        pass
    @staticmethod
    def get_Data():
        data = {}
        with open("db.json", 'r+') as json_file :
            file = json_file.read()
            if file != '':
                data = json.loads(file)
        return data
    @staticmethod
    def update_Date(new_Data):
        with open('db.json', 'w') as file:
            json.dump(new_Data, file, indent=4)
            
    def show(self, args):
        data = self.get_Data()
        empty = False
        if bool(data) == empty:
            print("No data. Please create Task by use add")
        else:
            print(json.dumps(data, indent=4))
    def add(self, args):
        current_date = datetime.date.today()
        data = self.get_Data()
        taskID = 'Task' + str(len(data) + 1)
        isComplete = False
        task = ' '.join(args)
        task = {
                taskID: 
                {
                    'Task': task,
                    'CreatedDate': current_date.isoformat(),
                    'Status': isComplete,
                }
            }
        data.update(task)
        self. update_Date(data)
    def edit(self, args):
        taskID, newTask = args
        data = self.get_Data()
        data[taskID]['Task'] = newTask
        self.update_Date(data)
    def remove(self, args):
        data = self.get_Data()
        data.pop(args)
        self.update_Date(data)
    def complete(self, args):
        data = self.get_Data()
        data[args]['Status'] = True
        self.update_Date(data)
    def incomplete(self, args):
        data = self.get_Data()
        data[args]['Status'] = False
        self.update_Date(data)
    def deleteAll(self, args):
        data = {}
        self.update_Date(data)