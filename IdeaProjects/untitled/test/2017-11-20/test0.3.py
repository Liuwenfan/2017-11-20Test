#!/usr/bin/env python
# queue实现堆栈
queue = []


def insert():
    queue_buff = input("Enter you string:")
    queue.append(queue_buff)


def delete():
    if len(queue) == 0:
        print("cannot delete from empty queue")
    else:
        queue_buff = queue.pop(len(queue) - 1)
        view()


def view():
    print(queue)


def showmenu():
    print("""
        action1:insert
        action2:delete
        action3:view
        action4:quit
    """)

    while True:
        try:
            choice = input("Enter you action:").strip().lower()
        except (EOFError, KeyboardInterrupt):
            choice = "quit"

        if choice == "insert":
            insert()
        elif choice == "delete":
            delete()
        elif choice == "view":
            view()
        elif choice == "quit":
            quit()


if __name__ == '__main__':
    showmenu()
