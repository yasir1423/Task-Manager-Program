#task manager program using file handling and list.
task_file="tasks.txt"
#function to load tasks from file
def load_tasks():
    try:
        with open(task_file,"r") as f:
            tasks=[line.strip() for line in f.readlines()]#explanation=>below
    except FileNotFoundError:
        tasks=[]#if file does not exist start with an empty list
    return tasks#must return a list
print("load tasks:",load_tasks())
#function to save the task file
def save_tasks(tasks):
    with open(task_file,"w") as f:
        for task in tasks:
            f.write(task+ "\n")
#function to veiw task
def veiw_tasks(tasks):
    if not tasks:
        print("No tasks Available!!!!\n")
    else:
        print("Your Tasks:\n")
        for i, task in enumerate(tasks,start=1):#explanation=>below
            print(f"{i}.{task}")
        print()
#function to add tasks
def add_tasks(tasks):
    task=input("Enter new task:")
    tasks.append(task)#appen() is built in function to add new element at the end of list. 
    save_tasks(tasks)
    print("Task added successfully!!!")
#function to delete tasks
def delete_tasks(tasks):
    veiw_tasks(tasks)
    if tasks:
        try:
            n=int(input("Enter the task number you want to delete:"))
            if(n>=1 or n<=len(tasks)):
                removed=tasks.pop(n-1)#explanation=>below
                save_tasks(tasks)
                print(f"task '{removed}' deleted successfuly!!!")
            else:
                print("Invalid Number!!! Please enter the correct number")
        except ValueError:
            print("please enter a valid number...")
#Main program loop
def main():
    tasks=load_tasks()
    while True:
        print("<=TASK MANAGER=>")
        print("1.Veiw task" )
        print("2.Add task")
        print("3.Delete Task")
        print("4.Exit")
        choice=input("Enter you choice(1-4):")
        if choice=='1':
            veiw_tasks(tasks)
        elif choice=='2':
            add_tasks(tasks)
        elif choice=='3':
            delete_tasks(tasks)
        elif choice=='4':
            print("Exiting from program.....")
            break
        else:
            print("Invalid Choice.Try again later.\n ")
#Run the program
if __name__=="__main__":
    main()
''' for line 7:here f.readlines read all the lines of file(f=>file) included 
in program and strip() function is used to remonve extra spaces and at the
end of line.for loop here is used to go through all lines.
for line 22: enumerate is built in function that lets us loop through both
index and item at the same time.
for line 39:pop() is a listed method in python that removes an element from
a list by its index and also returns the removed element and n-1 is for if 
the user enter 1 to delete the task 1 so it will delete the task 1 which is 
at 0 index as in pytthon index start from zero(e.g:0,1,2,3,4....) '''