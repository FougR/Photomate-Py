import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import methods as pm
import mysql.connector as mysql

db = mysql.connect(
        host="localhost",
        user="root",
        password="eric",
        database="photomate")

cursor = db.cursor()

pseudo_Entry = None
mdp_Entry = None
mdp2_Entry = None
login_win = None
home_win = None
post_win = None
me_statut = None
me_win = None
post_statut = None
desc_Entry = None
friend_win = None


def me():
    global home_win
    global me_statut
    global me_win
    me_statut = "Running"
    
    home_win.destroy()
    me_win = tk.Tk()
    canvas = tk.Canvas(me_win, width=600, height=300)
    canvas.grid(columnspan=3, rowspan=3)

    cursor.execute(f"select * from comptes where pseudo ='{pm.pseudonyme}';")
    reqResult = cursor.fetchall()
    pseudo = str(reqResult[0][1])

    pseudo_label = tk.Label(me_win, text=pseudo, font="Raleway", height=2, width=15)
    home_btn = tk.Button(me_win, text="Home", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=home)
    friend_btn = tk.Button(me_win, text="Friends", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    param_btn = tk.Button(me_win, text="Me", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    param_btn.grid(column=2, row=3)
    home_btn.grid(column=0, row=3)
    friend_btn.grid(column=1, row=3)
    pseudo_label.grid(column=1, row=1)

def post_sql():
    global desc_Entry
    
    desc = desc_Entry.get()
    pm.post(desc)
    home()
    

def friend():
    global home_win
    global friend_win
    global cusor
    
    home_win.destroy()
    friend_win = tk.Tk()
    canvas = tk.Canvas(post_win, width=600, height=300)
    canvas.grid(columnspan=3, rowspan=4)
    
    cursor.execute(f"select * from amis where user_1 = {pm.id};")
    reqResult = cursor.fetchall()
    id_friend = reqResult[0][2]
    cursor.execute(f"select pseudo from comptes where user_id = {id_friend};")
    reqResult = cursor.fetchall()
    pseudo_friend = reqResult[0][0]
    print(pseudo_friend)
    
    friend_label = tk.Label(friend_win, text="Vous êtes amis avec :", font="Raleway", height=2, width=25)
    friends_label = tk.Label(friend_win, text=pseudo_friend, font="Raleway", height=2, width=10)
    post_btn = tk.Button(friend_win, text="Post", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=post)
    home_btn = tk.Button(friend_win, text="Home", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    friend_btn = tk.Button(friend_win, text="Friends", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    user_btn = tk.Button(friend_win, text="Me", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=me)
    user_btn.grid(column=2, row=3)
    friends_label.grid(column=0, row=1)
    post_btn.grid(column=2, row=0)
    friend_label.grid(column=0, row=0)
    home_btn.grid(column=0, row=3)
    friend_btn.grid(column=1, row=3)

def post():
    global post_win
    global home_win
    global post_statut
    global desc_Entry
    post_statut = "Running"
    home_win.destroy()
    post_win = tk.Tk()
    canvas = tk.Canvas(post_win, width=600, height=300)
    canvas.grid(columnspan=2, rowspan=3)
    
    browse_btn = tk.Button(post_win, text="Browse", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=post_sql)
    desc_Label = tk.Label(post_win, text="Description ?", font="Raleway", height=2, width=10)
    desc_Entry = tk.Entry(post_win, width=20)
    return_btn = tk.Button(post_win, text="Return", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=home)
        
    desc_Label.grid(column=1, row=0)
    desc_Entry.grid(column=1, row=1)
    return_btn.grid(column=0, row=2)
    browse_btn.grid(column=2, row=2)
    
    post_win.mainloop()
    
def home():
    global cursor
    global home_win
    global post_statut
    global me_win
    global post_win
    global me_statut
    
    if post_statut == "Running":
        post_statut = None
        post_win.destroy()
    elif me_statut == "Running":
        me_win.destroy()
        me_statut = None
    
    cursor.execute(f"select post_id from images;")
    post_ids = cursor.fetchall()
    
    posts_nbr = len(post_ids)
    
    home_win = tk.Tk()
    canvas = tk.Canvas(home_win, width=600, height=300)
    canvas.grid(columnspan=posts_nbr+3, rowspan=posts_nbr+3)

    post_btn = tk.Button(home_win, text="Post", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=post)
    home_btn = tk.Button(home_win, text="Home", font="Raleway", bg="#20bebe", fg="white", height=2, width=10)
    friend_btn = tk.Button(home_win, text="Friends", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=friend)
    user_btn = tk.Button(home_win, text="Me", font="Raleway", bg="#20bebe", fg="white", height=2, width=10, command=me)
    user_btn.grid(column=posts_nbr+2, row=3)
    post_btn.grid(column=posts_nbr+2, row=0)
    home_btn.grid(column=posts_nbr+0, row=3)
    friend_btn.grid(column=posts_nbr+1, row=3)

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