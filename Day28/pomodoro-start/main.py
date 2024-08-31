import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def resetTime():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timerCount.config(text='Timer')
    checkmark.config(text='')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer(): 
    global reps
    reps += 1
    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreaksec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(longBreaksec)
        timerCount.config(text='Long Break Time', fg=RED)
    elif reps % 2 == 0: 
        count_down(shortBreakSec)
        timerCount.config(text='Short Break Time', fg=PINK)
    else:
        count_down(workSec)
        timerCount.config(text='Work Time',fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f'{minutes:02d}:{seconds:02d}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        starttimer()
        mark = ""
        workSession = math.floor(reps/2)
        for _ in range(workSession):
            mark += '✓'

        checkmark.config(text=mark)
        
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro')
window.minsize(700,500)
window.config(padx=250, pady=138, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

image = tkinter.PhotoImage(file="./100-Day-of-coding-python/Day28/pomodoro-start/tomato.png") 


timerCount = tkinter.Label(text="Timer", font=(FONT_NAME, 32, 'bold'),fg=GREEN, bg=YELLOW, highlightthickness=0)
timerCount.grid(column=1,row=0)
timerCount.config(pady=10)

canvas.create_image(100,112, image=image)
timer_text = canvas.create_text(100, 132, text='00:00', fill='white', font=(FONT_NAME,  32, 'bold'))
canvas.grid(column=1,row=1)

start = tkinter.Button(text='start', width=10, command=starttimer)
start.grid(column=0,row=2)

checkmark = tkinter.Label( font=(FONT_NAME, 36), fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark.grid(column=1,row=3)

reset = tkinter.Button(text='Reset', width=10, command=resetTime)
reset.grid(column=2,row=2)


window.mainloop()   