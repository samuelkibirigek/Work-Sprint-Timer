from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Work Sprint Timer")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg="black", bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


def start_timer():
    work_sprint = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    if reps in (1, 3, 5, 7):
        count_down(work_sprint)
        timer_label.config(text="WORK", fg=GREEN)
        print("work sprint")
    elif reps in (2, 4, 6):
        count_down(short_break)
        timer_label.config(text="SHORT BREAK", fg=PINK)
        print("short break")
    elif reps == 8:
        count_down(long_break)
        timer_label.config(text="LONG BREAK", fg=RED)
        print("long break")


def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    global timer
    if count > 0:
        if seconds < 10:
            seconds = f"0{seconds}"
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        timer = canvas.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps == 2:
            ticks.config(text="✔", fg="green", font=(FONT_NAME, 15, "bold"), bg=YELLOW)
        elif reps == 4:
            ticks.config(text="✔✔", fg="green", font=(FONT_NAME, 15, "bold"), bg=YELLOW)
        elif reps == 6:
            ticks.config(text="✔✔✔", fg="green", font=(FONT_NAME, 15, "bold"), bg=YELLOW)
        elif reps == 8:
            ticks.config(text="✔✔✔✔", fg="green", font=(FONT_NAME, 15, "bold"), bg=YELLOW)


def reset():
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    ticks.config(text="")
    global reps
    reps = 0


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

ticks = Label(text="", fg="green", font=(FONT_NAME, 15, "bold"), bg=YELLOW)
ticks.grid(column=1, row=3)


window.mainloop()


