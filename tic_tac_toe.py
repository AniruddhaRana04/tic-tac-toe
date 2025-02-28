import random as r
a=[" "," "," "," "," "," "," "," "," "]

# Print box 
def draw():
    c=0

    for item in a:
        if c%3==0:
            print("\n-----------------")
        print(f"| {item} |",end=" ")
        c+=1
    print("\n-----------------")

# For user input 
def user_input():
    while True:
        n=int(input("Enter your input (1,9): "))
        if a[n-1] == " ":
            a[n-1]=1
            break
        if a[n-1] == 0:
            print("It is all ready choose by Computer .")
        if a[n-1] == 1: 
            print("It is all ready choose by you")
# For computer input
def computer_input():
    if a[0]==a[1]==0 and a[2]==" ":
        n=2
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[1]==a[2]==0 and a[0]==" ":
        n=0
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[0]==a[2]==0 and a[1]==" ":
        n=1
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[3]==a[4]==0 and a[5]==" ":
        n=5
        a[n]=0
        print(f"Computer choose : {+1}")
        return

    if a[3]==a[5]==0 and a[4]==" ":
        n=4
        a[n]=0
        print(f"Computer choose : {+1}")
        return
    
    if a[5]==a[4]==0 and a[3]==" ":
        n=3
        a[n]=0
        print(f"Computer choose : {+1}")
        return
    
    if a[6]==a[7]==0 and a[8]==" ":
        n=8
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[8]==a[7]==0 and a[6]==" ":
        n=6
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[6]==a[8]==0 and a[7]==" ":
        n=7
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[0]==a[3]==0 and a[6]==" ":
        n=6
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[0]==a[6]==0 and a[3]==" ":
        n=3
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[6]==a[3]==0 and a[0]==" ":
        n=0
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[1]==a[4]==0 and a[7]==" ":
        n=7
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[1]==a[7]==0 and a[4]==" ":
        n=4
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[7]==a[4]==0 and a[1]==" ":
        n=1
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[2]==a[5]==0 and a[8]==" ":
        n=8
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[2]==a[8]==0 and a[5]==" ":
        n=5
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[8]==a[5]==0 and a[2]==" ":
        n=2
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[0]==a[4]==0 and a[8]==" ":
        n=8
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[8]==a[4]==0 and a[0]==" ":
        n=0
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[0]==a[8]==0 and a[4]==" ":
        n=4
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[2]==a[4]==0 and a[6]==" ":
        n=6
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[6]==a[4]==0 and a[2]==" ":
        n=2
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[2]==a[6]==0 and a[4]==" ":
        n=4
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    if a[0]==a[1]==1 and a[2]==" ":
        n=2
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[1]==a[2]==1 and a[0]==" ":
        n=0
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[0]==a[2]==1 and a[1]==" ":
        n=1
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[3]==a[4]==1 and a[5]==" ":
        n=5
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[3]==a[5]==1 and a[4]==" ":
        n=4
        a[n]=0
        print(f"Computer choose : {n+1}")
        return

    if a[5]==a[4]==1 and a[3]==" ":
        n=3
        a[n]=0
        print(f"Computer choose : {n+1}")
        return

    if a[6]==a[7]==1 and a[8]==" ":
        n=8
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[8]==a[7]==1 and a[6]==" ":
        n=6
        a[n]=0
        print(f"Computer choose : {n+1}")
        return

    if a[6]==a[8]==1 and a[7]==" ":
        n=7
        a[n]=0
        print(f"Computer choose : {n+1}")
        return

    if a[0]==a[3]==1 and a[6]==" ":
        n=6
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[0]==a[6]==1 and a[3]==" ":
        n=3
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[6]==a[3]==1 and a[0]==" ":
        n=0
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[1]==a[4]==1 and a[7]==" ":
        n=7
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[1]==a[7]==1 and a[4]==" ":
        n=4
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[7]==a[4]==1 and a[1]==" ":
        n=1
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[2]==a[5]==1 and a[8]==" ":
        n=8
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[2]==a[8]==1 and a[5]==" ":
        n=5
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[8]==a[5]==1 and a[2]==" ":
        n=2
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[0]==a[4]==1 and a[8]==" ":
        n=8
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[8]==a[4]==1 and a[0]==" ":
        n=0
        a[n]=0
        print(f"Computer choose : {n+1}")
        return

    if a[0]==a[8]==1 and a[4]==" ":
        n=4
        a[n]=0
        print(f"Computer choose : {n+1}")
        return

    if a[2]==a[4]==1 and a[6]==" ":
        n=6
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
    
    if a[6]==a[4]==1 and a[2]==" ":
        n=2
        a[n]=0
        print(f"Computer choose : {n+1}")
        return
     
    if a[2]==a[6]==1 and a[4]==" ":
        n=4
        a[n]=0
        print(f"Computer choose : {n+1}")
        return

    else:
        while(True):
            n=r.randint(1,9)
            if a[n-1] == " ":
                a[n-1]=0
                break
        print(f"Computer choose : {n}")

# for check 
def check():
    if (a[0]==a[1]==a[2]==1)or(a[3]==a[4]==a[5]==1)or(a[6]==a[7]==a[8]==1)or(a[0]==a[3]==a[6]==1)or(a[1]==a[4]==a[7]==1)or(a[2]==a[5]==a[8]==1)or(a[0]==a[4]==a[8]==1)or(a[2]==a[4]==a[6]==1):
        print("You win !")
        return 1
    if (a[0]==a[1]==a[2]==0)or(a[3]==a[4]==a[5]==0)or(a[6]==a[7]==a[8]==0)or(a[0]==a[3]==a[6]==0)or(a[1]==a[4]==a[7]==0)or(a[2]==a[5]==a[8]==0)or(a[0]==a[4]==a[8]==0)or(a[2]==a[4]==a[6]==0):
        print("Computer win !")
        return 1
    if  " "not in a: 
        print("It's a draw !")
        return 1
    
def main1():
    k=0
    draw()
    while True:
        user_input()
        draw()
        k=check()
        if k==1:
            break
        computer_input()
        draw()
        k=check()
        if k==1:
            break
        k=check()
        if k==1:
            break
def main2():
        k=0
        draw()
        while True:
            computer_input()
            draw()
            k=check()
            if k==1:
                break
            user_input()
            draw()
            k=check()
            if k==1:
                break
            k=check()
            if k==1:
               break
def run():
    while True:
        global a
        a=[" "," "," "," "," "," "," "," "," "]
        main1()
        print("""
                1.Replay
                2.Exit
        """)
        an=int(input("Enter your choice : "))
        if an==1:
            a=[" "," "," "," "," "," "," "," "," "]
            main2()
            print("""
                1.Replay
                2.Exit
            """)
            anr=int(input("Enter your choice : "))
            if anr==2:
                exit()
        else:
            exit()

run()