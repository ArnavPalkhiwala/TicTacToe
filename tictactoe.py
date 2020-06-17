from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

playerOneName = input('Player one, please enter your name: ')
playerTwoName = input('Player two, please enter your name: ')
ActivePlayer = 1
player1 = []
player2 = []
count = 0

root = Tk()
root.title(f'Tic Tac Toe: {playerOneName}')
style = ttk.Style()
style.theme_use('classic')

b1 = ttk.Button(root, text=' ')
b1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
b1.config(command=lambda: BuClick(1))

b2 = ttk.Button(root, text=' ')
b2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
b2.config(command=lambda: BuClick(2))

b3 = ttk.Button(root, text=' ')
b3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
b3.config(command=lambda: BuClick(3))

b4 = ttk.Button(root, text=' ')
b4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
b4.config(command=lambda: BuClick(4))

b5 = ttk.Button(root, text=' ')
b5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
b5.config(command=lambda: BuClick(5))

b6 = ttk.Button(root, text=' ')
b6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
b6.config(command=lambda: BuClick(6))

b7 = ttk.Button(root, text=' ')
b7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
b7.config(command=lambda: BuClick(7))

b8 = ttk.Button(root, text=' ')
b8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
b8.config(command=lambda: BuClick(8))

b9 = ttk.Button(root, text=' ')
b9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
b9.config(command=lambda: BuClick(9))


def BuClick(id):
    global ActivePlayer
    global player1
    global player2
    if ActivePlayer == 1:
        SetLayout(id, 'X')
        player1.append(id)
        root.title(f'Tic Tac Toe: {playerTwoName}')
        ActivePlayer = 2
        print("player1:{}".format(player1))
    elif ActivePlayer == 2:
        SetLayout(id, 'O')
        player2.append(id)
        root.title(f'Tic Tac Toe: {playerOneName}')
        ActivePlayer = 1
        print("player2:{}".format(player2))
    Winner()


def SetLayout(id, text):
    if id == 1:
        b1.config(text=text)
        b1.state(['disabled'])

    elif id == 2:
        b2.config(text=text)
        b2.state(['disabled'])

    elif id ==3:
        b3.config(text=text)
        b3.state(['disabled'])

    elif id == 4:
        b4.config(text=text)
        b4.state(['disabled'])

    elif id == 5:
        b5.config(text=text)
        b5.state(['disabled'])

    elif id == 6:
        b6.config(text=text)
        b6.state(['disabled'])

    elif id == 7:
        b7.config(text=text)
        b7.state(['disabled'])

    elif id == 8:
        b8.config(text=text)
        b8.state(['disabled'])

    elif id == 9:
        b9.config(text=text)
        b9.state(['disabled'])


def Winner():
    Winner = -1
    if 1 in player1 and 2 in player1 and 3 in player1:
        Winner = 1
    elif 1 in player2 and 2 in player2 and 3 in player2:
        Winner = 2
    elif 4 in player1 and 5 in player1 and 6 in player1:
        Winner = 1
    elif 4 in player2 and 5 in player2 and 6 in player2:
        Winner = 2
    elif 7 in player1 and 8 in player1 and 9 in player1:
        Winner = 1
    elif 7 in player2 and 8 in player2 and 8 in player2:
        Winner = 2
    elif 1 in player1 and 4 in player1 and 7 in player1:
        Winner = 1
    elif 1 in player2 and 4 in player2 and 7 in player2:
        Winner = 2
    elif 2 in player1 and 5 in player1 and 8 in player1:
        Winner = 1
    elif 2 in player2 and 5 in player2 and 8 in player2:
        Winner = 2
    elif 3 in player1 and 6 in player1 and 9 in player1:
        Winner = 1
    elif 3 in player2 and 6 in player2 and 9 in player2:
        Winner = 2
    elif 1 in player1 and 5 in player1 and 9 in player1:
        Winner = 1
    elif 1 in player2 and 5 in player2 and 9 in player2:
        Winner = 2
    elif 3 in player1 and 5 in player1 and 7 in player1:
        Winner = 1
    elif 3 in player2 and 5 in player2 and 7 in player2:
        Winner = 2
    if Winner == 1:
        messagebox.showinfo(title="Great Job!", message = f'{playerOneName} is the Winner!')

    elif Winner == 2:
        messagebox.showinfo(title="Great Job!", message = f'{playerTwoName} is the Winner!')
    elif count == 9:
        messagebox.showinfo(title="Tie!", message = f'You tied!!')


def AutoPlay():
    global player1
    global player2
    EmptyCell = []
    for cell in range(9):
        if not((cell+1 in player1) or (cell+1 in player2)):
            EmptyCell.append(cell + 1)
        RandIndex = randint(0, len(EmptyCell)-1)
        BuClick(EmptyCell[RandIndex])



root.mainloop()