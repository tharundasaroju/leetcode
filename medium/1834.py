from os import pipe


def getOrder(tasks: list[list[int]]) -> list[int]:
    taskList: list['Task'] = []
    order: list[int] = []
    i = 0
    for task in tasks:
        taskList.append(Task(i, task[0], task[1]))
        i += 1
    taskList.sort(reverse=True)

    current_time = 0
    pipeline: list['Task'] = []
    while(len(taskList) > 0 or len(pipeline) > 0):
        if(len(taskList) > 0):
            task = taskList.pop()
        else:
            task = None
        if(task != None and current_time == 0):
            current_time = task.eTime
            pipeline.append(task)
        elif(task != None and current_time >= task.eTime):
            # print(current_time, task)
            pipeline.append(task)
        else:
            (presentTask, pipeline) = pickTask(pipeline)
            print("ptask",current_time, presentTask)
            current_time = current_time+presentTask.pTime
            order.append(presentTask.id)
            if(task!=None): 
                print(current_time, task)
                taskList.append(task)

    print(order)
    return order


def pickTask(tasks: list['Task']):
    task: 'Task' = None
    finalList = []
    for i in range(len(tasks)):
        if(task != None):
            if(tasks[i].pTime < task.pTime or (tasks[i].pTime == task.pTime and tasks[i].id < task.id)):
                finalList.append(task)
                task = tasks[i]
            else:
                finalList.append(tasks[i])
        else:
            task = tasks[i]
    # if(task.id in [12, 5]):
        # print(tasks)
    return (task, finalList)


class Task:
    def __init__(self, id: int, eTime: int, pTime: int):
        self.id = id
        self.eTime = eTime
        self.pTime = pTime

    def __lt__(self, other: 'Task'):
        return self.eTime < other.eTime

    def __str__(self):
        return f"id = {self.id}, eTime = {self.eTime}, pTime = {self.pTime}"

    def __repr__(self):
        return f"id:{self.id} eTime: {self.eTime} pTime:{self.pTime}"


getOrder([[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]])
