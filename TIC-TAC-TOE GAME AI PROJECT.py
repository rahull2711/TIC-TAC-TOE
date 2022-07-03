#TIC-TAC-TOE GAME USING MINIMAX ALGORITHM IN AI (WITH GUI INTERFACE)

from tkinter import *
from tkinter import messagebox
import random
game = [None] * 9
winningCombos = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
AIfirst = False
def init():
    global AIfirst
    game[8] = 'X'
    draw()
    AIfirst = True
def availableMoves(node):
    movesArr = []
    for x in range(9):
        if None == node[x]:
            movesArr.append(x)
    return movesArr
def terminate(node):
    complete = True
    for x in range(9):
        if node[x] == None:
            complete = False
    if complete:
        return True
    if winner(node) != None:
        return True
    return False
def winner(node):
    for player in ['X', 'O']:
        playerPositions = getSquares(player, node)
        for combo in winningCombos:
            win = True
            for position in combo:
                if position not in playerPositions:
                    win = False
            if win:
                return player
    return None
def getSquares(player, node):
    squares = []
    for x in range(9):          
        if node[x] == player:
            squares.append(x)
    return squares
def makeMove(position, player, node):
    node[position] = player
def minimax(node, maxPlayer):
    if terminate(node):
        if winner(node) == 'X':
            return 1, node
        elif winner(node) == 'O':
            return -1, node
        return 0, node
    if maxPlayer:
        best = -1
        bestMove = None
        for move in availableMoves(node):
            makeMove(move, 'X', node)
            val, choice = minimax(node, False)
            makeMove(move, None, node)
            if val >= best:
                bestMove = move
                best = val
        return best, bestMove
    else:
        best = 1
        bestMove = None
        for move in availableMoves(node):
            makeMove(move, 'O', node)
            val, choice = minimax(node, True)
            makeMove(move, None, node)
            if val <= best:
                bestMove = move
                best = val
        return best, bestMove
def update(event):
    global game
    if AIfirst:
        if len(getSquares('X', game)) != len(getSquares('O', game)) +1:
            return
    else:
        if len(getSquares('X', game)) != len(getSquares('O', game)):
            return
    if event.x in range(10, 291) and event.y in range(10, 291):
        if game[0] == None:
            game[0] = 'O'
        else:
            return
    elif event.x in range(310, 591) and event.y in range(10, 291):
        if game[1] == None:
            game[1] = 'O'
        else:
            return
    elif event.x in range(610, 891) and event.y in range(10, 291):
        if game[2] == None:
            game[2] = 'O'
        else:
            return
    elif event.x in range(10, 291) and event.y in range(310, 591):
        if game[3] == None:
            game[3] = 'O'
        else:
            return
    elif event.x in range(310, 591) and event.y in range(310, 591):
        if game[4] == None:
            game[4] = 'O'
        else:
            return
    elif event.x in range(610, 891) and event.y in range(310, 591):
        if game[5] == None:
            game[5] = 'O'
        else:
            return
    elif event.x in range(10, 291) and event.y in range(610, 891):
        if game[6] == None:
            game[6] = 'O'
        else:
            return
    elif event.x in range(310, 591) and event.y in range(610, 891):
        if game[7] == None:
            game[7] = 'O'
        else:
            return
    elif event.x in range(610, 891) and event.y in range(610, 891):
        if game[8] == None:
            game[8] = 'O'
        else:
            return
    draw()
    if terminate(game):
        endgame()
        return 
    if easy.get() == 0:
        outcome, bestMove = minimax(game, True)
        game[bestMove] = 'X'
    else:
        easyMove = randomMove(game)
        game[easyMove] = 'X'
    draw()
    if terminate(game):
        endgame()
        return
def randomMove(game):
    return random.choice(availableMoves(game))
def draw():
    global game
    count = 0
    for x in range(150, 751, 300):
        for y in range(150, 751, 300):
            if game[count] == None:
                symbol = ' '
            else:
                symbol = game[count]
            if symbol == 'X':
                canvas.create_text((y, x), font = ('Arial', 290), text = symbol, fill = 'red', tag='Del')
            else:
                canvas.create_text((y, x), font = ('Arial', 290), text = symbol, fill = 'blue', tag='Del')
            count += 1
    root.update()
def endgame():
    global game
    if winner(game) == 'X':
        messagebox.showerror('LOSER!', 'You lost!')
    elif winner(game) == 'O':
        messagebox.showerror('NOOOOOB', 'You have won but you are a noob who picked easy AI to win!')
    else:
        messagebox.showerror('TIE', 'It was a tie!')
def restart():
    global game
    game = [None] * 9
    canvas.delete('Del')
    draw()

#setup for GUI interface

root = Tk()
root.title('TIC-TAC-TOE (USING MINIMAX ALGORITHM)')
root.geometry('1200x1200')
compFirst = Button(root, text='PRESS THIS BUTTON TO LET PC OR AI GO FIRST', command=init)
compFirst.pack()
easy = IntVar()
Checkbutton(root, text='CLICK HERE FOR AI WHICH WILL NOT COME IN THE WAY OF YOU WINNING THE GAME', variable = easy).pack()
reset = Button(root, text='PRESS HERE TO RESTART THE GAME', command=restart)
reset.pack()
canvas = Canvas(root, width=900, height=900, bg='tan')
canvas.bind('<Button-1>', update)
canvas.create_line(0, 300, 900, 300, fill="black",width = 5)
canvas.create_line(0, 600, 900, 600,fill="black", width = 5)
canvas.create_line(300, 0, 300, 900,fill="black", width = 5)
canvas.create_line(600, 0, 600, 900,fill="black", width = 5)
canvas.pack()
root.mainloop()