que_list = ['10','20','30']

def enqueue():
    add_value = input("enter the value to add")
    que_list.append(add_value)
    print(que_list)

def dequeue():
    if len(que_list) > 0:
        print(que_list)
        del_value = int(input("eter position to delete"))
        que_list.pop(del_value)
        print(que_list)

def peek():
    if len(que_list) > 0:
        print(que_list)
        print("peep value is -",que_list[0])
    else:
        print("value is not valid")

while True:
    print("queue operations")
    print("1.enqueue")
    print("2.dequeue")
    print("3.peek")
    print("4.quit")
    ch = int(input("enter your choice"))

    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        peek()
    elif ch==4:
        quit()
    else:
        print("invalid number")