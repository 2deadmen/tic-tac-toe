count=0
a1=["1"]
a2=["2"]
a3=['3']
b4=['4']
b5=['5']
b6=['6']
c7=['7']
c8=['8']
c9=['9']
pos={
   "a1":a1,
    "a2":a2,
    "a3":a3,
    "b4":b4,
    "b5":b5,
    "b6":b6,
    "c7":c7,
    "c8":c8,
    "c9":c9

}
def display():
    print(f"a{a1}   a{a2}  a{a3} \nb{b4}  b{b5}  b{b6} \nc{c7}  c{c8}  c{c9} \n")
print("TIC TAC TOE\n\n")
while True:

    display()
    #checking the player number
    if count%2==0:

        value=input("enter the position player 1").lower()
        for i in pos.keys():
            #identifying the position
            if value==i:
                #checking if it is empty
                if not (pos[i][0] == "X" or pos[i][0]=="0"):
                    pos[i][0] ="X"
                    count += 1
                else:
                    print("choose another block")

    else:

        value=input("enter the position player 2").lower()
        for i in pos.keys():
            #identifying the position
            if value==i:
                #checking if it is empty
                if not (pos[i][0] == "X" or pos[i][0]=="0"):
                    pos[i][0] = "0"
                    count += 1
                else:
                    print("choose another block")

    #checking for results
    if(a1==a2==a3 or a1==b4==c7 or c7==c8==c9 or c9==b6==a3 or a1==b5==c9 or c7==b5==a3 or a2==b5==c8 or b4==b5==b6):
        display()
        if(count%2==0):
            print("player 1 has won")
            break
        else:
            print("player 2 has won")
            break



