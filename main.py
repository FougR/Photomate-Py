# pm help : pour connaître les commandes

import methods as pm

running = True
while running == True:
    action = input("$ ")

    if action == "pm quit":
        running = False
    elif action.startswith("pm signup"):
        args = action.split("-")
        if len(args) == 4:
            pm.signup(args[1].rstrip(), args[2].rstrip(), args[3].rstrip())
        else: print("pm signup -<pseudo> -<mdp> -<confirmMdp>")
    elif action.startswith("pm login"):
        args = action.split("-")
        if len(args) == 3:
            pm.login(args[1], args[2])
        else: print("pm login -<pseudo> -<mdp>")
    elif action.startswith("pm post"):
        args = action.split("-")
        if len(args) == 2:
            pm.post(args[1])
        else: print("pm post -<url>")
    elif action == "pm friendlink -g":
        pm.friendlink_generation()
    elif action.startswith("pm friendlink -a"):
        args = action.split("-")
        if len(args) == 4:
            pm.friendlink(args[3])
        else: print("pm friendlink help")
    elif action == ("pm friendlink help"):
        print("pm friendlink -g : génère un lien d'amitié à envoyer à votre ami.\npm friendlink -a -<link> : permet d'ajouter votre ami via un lien d'amitié.")
    elif action.startswith("pm pseudo-change"):
        args = action.split("-")
        if len(args) == 3:
            pm.pseudo_change(args[2])
        else: print("pm pseudo-change -<newPseudo>")
    elif action.startswith("pm password-change"):
        args = action.split("-")
        if len(args) == 3:
            pm.mdp_change(args[2])
        else: print("pm password-change -<newMdp>")
    elif action == "pm help":
        print("pm quit : quitte le programme.\npm signup -<pseudo> -<mdp> -<confirmMdp> : permet de créer un compte.\npm login -<pseudo> -<mdp> : permet de se connecter à un compte.\npm post -<url> : permet de poster une photo.\npm friendlink help : aide pour la commande pm friendlink")
