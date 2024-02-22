"""
Disappearing Text Writing App
"""
from tkinter import *

# ----------------------------    variables    -------------------------------- #

wait_time = 3
count_wait = 0
cpm_start = 1
time = 60
stop = 0
wpm = 0
cpm = 0
one = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def choose_minutes(value):
    global time
    minutes = int(value)
    time = minutes * 60
    timer_clock.config(text=time)


def star_timer(e):
    global time, one, cpm, wpm
    count = time
    if one == 1:
        text_input.delete(1.0, END)
        count_down(count)
        one += 1
    if e.char != ' ':
        cpm += 1
    else:
        wpm += 1
    wpm_speed.config(text=wpm)


def count_down(count):
    global time, cpm, wait_time, count_wait, cpm_start, stop
    count_wait += 1
    time = count - 1

    # user stopped typing?
    if count_wait == wait_time and cpm == cpm_start:
        time = 0
        stop = 1
        you_did_not_get_it()
    elif count_wait == wait_time and cpm > cpm_start:
        count_wait = 0
        cpm_start = cpm

    timer_clock.config(text=time)
    if time > 0:
        window.after(1000, count_down, time)
    else:
        if stop == 0:
            you_got_it()


def you_got_it():
    outcome_text = 'You got it!'
    color = '#2c2085'
    outcome(outcome_text, color)


def you_did_not_get_it():
    text_input.delete(1.0, END)
    outcome_text = 'Want to try again?'
    color = '#e3c30e'
    outcome(outcome_text, color)


def outcome(outcome_text, color):
    outcome_window = Toplevel()
    outcome_window.minsize(width=200, height=200)
    outcome_window.title("Outcome!")
    outcome_window.configure(bg='white')
    outcome_window.config(padx=80, pady=80)  # padding
    outcome_label = Label(outcome_window, text=outcome_text, font=('Montserrat', 18, 'bold'), bg='white',
                          fg=color, wraplength=300)
    outcome_label.grid(column=1, row=1)
    again = Button(outcome_window, text='Try again', height=1, width=8, command=lambda: try_again(outcome_window),
                   borderwidth=2, bg='#4281f5', font=('Montserrat', 14, 'bold'))
    again.grid(column=1, row=2, padx=5,  pady=5,)


def try_again(outcome_window):
    global time, wpm, cpm, one, count_wait, cpm_start, stop
    outcome_window.destroy()
    value_inside.set("Minutes")
    count_wait = 0
    cpm_start = 1
    stop = 0
    time = 60
    wpm = 0
    cpm = 0
    one = 1
    timer_clock.config(text=time)
    wpm_speed.config(text=wpm)
    text_input.delete(1.0, END)
    text_input.insert(1.0, 'start typing...')
    text_input.focus()
    text_input.bind("<Key>", star_timer)


# ---------------------------- UI SETUP ------------------------------- #
# creating a window
window = Tk()
window.title("Disappearing text writing app")
window.minsize(width=600, height=600)
window.configure(bg='white')
window.config(padx=100, pady=100)  # padding

# Labels
title_label = Label(text="The Most Dangerous Writing App", font=('Montserrat ', 40, 'bold'), bg='white')
title_label.grid(column=0, columnspan=5, row=0)
# subtitle label
subtitle_label = Label(text='Don’t stop writing, or all progress will be lost.', font=('Montserrat ', 20, 'bold'),
                       bg='white')
subtitle_label.grid(column=0, columnspan=5, row=1)
# time label
time_label = Label(text="seconds", font=('Montserrat', 12, 'bold'), bg='white')
time_label.grid(column=1, row=3)
# word per minute
wpm_label = Label(text="words", font=('Montserrat', 12, 'bold'), bg='white')
wpm_label.grid(column=2, row=3)

# Text Box (Text Box Widgets)
text_input = Text(window, width=60, height=10, font=('Montserrat', 18, 'normal'), bg='white', bd=0)
text_input.insert(1.0, 'start typing...')
text_input.focus()
text_input.grid(column=0, columnspan=5, row=4)
text_input.bind("<Key>", star_timer)

# label results
# time clock
timer_clock = Label(text=f'{time}', font=('Montserrat', 14, 'bold'), bg='white')
timer_clock.grid(column=1, row=2)
# word per minute
wpm_speed = Label(text=f'{wpm}', font=('Montserrat', 14, 'bold'), bg='white')
wpm_speed.grid(column=2, row=2)

# menu button
options_list = ['1', '3', '5', '10']
value_inside = StringVar(window)
# Set the default value of the variable
value_inside.set("Minutes")
minutes_menu = OptionMenu(window, value_inside, *options_list, command=choose_minutes)
minutes_menu.grid(column=3, row=2, rowspan=2)


window.mainloop()
