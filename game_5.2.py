# --------------------------------COURSEWORK 2 v5.2----------------------------
# Name of the game: CLAW MACHINE - catch for the wing
# Author: Ziyang Yu
# Last edited date: 13/12/2019     final version
# -----------------------------------------------------------------------------
# catch for the wing (win) - use of homophone, not a typo!
# CHEAT CODES
# <Control_L>w   You become the top 1
# <Control_L>g  Remove all the bombs (apply before start)
# <Control_L>f  Fake your score to 1000
# -----------------------------------------------------------------------------

from tkinter import *
from os import path
import sys
import os
import random


def clear_instrct():
    instruction_button.config(state="normal")  # Change the state back
    canvas.delete(instrct)
    ok_button.destroy()


# Displays the guidance on how to play the game
def game_instrct():
    global instrct, ok_button
    # Button cannot be pressed twice
    instruction_button.config(state=DISABLED)
    instrct = canvas.create_image(0, 50, image=instrct_img, anchor=NW)
    # Removes the instrct when "OKAY" button is clicked
    ok_button = Button(text="OKAY", command=clear_instrct)
    ok_button.place(x=155, y=450)


def leader_record():
    if path.exists("leaderrecord.txt") is False:
        leader_file = open("leaderrecord.txt", "a")
        for i in range(3):
            leader_file.write("None\n0\n")
        leader_file.close()

    leader_record = []
    leader_file = open("leaderrecord.txt", "r")
    for line in leader_file:
        line = line.rstrip()
        leader_record.append(line)

    leader_score = []
    leader_name = []

    leader_record.append(player)
    leader_record.append(score)

    for x in range(0, len(leader_record)):
        if x % 2 == 1:
            leader_score.append(int(leader_record[x]))
        else:
            leader_name.append(leader_record[x])

    leader_file = open("leaderrecord.txt", "w")
    top_count = 3

    while top_count > 0:
        top_count -= 1
        top_score = max(leader_score)
        i = leader_score.index(top_score)

        top_list.append(leader_name[i])
        top_list.append(top_score)
        leader_file.write(str(leader_name[i])+"\n")
        leader_file.write(str(top_score)+"\n")
        leader_name.remove(leader_name[i])
        leader_score.remove(top_score)


def save():
    record_file = open("player_record.txt", "w")
    record_file.write(str(score)+"\n")


def load():
    global score, score_text

    record_file = open("player_record.txt", "r")

    for record in record_file:
        record = record.rstrip()
        record_list.append(record)

    i = len(record_list) - 1
    score = record_list[i]
    loaded = "SCORE: " + score
    score = int(score)
    canvas.itemconfigure(score_text, text=loaded)


def restart_game():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def pause(event):
    global pause_state

    if pause_state == 0:
        pause_state = 1
        stop(claw)
        canvas.unbind("<Left>")
        canvas.unbind("<Right>")
        canvas.unbind("<Up>")
        canvas.unbind("<Down>")

    else:

        pause_state = 0
        return_game = canvas.create_text(600, 300, fill="black",
                                         font="Times 20 bold",
                                         text="BACK TO THE GAME...")
        window.after(1000, lambda: canvas.itemconfigure(return_game, text="3"))
        window.after(1500, lambda: canvas.itemconfigure(return_game, text="2"))
        window.after(1900, lambda: canvas.itemconfigure(return_game, text="1"))
        window.after(2200,
                     lambda: canvas.itemconfigure(return_game, text="GO!"))
        window.after(2500, lambda: canvas.delete(return_game))
        window.after(2500, lambda: canvas.bind("<Left>", left_key))
        window.after(2500, lambda: canvas.bind("<Right>", right_key))
        window.after(2500, lambda: canvas.bind("<Up>", up_key))
        window.after(2500, lambda: canvas.bind("<Down>", down_key))


def player_name():
    global name, entered, display, game_name
    # Catch for the wing image
    game_name = canvas.create_image(-50, -180, image=title, anchor=NW)
    display = canvas.create_text(600, 480, fill="#4d0000",
                                 font="Arial 15 bold",
                                 text="Heyyyyy, pls enter your name below" +
                                 " (or leave it blank, it's perfectly fine)")
    name = Entry(window, width=25)
    name.place(x=480, y=500)
    entered = Button(text="OK DONE", command=clear_text)
    entered.place(x=680, y=495)


def clear_text():
    global name, player
    entered.destroy()
    canvas.itemconfigure(game_name, image=game_bg)
    canvas.delete(display)
    player = name.get()
    name.destroy()
    display_menu()


def back():
    canvas.delete(board, design1, design2, design3, header)
    canvas.delete(display1, display2, display3, display4, display5, score_text)
    cancel_button.destroy()
    display_menu()


def boss_key(event):
    global working_state, slide

    if working_state == 0:
        working_state = 1
        slide = Toplevel()
        slide.title("PROJECT PRESENTATION")
        slide.geometry('%dx%d+%d+%d' % (ws, hs, 0, 0))
        show_slide = Label(slide, image=plan, height=hs, width=ws)
        show_slide.pack()
    else:
        working_state = 0
        slide.destroy()


def countdown1():

    stopclock = "GET READY FOR LEVEL 1: EASY !!!"
    clock = canvas.create_text(600, 300, fill="black", font="Times 20 bold",
                               text=stopclock)
    window.after(1000, lambda: canvas.itemconfigure(clock, text="3"))
    window.after(1500, lambda: canvas.itemconfigure(clock, text="2"))
    window.after(1900, lambda: canvas.itemconfigure(clock, text="1"))
    window.after(2200, lambda: canvas.itemconfigure(clock, text="GO!"))

    import_claw()

    window.after(2500, move_claw)
    window.after(2500, lambda: canvas.delete(clock))
    window.after(2500, start_game1)


def countdown2():
    stopclock = "GET READY FOR LEVEL 2: MEDIUM !!!"
    clock = canvas.create_text(600, 300, fill="black", font="Times 20 bold",
                               text=stopclock)
    window.after(500, lambda: canvas.itemconfigure(clock, text="3"))
    window.after(1000, lambda: canvas.itemconfigure(clock, text="2"))
    window.after(1500, lambda: canvas.itemconfigure(clock, text="1"))
    window.after(2000, lambda: canvas.itemconfigure(clock, text="GO!"))

    import_claw()

    window.after(2500, move_claw)
    window.after(2500, lambda: canvas.delete(clock))
    window.after(2500, start_game2)


def countdown3():
    stopclock = "GET READY FOR LEVEL 3: HARDEST !!!"
    clock = canvas.create_text(600, 300, fill="black", font="Times 20 bold",
                               text=stopclock)
    window.after(500, lambda: canvas.itemconfigure(clock, text="3"))
    window.after(1000, lambda: canvas.itemconfigure(clock, text="2"))
    window.after(1500, lambda: canvas.itemconfigure(clock, text="1"))
    window.after(2000, lambda: canvas.itemconfigure(clock, text="GO!"))

    import_claw()

    window.after(2500, move_claw)
    window.after(2500, lambda: canvas.delete(clock))
    window.after(2500, start_game3)


def player_score():
    global score

    score += 10
    txt = "SCORE: " + str(score)
    canvas.itemconfigure(score_text, text=txt)  # Update the score


def hit_by_bomb(c, b):
    if c[0] >= (b[0]) and (c[0]+98) <= (b[0]+275):
        if (c[1]+952) >= (b[1]) and (c[1]+952) <= (b[1]+236):
            leader_file = open("leaderrecord.txt", "a")
            leader_file.write(str(player)+"\n")
            leader_file.write(str(score)+"\n")
            return True
    return False


def caught_toy(c, t):
    if c[0] >= t[0] and (c[0]+98) <= (t[0]+117):
        if (c[1]+900) >= t[1] and (c[1]+900) <= (t[1]+500):
            return True
    return False


def move_claw():
    global claw_pos, claw_state
    claw_pos = canvas.coords(claw)
    if claw_pos[1] == -600.0:
        claw_state = 0  # State in use
        canvas.itemconfigure(claw, image=metalclaw)  # Claw back to normal

    # Controlling the claw movement
    if claw_pos[0] > width or claw_pos[0] < 0:
        if direction == "left":
            right_key(claw)
        elif direction == "right":
            left_key(claw)
    elif claw_pos[1] > (height-1050) or claw_pos[1] < -600:
        if direction == "up":
            down_key(claw)
        elif direction == "down":
            up_key(claw)

    if direction == "left":
        canvas.move(claw, -25, 0)
    elif direction == "right":
        canvas.move(claw, 25, 0)
    elif direction == "up":
        canvas.move(claw, 0, -25)
    elif direction == "down":
        canvas.move(claw, 0, 25)

    window.after(80, move_claw)


def import_claw():
    global claw
    claw = canvas.create_image(0, -600, image=metalclaw, anchor=NW)
    canvas.bind("p", pause)
    canvas.focus_set()


class import_bomb:

    def __init__(self):
        # Generates a random speed
        self.bomb = bomb
        self.speedx = random.randint(5, 10)
        self.speedy = random.randint(5, 15)
        self.active = True
        self.move_active()

    def bomb_update(self):
        canvas.move(self.bomb, self.speedx, self.speedy)
        bomb_pos = canvas.coords(self.bomb)
        # Collision with the wall
        if bomb_pos[0] >= (width-100) or bomb_pos[0] <= 0:
            self.speedx *= -1
        if bomb_pos[1] >= (height-100) or bomb_pos[1] <= 500:
            self.speedy *= -1
        if hit_by_bomb(claw_pos, bomb_pos):
            scoring = canvas.create_text(600, 300, fill="#4d0000",
                                         font="Times 20 italic bold",
                                         text="OOPS...")
            window.after(500, restart_game)

    def move_active(self):
        if self.active:
            self.bomb_update()
            window.after(5, self.move_active)


# Import all the toys
class import_toy:

    def __init__(self):
        # Generates the random speed for toy
        self.toy = toy
        self.speedx = random.randint(5, 10)
        self.speedy = random.randint(10, 15)
        self.active = True
        self.move_active()

    def toy_update(self):
        global claw_state
        canvas.move(self.toy, self.speedx, self.speedy)
        toy_pos = canvas.coords(self.toy)

        if toy_pos[0] >= (width-100) or toy_pos[0] <= 0:
            self.speedx *= -1
        if toy_pos[1] >= (height-100) or toy_pos[1] <= 500:
            self.speedy *= -1

        if claw_state == 0:
            if caught_toy(claw_pos, toy_pos):
                claw_state += 1
                canvas.itemconfigure(claw, image=caught_claw)
                up_key(claw)
                if claw_state == 1:
                    player_score()
                    scoring = canvas.create_text(600, 300, fill="black",
                                                 font="Times 20 italic bold",
                                                 text="SCORE +10")
                    window.after(600, lambda: canvas.delete(scoring))

    def move_active(self):
        if self.active:
            self.toy_update()
            window.after(1, self.move_active)


# To remove the buttons
def remove_buttons():
    canvas.delete(menu, shape)
    start_button1.destroy()
    start_button2.destroy()
    start_button3.destroy()
    leaderboard_button.destroy()
    quit_button.destroy()


# Goes to different levels
def start1():
    remove_buttons()
    countdown1()


def start2():
    remove_buttons()
    countdown2()


def start3():
    remove_buttons()
    countdown3()


# Start different levels
def start_game1():
    global toy, bomb, t_count, b_count

    while t_count > 0:
        t_count -= 1
        toy = canvas.create_image(random.randint(0, 900),
                                  random.randint(500, 900),
                                  image=chicken,
                                  anchor=NW)
        import_toy()

    while b_count > 2:
        b_count -= 1
        bomb = canvas.create_image(random.randint(0, 900),
                                   random.randint(500, 900),
                                   image=obstacle,
                                   anchor=NW)
        import_bomb()


def start_game2():
    global toy, bomb, t_count, b_count

    while t_count > 0:
        t_count -= 1
        toy = canvas.create_image(random.randint(0, 900),
                                  random.randint(500, 900),
                                  image=chicken,
                                  anchor=NW)
        import_toy()

    while b_count > 1:
        b_count -= 1
        bomb = canvas.create_image(random.randint(0, 900),
                                   random.randint(500, 900),
                                   image=obstacle,
                                   anchor=NW)
        import_bomb()


def start_game3():
    global toy, bomb, t_count, b_count

    while t_count > 0:
        t_count -= 1
        toy = canvas.create_image(random.randint(0, 900),
                                  random.randint(500, 900),
                                  image=chicken,
                                  anchor=NW)
        import_toy()

    while b_count >= 0:
        b_count -= 1
        bomb = canvas.create_image(random.randint(0, 900),
                                   random.randint(500, 900),
                                   image=obstacle,
                                   anchor=NW)
        import_bomb()


def leaderboard():
    global board, design1, design2, design3, header, cancel_button
    global display1, display2, display3, display4, display5, display6

    remove_buttons()  # Clear the background
    board = canvas.create_rectangle(350, 250, 850, 700, fill="#4d0000")
    design1 = canvas.create_rectangle(430, 260, 780, 330, fill="",
                                      outline="#FFD700")
    design2 = canvas.create_rectangle(420, 270, 770, 340, fill="",
                                      outline="#FFD700")
    design3 = canvas.create_image(325, 230, image=wing, anchor=NW)
    header = canvas.create_text(600, 300, fill="#ffe6e6", font="Times 30 bold",
                                text="LEADERBOARD")
    leader_record()  # Find the top 3
    # Goes back to the menu
    cancel_button = Button(text="OKAY", command=back)
    cancel_button.place(x=580, y=670)

    # Display top 3
    display1 = canvas.create_text(500, 400, fill="#ffe6e6",
                                  font="Times 40 bold", text="1. "+top_list[0])
    display2 = canvas.create_text(700, 400, fill="#ffe6e6",
                                  font="Times 40 bold", text=top_list[1])
    display3 = canvas.create_text(500, 480, fill="#ffe6e6",
                                  font="Times 40 bold", text="2. "+top_list[2])
    display4 = canvas.create_text(700, 480, fill="#ffe6e6",
                                  font="Times 40 bold", text=top_list[3])
    display5 = canvas.create_text(500, 560, fill="#ffe6e6",
                                  font="Times 40 bold", text="3. "+top_list[4])
    display6 = canvas.create_text(700, 560, fill="#ffe6e6",
                                  font="Times 40 bold", text=top_list[5])


# To quit the game
def end():
    window.destroy()


# Keys controlling movement of the claw
def stop(event):
    global direction
    direction = ""


def left_key(event):
    global direction
    direction = "left"


def right_key(event):
    global direction
    direction = "right"


def up_key(event):
    global direction
    direction = "up"


def down_key(event):
    global direction
    direction = "down"


# Display the menu
def display_menu():
    global player, name, score, score_text
    canvas.bind("<Left>", left_key)
    canvas.bind("<Right>", right_key)
    canvas.bind("<Up>", up_key)
    canvas.bind("<Down>", down_key)
    canvas.bind("<space>", stop)
    canvas.bind("<Control_L>w", cheatcode1)  # You become the top 1
    canvas.bind("<Control_L>g", cheatcode2)  # Remove all the bombs
    canvas.bind("<Control_L>f", cheatcode3)  # Fake your score to 1000

    canvas.focus_set()

    global menu, shape, start_button1, start_button2, start_button3
    global leaderboard_button, quit_button, score, score_text
    global instruction_button
    score = 0
    txt = "SCORE: " + str(score)
    score_text = canvas.create_text(90, 50, fill="black", font="Times 20 bold",
                                    text=txt)
    border = canvas.create_rectangle(0, 500, 2000, 490, fill="#4d0000",
                                     outline="#4d0000")
    shape = canvas.create_rectangle(380, 150, 800, 240, fill="black")
    menu = canvas.create_text(600, 200, fill="#ffe6e6", font="Arial 70 bold",
                              text="MENU")
    start_button1 = Button(canvas, image=level1_img, width="300", height="100",
                           command=start1)
    start_button1.place(x=450, y=250)
    start_button2 = Button(canvas, image=level2_img, width="300", height="100",
                           command=start2)
    start_button2.place(x=450, y=350)
    start_button3 = Button(canvas, image=level3_img, width="300", height="100",
                           command=start3)
    start_button3.place(x=450, y=450)
    leaderboard_button = Button(canvas, image=leaderboard_img, width="300",
                                height="100", command=leaderboard)
    leaderboard_button.place(x=450, y=550)
    quit_button = Button(canvas, image=quit_img, width="300", height="100",
                         command=end)
    quit_button.place(x=450, y=650)

    # Toplevel to create a instrct page
    instruction_button = Button(text="INSTRUCTION", command=game_instrct)
    instruction_button.place(x=0, y=0)
    # Save/add to saved list
    save_button = Button(text="SAVE", command=save)
    save_button.place(x=108, y=0)
    load_button = Button(text="LOAD", command=load)
    load_button.place(x=169, y=0)
    restart_button = Button(text="RESTART", command=restart_game)
    restart_button.place(x=231, y=0)
    quit2_button = Button(text="QUIT", command=end)
    quit2_button.place(x=313, y=0)


# Configure the window
def set_window_dimensions(w, h):
    global ws, hs
    window = Tk()
    window.title("CLAW MACHINE")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return window


# Cheat codes in use
def cheatcode1(event):
    leader_record()
    top_list[0] = player
    with open("leaderrecord.txt") as f:
        lines = f.readlines()
    lines[0] = lines[0] .replace(lines[0], (top_list[0]+"\n"))
    with open("leaderrecord.txt", "w") as g:
        for line in lines:
            g.write(line)
    print("CONGRAATS !! YOU ARE THE TOP 1 !!!")


def cheatcode2(event):
    global b_count
    cheat_txt2 = canvas.create_text(600, 100, fill="#4d0000",
                                    font="Times 20 bold",
                                    text="GUARANTEED WIN!!")
    window.after(1000,
                 lambda: canvas.itemconfigure(cheat_txt2,
                                              text="GUARANTEED SATISFACTION!"))
    b_count = -1
    window.after(2000, lambda: canvas.delete(cheat_txt2))


def cheatcode3(event):
    global score
    score = 1000
    cheat_txt3 = "SCORE: " + str(score)
    canvas.itemconfigure(score_text, text=cheat_txt3)

# States in use
working_state = 0
pause_state = 0
t_count = 3
b_count = 3
score = 0

# Set the background
width = 1200
height = 1000
window = set_window_dimensions(width, height)
canvas = Canvas(window, bg="#ffe6e6", width=width, height=height)
canvas.pack(expand=YES, fill=BOTH)

level1_img = PhotoImage(file="level1.png")  # Images for menu buttons and toys
level2_img = PhotoImage(file="level2.png")
level3_img = PhotoImage(file="level3.png")
leaderboard_img = PhotoImage(file="leaderboard.png")
quit_img = PhotoImage(file="quit.png")
chicken = PhotoImage(file="chicken.png")
obstacle = PhotoImage(file="bomb.png")
metalclaw = PhotoImage(file="claw.png")
caught_claw = PhotoImage(file="updated_claw.png")
plan = PhotoImage(file="plan.png")
title = PhotoImage(file="title.png")
wing = PhotoImage(file="wing.png")
instrct_img = PhotoImage(file="instruction.png")
game_bg = PhotoImage(file="wallpaper.png")
player_name()

canvas.bind_all("<Tab>", boss_key)
# You become the top 1
canvas.bind("<Control_L>w", cheatcode1)
# Has to be applied beforehand (remove all the bombs)
canvas.bind("<Control_L>g", cheatcode2)
# Fake your score to 1000
canvas.bind("<Control_L>f", cheatcode3)
canvas.focus_set()

# Lists in use
top_list = []
record_list = []

# Initial direction of the game
direction = "right"
canvas.pack()
window.mainloop()
