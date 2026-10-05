def add_task(task_name, task_list=[]):
    task_list.append(task_name)
    return task_list


print(add_task("Buy milk"))
print(add_task("Write report"))
print(add_task("Call mom"))