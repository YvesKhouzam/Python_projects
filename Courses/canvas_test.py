import json
import tkinter as tk
from tkinter import BOTH

# Setup de la fenêtre
root = tk.Tk()
# root.geometry("900x200")
root.update_idletasks()
root_width = root.winfo_width()
root_heiht = root.winfo_height()
print(root_width, root_heiht)
root.title("Quiz")
root.iconphoto(False, tk.PhotoImage(file="quiz.png"))
# root.resizable(0, 0)
# root.config(bg="#123456")

# Defining the frames
left_frame = tk.Frame(root, bg="red", width=300, height=500)
center_frame = tk.LabelFrame(root, bg="#123456")
right_frame = tk.Frame(root, bg="green")

# Packing the frames
left_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)  # .grid(row=0, column=0)
center_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)  # .grid(row=0, column=1)
right_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)  # .grid(row=0, column=2)

root.update_idletasks()
print(left_frame.winfo_width(), center_frame.winfo_width(), left_frame.winfo_width())

root.bind('<Return>', check_answer)

root.mainloop()

# TODO: Dessiner la barre de fraction pour le pointage + encadrer la légende
# TODO: Texte plus gros, en couleur(?) - Bande en couleur premier tier et 3e tier
# TODO: Mettre une image en fond d'écran
# TODO: demander prénom et ajouter Bravo{prénom}
# TODO: animation ou image(main hight five) avec un son (applaudissement)
