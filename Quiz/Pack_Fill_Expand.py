import json
import tkinter as tk
from tkinter import BOTH

# Setup de la fenêtre
root = tk.Tk()
root.geometry("900x300")
root.update_idletasks()
root_width = root.winfo_width()
root_heiht = root.winfo_height()
print(root_width, root_heiht)
root.title("Quiz")
root.iconphoto(False, tk.PhotoImage(file="quiz.png"))
# root.resizable(0, 0)
# root.config(bg="#123456")

# Defining the frames
left_frame = tk.Frame(root, bg="red")
center_frame = tk.Frame(root, bg="#123456", width=300)
right_frame = tk.Frame(root, bg="green")

# Packing the frames
left_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)
center_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)
right_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)


# tk.Label(left_frame, text="dsfdfsf fdsffds fds ", bg="black").pack()

root.update_idletasks()
print(left_frame.winfo_width(), center_frame.winfo_width(), right_frame.winfo_width())

root.mainloop()

# TODO: Dessiner la barre de fraction pour le pointage + encadrer la légende
# TODO: Texte plus gros, en couleur(?) - Bande en couleur premier tier et 3e tier
# TODO: Mettre une image en fond d'écran
# TODO: demander prénom et ajouter Bravo{prénom}
# TODO: animation ou image(main hight five) avec un son (applaudissement)
