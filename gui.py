import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import methods as pm
import mysql.connector as mysql

db = mysql.connect(
        host="localhost",
        user="root",
        password="",
        database="photomate")

cursor = db.cursor()

pseudo_Entry = None
mdp_Entry = None
mdp2_Entry = None
login_win = None
home_win = None

def me():
    global home_win
    home_win.destroy()
    me_win = tk.Tk()
    canvas = tk.Canvas(me_win, width=600, height=300)
    canvas.grid(columnspan=3, rowspan=3)

    cursor.execute(f"select * from comptes where pseudo ='{pm.pseudonyme}';")
    reqResult = cursor.fetchall()
    pseudo = str(reqResult[0][1])

    pseudo_label = tk.Label(me_win, text=pseudo, font="Raleway", height=2, width=15)
    home_btn = tk.Button(me_win, text="Home", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    friend_btn = tk.Button(me_win, text="Friends", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    param_btn = tk.Button(me_win, text="Me", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    param_btn.grid(column=2, row=3)
    home_btn.grid(column=0, row=3)
    friend_btn.grid(column=1, row=3)
    pseudo_label.grid(column=1, row=1)

def home():
    global home_win
    home_win = tk.Tk()
    canvas = tk.Canvas(home_win, width=600, height=300)
    canvas.grid(columnspan=3, rowspan=3)

    post_btn = tk.Button(home_win, text="Post", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    home_btn = tk.Button(home_win, text="Home", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    friend_btn = tk.Button(home_win, text="Friends", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    user_btn = tk.Button(home_win, text="Me", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=me)
    user_btn.grid(column=2, row=3)
    post_btn.grid(column=2, row=0)
    home_btn.grid(column=0, row=3)
    friend_btn.grid(column=1, row=3)

    home_win.mainloop()

def login_sql():
    global pseudo_Entry
    global mdp_Entry
    global login_win
    pseudo = pseudo_Entry.get()
    mdp = mdp_Entry.get()
    pm.login(pseudo, mdp)
    if pm.pseudonyme != None:   
        login_win.destroy()
        home()

def signup_sql():
    global pseudo_Entry
    global mdp_Entry
    global mdp2_Entry
    global login_win
    pseudo = pseudo_Entry.get()
    mdp = mdp_Entry.get()
    mdp = mdp_Entry.get()
    pm.login(pseudo, mdp)
    login_win.destroy()
    home()

def login():
    global pseudo_Entry
    global mdp_Entry
    global root
    global login_win
    root.destroy()

    login_win = tk.Tk()
    canvas = tk.Canvas(login_win, width=600, height=300)
    canvas.grid(columnspan=1, rowspan=5)
    
    pseudo_txt = tk.Label(login_win, text="Pseudo ?", font="Raleway", height=2, width=10)
    pseudo_Entry = tk.Entry(login_win, width=20)
    mdp_txt = tk.Label(login_win, text="Mot de Passe ?", font="Raleway", height=2, width=15)
    mdp_Entry = tk.Entry(login_win, width=20)
    login_btn = tk.Button(login_win, text="Login", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=login_sql)
    
    pseudo_txt.grid(column=0, row=1)
    pseudo_Entry.grid(column=0, row=2)
    mdp_txt.grid(column=0, row=3)
    mdp_Entry.grid(column=0, row=4)
    login_btn.grid(column=0, row=5)

    login_win.mainloop()

def signup():
    global pseudo_Entry
    global mdp_Entry
    global mdp2_Entry
    global root
    global login_win
    root.destroy()

    login_win = tk.Tk()
    canvas = tk.Canvas(login_win, width=600, height=300)
    canvas.grid(columnspan=1, rowspan=7)
    
    pseudo_txt = tk.Label(login_win, text="Pseudo ?", font="Raleway", height=2, width=10)
    pseudo_Entry = tk.Entry(login_win, width=20)
    mdp_txt = tk.Label(login_win, text="Mot de Passe ?", font="Raleway", height=2, width=15)
    mdp_Entry = tk.Entry(login_win, width=20)
    mdp2_txt = tk.Label(login_win, text="Confirmez votre mot de passe ?", font="Raleway", height=2, width=25)
    mdp2_Entry = tk.Entry(login_win, width=30)
    signup_btn = tk.Button(login_win, text="Sign Up", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=signup_sql)
    
    pseudo_txt.grid(column=0, row=1)
    pseudo_Entry.grid(column=0, row=2)
    mdp_txt.grid(column=0, row=3)
    mdp_Entry.grid(column=0, row=4)
    mdp2_txt.grid(column=0, row=5)
    mdp2_Entry.grid(column=0, row=6)
    signup_btn.grid(column=0, row=7)

    login_win.mainloop()

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=1, rowspan=4)

login_btn = tk.Button(root, text="Login", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=login)
login_btn.grid(column=0, row=1)

signup_btn = tk.Button(root, text="Sign Up", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=signup)
signup_btn.grid(column=0, row=2)

root.mainloop()