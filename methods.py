import mysql.connector as mysql

db = mysql.connect(
        host="localhost",
        user="root",
        password="",
        database="photomate")

cursor = db.cursor()
pseudonyme = None

def login(pseudo, mdp):
    global pseudonyme
    cursor.execute('Select * from comptes where pseudo="'+pseudo+'"')
    resultReq = cursor.fetchall()
    if len(resultReq) != 0:
        if resultReq[0][2] == mdp:
            print("Vous êtes bien connecté sous le pseudo de "+resultReq[0][1])
            pseudonyme = pseudo
        else:
            print("Mauvais Mot de Passe.")
    else:
        print("Mauvais Pseudo.")

def signup(pseudo, mdp, mdp2):
    if mdp == mdp2:
        cursor.execute('insert into comptes (pseudo, mdp) values("'+pseudo+'","'+mdp+'");')
        print("Le compte a bien été créé.")
    else:
        print("Les mots de passe ne correspondent pas.")

def post(url):
    global pseudonyme
    if pseudonyme != None:
        cursor.execute(f'select user_id from comptes where pseudo = "{pseudonyme}";')
        resultReq = cursor.fetchall()
        cursor.execute(f"insert into images (author_id, post_img) values({resultReq[0][0]}, '{url}');")
        print("L'image a bien été postée.")
    else: print("Il faut être connecté pour pouvoir utiliser cette fonctionalité.")

def friendlink_generation():
    global pseudonyme
    if pseudonyme != None:
        cursor.execute(f'select user_id from comptes where pseudo = "{pseudonyme}";')
        resultReq = cursor.fetchall()
        print(f"Votre lien d'amitié : photomate/friendlink/user-{resultReq[0][0]}")
    else: print("Il faut être connecté pour pouvoir utiliser cette fonctionalité.")

def friendlink(friend_id):
    global pseudonyme
    if pseudonyme != None:
        cursor.execute(f'select user_id from comptes where pseudo = "{pseudonyme}";')
        resultReq = cursor.fetchall()
        cursor.execute(f"insert into amis (user_1, user_2) values({resultReq[0][0]}, {friend_id});")
        cursor.execute(f'select pseudo from comptes where user_id = "{friend_id}";')
        resultReq = cursor.fetchall()
        print(f"Vous êtes maintenant ami avec {resultReq[0][0]}.")
    else: print("Il faut être connecté pour pouvoir utiliser cette fonctionalité.")

def pseudo_change(new_pseudo):
    global pseudonyme
    if pseudonyme != None:
        cursor.execute(f'update comptes set pseudo = "{new_pseudo}" where pseudo = "{pseudonyme}";')
        print("Le pseudo a bien été modifié.")
    else: print("Il faut être connecté pour pouvoir utiliser cette fonctionalité.")

def mdp_change(new_mdp):
    global pseudonyme
    if pseudonyme != None:
        cursor.execute(f'update comptes set mdp = "{new_mdp}" where pseudo = "{pseudonyme}";')
        print("Le mot de passe a bien été modifié.")
    else: print("Il faut être connecté pour pouvoir utiliser cette fonctionalité.")