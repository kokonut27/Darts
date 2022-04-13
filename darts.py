from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import Button
from tkinter import Text
import time
import os
from replit import db


def show_board():
  board = None
  messagebox.showinfo("Leaderboard", board)

score = 0
darts = 10
direction = 3
xvel = 0

def moveDart(event):
  global xvel, direction
  xvel = 7
  direction = 0

tk = Tk()
canvas = Canvas(tk, width = 600, height = 300)
canvas.pack()


player = canvas.create_polygon(10, 148, 30, 148, 30, 146, 35, 149, 30, 152, 30, 150, 10, 150)
target = canvas.create_polygon(520, 118, 530, 118, 530, 178, 520, 178)


titleFont = font.Font(family = "Times", size = 18, weight = "bold")
scoreFont = font.Font(family = "Times", size = 13)


title = canvas.create_text(300, 20, text = "DARTS", font = titleFont)
scoreDisplay = canvas.create_text(100, 20, text = f"Score: {score}", font = scoreFont)
dartsLeft = canvas.create_text(500,20, text = f"Darts Left: {darts}", font = scoreFont)


def cheat(event):
  global score
  if event.keysym == "w":
    score+=1000
    canvas.itemconfig(scoreDisplay, text = f"Score: {score}", font = scoreFont)

canvas.bind_all("<Key>", moveDart)
canvas.bind_all("<KeyPress-w>", cheat)

btn = Button(tk, text = 'Leaderboard', command = show_board)
btn.pack()

while True:
  canvas.move(player,xvel,direction)
  pos = canvas.coords(player)
  if pos[0]>500:
    dartcenter = pos[1]+1
    points = int(max([0,30-abs(148-dartcenter)]))
    score += points
    darts -= 1
    canvas.itemconfig(scoreDisplay, text = f"Score: {score}", font = scoreFont)
    canvas.itemconfig(dartsLeft, text = f"Darts Left: {darts}", font = scoreFont)
    direction = 2
    xvel = 0
    if darts == 0:
      gameOver = canvas.create_text(300,150, text="GAME OVER", font = titleFont)
      finalScore = canvas.create_text(300,180, text = f"Your score was: {score}", font = scoreFont)
      add_leader(os.environ["REPL_OWNER"], score)
      tk.update()
      time.sleep(3)
      break
    canvas.move(player, -490,0)
  if (pos[1]>208) or(pos[1]<88):
    direction *= -1
  time.sleep(0.01)
  tk.update()

tk.destroy()