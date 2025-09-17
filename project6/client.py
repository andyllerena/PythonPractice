import requests

BASE_URL = "http://127.0.0.1:5000/"


def show_menu():
    print("\n==== Todo App ====")
    print("1. View all todos")
    print("2. View a specific todo")
    print("3. Add a new todo")
    print("4. Delete a todo")
    print("q. Quit")
    print("==================")


def view_all_todos():
    response = requests.get(BASE_URL + "todo")
    data = response.json()
    print(data)

def get_todo_by_id(id):
    response = requests.get(BASE_URL + f"todo/{id}" )
    data = response.json()
    
    task = data["todo"]["task"]

    print(task)

def add_new_todo(task):

    new_todo = {"task" : task}

    create_response = requests.post(BASE_URL + "todos",json=new_todo )

    response = requests.get(BASE_URL + "todo")
    data = response.json()
    print(data)


  

def main():
    show_menu()
    answer = ""

    
    while answer != 'q':

        answer = input("Enter your choice").lower()


        if answer == "1":
            view_all_todos()
        
        elif answer == "2":
            id = input("Enter the id of the task")
            get_todo_by_id(id)

        elif answer == "3":
            task = input("Enter the new todo ")
            add_new_todo(task)
        
        elif answer == 'q':
            print("GoodBye")
            break
        
        else:
            "Please Try Again"
            
        



if __name__ == "__main__":
    main()