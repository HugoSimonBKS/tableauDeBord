from tkinter import *
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Tableau de bord")

# On affiche le label dans la fenêtre
champ_label.pack()
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=3)
ligne_texte.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
