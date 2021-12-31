from tkinter import*
from tkinter import messagebox

ws=Tk()
ws.title("Tic Tac Toe")
ws.geometry('')
ws.config(background='Dark gray')
f=('arial', 20 ,'bold')
f1=('arial', 15 ,'bold')
click=True


count_x = 0
count_o = 0
number = 0
var_x = StringVar()
var_o = StringVar()
var_gameX = StringVar()
var_gameO = StringVar()
gameX_count = 0
gameO_count = 0



def reset():
    but1['text'] = " "
    but2['text'] = " "
    but3['text'] = " "
    but4['text'] = " "
    but5['text'] = " "
    but6['text'] = " "
    but7['text'] = " "
    but8['text'] = " "
    but9['text'] = " "


def buttons_disable():
    but1['text'] = " "
    but2['text'] = " "
    but3['text'] = " "
    but4['text'] = " "
    but5['text'] = " "
    but6['text'] = " "
    but7['text'] = " "
    but8['text'] = " "
    but9['text'] = " "


def game(but):
    global click
    global count_x
    global count_o
    global number
    global gameX_count
    global gameO_count
    if but['text'] == " " and click == True:
        but['text'] = "X"
        click = False

    elif but['text'] == " " and click == False:
        but['text'] = "O"
        click = True

    if but1['text'] == "X" and but2['text'] == "X" and but3['text'] == "X":
        count_x += 1

        messagebox.showinfo("Tic Tac Toe", "Player_X hat ein Punkt!")
        buttons_disable()



    if but4['text'] == "X" and but5['text'] == "X" and but6['text'] == "X":
        count_x += 1
        gameX_count +=1
        messagebox.showinfo("Tic Tac Toe", "Player_X hat ein Punkt!")
        buttons_disable()


    if but7['text'] == "X" and but8['text'] == "X" and but9['text'] == "X":
        count_x += 1
        gameX_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_X hat ein Punkt!")
        buttons_disable()

    if but1['text'] == "X" and but5['text'] == "X" and but9['text'] == "X":
        count_x += 1
        gameX_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_X hat ein Punkt!")
        buttons_disable()


    if but3['text'] == "X" and but5['text'] == "X" and but7['text'] == "X":
        count_x += 1
        gameX_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_X hat ein Punkt!")
        buttons_disable()

    if but1['text'] == "X" and but4['text'] == "X" and but7['text'] == "X":
        count_x += 1
        gameX_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_X hat ein Punkt!")
        buttons_disable()


    if but2['text'] == "X" and but5['text'] == "X" and but8['text'] == "X":
        count_x += 1
        gameX_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_X hat ein Punkt!")
        buttons_disable()

    if but3['text'] == "X" and but6['text'] == "X" and but9['text'] == "X":
        count_x += 1
        gameX_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_X hat ein Punkt!")
        buttons_disable()


    if but1['text'] == "O" and but2['text'] == "O" and but3['text'] == "O":
        count_o += 1
        gameO_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_O hat ein Punkt!")
        buttons_disable()


    if but4['text'] == "O" and but5['text'] == "O" and but6['text'] == "O":
        count_o += 1
        gameO_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_O hat ein Punkt!")
        buttons_disable()


    if but7['text'] == "O" and but8['text'] == "O" and but9['text'] == "O":
        count_o += 1
        gameO_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_O hat ein Punkt!")
        buttons_disable()


    if but1['text'] == "O" and but5['text'] == "O" and but9['text'] == "O" :
        count_o += 1
        gameO_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_O hat ein Punkt!")
        buttons_disable()


    if but3['text'] == "O" and but5['text'] == "O" and but7['text'] == "O":
        count_o += 1
        gameO_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_O hat ein Punkt!")
        buttons_disable()


    if but1['text'] == "O" and but4['text'] == "O" and but7['text'] == "O":
        count_o += 1
        gameO_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_O hat ein Punkt!")
        buttons_disable()

    if but2['text'] == "O" and but5['text'] == "O" and but8['text'] == "O":

        count_o += 1
        gameO_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_O hat ein Punkt!")
        buttons_disable()
    if but3['text'] == "O" and but6['text'] == "O" and but9['text'] == "O":
        count_o += 1
        gameO_count += 1
        messagebox.showinfo("Tic Tac Toe", "Player_O hat ein Punkt!")
        buttons_disable()





    if count_x == 1:
        number = 1
        var_x.set(number)
    elif count_x == 2:
        number = 2
        var_x.set(number)
    elif count_x == 3:
        number=3
        var_x.set(number)
        messagebox.showinfo("Tic Tac Toe", "Player_X hat 3 Punkte!")



    if count_o == 1:
        number = 1
        var_o.set(number)
    elif count_o == 2:
        number = 2
        var_o.set(number)
    elif count_o == 3:
        number = 3
        var_o.set( number )
        messagebox.showinfo("Tic Tac Toe", "Player_O hat 3 Punkte!")

    if Point_X.get() == "3" or Point_O.get() == "3":
        count_x = 0
        count_o = 0
        number = 0
        var_x.set(number)
        var_o.set(number)


    if gameX_count == 3:
        var_gameX.set(1)
    elif gameX_count == 6:
        var_gameX.set(2)
    elif gameX_count == 9:
        var_gameX.set(3)
        messagebox.showinfo("Tic Tac Toe", ' Player_X hat gewonnen')

    if gameO_count == 3:
        var_gameO.set(1)
    elif gameO_count == 6:
        var_gameO.set(2)
    elif gameO_count == 9:
        var_gameO.set(3)
        messagebox.showinfo("Tic Tac Toe", ' Player_O hat gewonnen')


    if game_X.get() == "3" or game_O.get() == "3":

        var_gameX.set(0)
        var_gameO.set(0)



but1 =Button(ws, fg="blue", bg='Dark gray', font=f,width=6,height=3 ,text=" ",command= lambda : game(but1))
but2 =Button(ws, fg="blue", bg='Dark gray', font=f,width=6,height=3 ,text=" ",command= lambda : game(but2))
but3 =Button(ws, fg="blue", bg='Dark gray', font=f,width=6,height=3 ,text=" ",command= lambda : game(but3))
but4 =Button(ws, fg="blue", bg='Dark gray', font=f,width=6,height=3 ,text=" ",command= lambda : game(but4))
but5 =Button(ws, fg="blue", bg='Dark gray', font=f,width=6,height=3 ,text=" ",command= lambda : game(but5))
but6 =Button(ws, fg="blue", bg='Dark gray', font=f,width=6,height=3 ,text=" ",command= lambda : game(but6))
but7 =Button(ws, fg="blue", bg='Dark gray', font=f,width=6,height=3 ,text=" ",command= lambda : game(but7))
but8 =Button(ws, fg="blue", bg='Dark gray', font=f,width=6,height=3 ,text=" ",command= lambda : game(but8))
but9 =Button(ws, fg="blue", bg='Dark gray', font=f,width=6,height=3 ,text=" ",command= lambda : game(but9))


but1.grid(row=0, column=0)
but2.grid(row=0, column=1)
but3.grid(row=0, column=2)
but4.grid(row=1, column=0)
but5.grid(row=1, column=1)
but6.grid(row=1, column=2)
but7.grid(row=2, column=0)
but8.grid(row=2, column=1)
but9.grid(row=2, column=2)



Label(
    ws,
    text=" ",
    bg='Dark gray',
    font=f1
) .grid(row=3, column=0,pady=10,sticky=W)

Label(
    ws,
    text="Player_X",
    bg='Dark gray',
    font=f1
) .grid(row=4, column=0,pady=10,sticky=W)
Label(
    ws,
    text="Player_O",
    bg='Dark gray',
    font=f1
) .grid(row=5, column=0,pady=10,sticky=W)
Label(
    ws,
    text="Games_X",
    bg='Dark gray',
    font=f1
) .grid(row=4, column=2,pady=10,sticky=W)
Label(
    ws,
    text="Games_O",
    bg='Dark gray',
    font=f1
) .grid(row=5, column=2,pady=10,sticky=W)
Point_X=Entry(
    ws,
    font=f1,
    width=5,
    bd=7,
    textvariable=var_x
)
Point_O=Entry(
    ws,
    font=f1,
    width=5,
    bd=7,
    textvariable=var_o
)

game_X=Entry(
    ws,
    font=f1,
    width=5,
    bd=7,
    text=var_gameX
)
game_O=Entry(
    ws,
    font=f1,
    width=5,
    bd=7,
    text=var_gameO
)
rest_but = Button(
    ws,
    width=5,
    text='Reset',
    font=f1,
    bg='dark gray',
    bd=5,
    relief=SOLID,
    cursor='hand2',
    command=reset
)

rest_but.grid(row=1, column=3, padx=10, pady=10)
Point_X.grid(row=4, column=1,padx=5, pady=5)
game_X.grid(row=4, column=3)
Point_O.grid(row=5, column=1)
game_O.grid(row=5, column=3)

ws.mainloop()


