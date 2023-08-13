from tkinter import *
from buttons import Buttons
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Reps = 0
marks = ""
ResetPressed = False


window = Tk()
window.title("Pomodora App")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"Python_Course\Day 28\Pomodora App\tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

# Timer Label

TimerLabel = Label(text="Timer",font=(FONT_NAME,25,"bold"),fg=GREEN)
TimerLabel.grid(row=1,column=2)
TimerLabel.config(bg=YELLOW)
TimerLabel.config(borderwidth=0)


def CountRepsAndStart():
    global Reps
    global marks
    Reps += 1
    if Reps%2 == 0:
        marks += "✔️"
        CheckMarks.config(text=marks)
    if Reps%8 == 0:
        count = LONG_BREAK_MIN*60
        TimerLabel.config(text="Break", fg=RED)
        count_down(count)
    elif Reps%2 == 0:
        count = SHORT_BREAK_MIN*60
        TimerLabel.config(text="Break", fg=PINK)
        count_down(count)
    else:
        count = WORK_MIN*60
        TimerLabel.config(text="Work", fg=GREEN)
        count_down(count)


def count_down(count):
    global ResetPressed
    if ResetPressed == True:
        count = 0
        ResetPressed = False
    minute = math.floor(count/60)
    seconds = count - minute*60 
    if minute < 10:
        minute = f"0{minute}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text = f"{minute}:{seconds}")
    if count > 0:
        window.after(1,count_down
,count - 1)
    else:
        CountRepsAndStart()

# Buttons

# 1. Start Button

def StartTimer():
    CountRepsAndStart()

Start = Buttons("Start")
Start.grid(row=3, column=1)
Start.config(width=6,command=StartTimer)



#2 Reset Button

def ResetPressed():
    global Reps 
    global marks
    global ResetPressed
    Reps = 0
    ResetPressed = True
    marks = ""
    CheckMarks.config(text=marks)
    


Reset = Buttons("Reset")
Reset.grid(row=3,column=3)
Reset.config(width=6,command=ResetPressed)


# CheckMarkLabel\

CheckMarks = Label(text = marks, fg=GREEN, bg=YELLOW, borderwidth=0)
CheckMarks.grid(row=4,column=2)

window.mainloop()
