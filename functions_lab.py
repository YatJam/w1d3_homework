tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# Given the following list of dictionaries, use functions throughout to create a program to manage a task list.
# As a user, to manage my task list I would like a program that allows me to:
# Print a list of uncompleted tasks

def find_uncompleted_tasks(tasks):
    uncompleted_tasks  = []
    for task in tasks:
        if task["completed"] == False:
            # put in uncomplete_tasks lists if condition met
            uncompleted_tasks.append(task)
# create return for uncompleted tasks
    return uncompleted_tasks        
        
print(find_uncompleted_tasks(tasks))
print("")
# Print a list of completed tasks
def find_completed_tasks(tasks):
    completed_tasks = []
    for task in tasks:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks

print(find_completed_tasks(tasks))
print("")
# Print a list of all task descriptions
def task_descriptions(tasks):
    descriptions = []
    for task in tasks:
        descriptions.append(task['description'])
    return descriptions

print(task_descriptions(tasks))
print("")
# Print a list of tasks where time_taken is at least a given time
def find_tasks_with_min_time(min_time, tasks):
    chosen_time_tasks = []
    for task in tasks:
        if task["time_taken"] >= min_time:
            chosen_time_tasks.append(task)
    return chosen_time_tasks

print(find_tasks_with_min_time(15, tasks))
print("")
# Print any task with a given description

def find_a_description(description, tasks):
    for task in tasks:
        if task["description"] == description:
            return task

print(find_a_description("Make Dinner", tasks))
print("")
# Extension
# Given a description update that task to mark it as complete.
def update_task(description, tasks):
    for task in tasks:
        if task["description"] == description:
           task["completed"] = True
           return task

print(update_task("Wash Dishes", tasks))
print("")
# Add a task to the list
def add_task(task, tasks):
    tasks.append(task)
    return tasks
# assign new variable outside of function representing the "task" (the new dictionary to be added)
new_task = {"description": "Fluff Pillows", "completed": True, "time_taken": 40 }
# instead of inputting the new dictionary into the call, use a variable as assigned above
print(add_task(new_task, tasks))