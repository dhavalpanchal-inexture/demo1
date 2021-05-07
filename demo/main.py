stk_list = ['10','20','30']

def push():
    add_value = input("enter the value to add")
    stk_list.append(add_value)
    print(stk_list)

def pop():
    if len(stk_list) > 0:
        print(stk_list)
        del_value = int(input("eter position to delete"))
        stk_list.pop(del_value)
        print(stk_list)

def peep():
    if len(stk_list) > 0:
        print(stk_list)
        print("peep value is -",stk_list[-1])
    else:
        print("value is not valid")

while True:
    print("stack operations")
    print("1.pop")
    print("2.pop")
    print("3.pip")
    print("4.quit")
    ch = int(input("enter your choice"))

    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        peep()
    elif ch==4:
        quit()
    else:
        print("invalid number")