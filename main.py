from tkinter import *
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
CHECK_MARK = "✅"
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_button_clicked():
    global reps, timer
    window.after_cancel(timer)

    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

    timer_lab.config(text=f"Timer", fg=GREEN)
    timer_lab.grid(column=1, row=0)

    check_mark_lab.config(text="")
    check_mark_lab.grid(column=1, row=3)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button_clicked():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # 8
        timer_lab.config(text=f"Rest", fg=RED)
        timer_lab.grid(column=1, row=0)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        # 2, 4, 6
        timer_lab.config(text=f"Rest", fg=PINK)
        timer_lab.grid(column=1, row=0)
        count_down(short_break_sec)
    else:
        # 1, 3, 5, 7
        timer_lab.config(text=f"Work", fg=GREEN)
        timer_lab.grid(column=1, row=0)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:

        check_mark_lab.config(text=CHECK_MARK*int(math.floor(reps/2)))
        check_mark_lab.grid(column=1, row=3)
        start_button_clicked()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadoro")
window.config(padx=100, pady=50, bg=YELLOW)
# labels
check_mark_lab = Label(font=("Arial", 20, "bold"), fg=GREEN, bg=YELLOW)
check_mark_lab.grid(column=1, row=3)
timer_lab = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
timer_lab.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# buttons
start_button = Button(text="Start", command=start_button_clicked, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_button_clicked, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
