import json
import tkinter as tk
from tkinter import BOTH, Canvas
from winsound import *

# Setup de la fenêtre
root = tk.Tk()
root.geometry("1000x300")
root.update_idletasks()
root_width = root.winfo_width()
root_height = root.winfo_height()
root.title("Quiz")
root.iconphoto(False, tk.PhotoImage(file="quiz.png"))
# root.resizable(0, 0)
# root.config(bg="#123456")


# Retourne une liste généréée à partir d'un json selon une clé
# Le .json a été créé à partir d'un code dans "genere_json"
def read_json(path, key):
    values = []
    with open(path) as q:
        data = json.load(q)
        for entry in data:
            values.append(entry[key])
        return values


# Génère une liste des questions et une liste des réponses
questions = read_json("questions_answers.json", "question")
answers = read_json("questions_answers.json", "answer")

nbr_questions = len(questions)
question = tk.StringVar()
question_no = 0
question.set(questions[question_no])
guess = tk.StringVar()
message = tk.StringVar()
score = tk.IntVar()
total = tk.IntVar()
attempts = 0
your_name = ""


def play(file):
    return PlaySound(file, SND_FILENAME)


def poser_question():
    global nbr_questions, question_no
    question_no += 1
    nbr_questions -= 1
    question.set(questions[question_no])


def msg_final():
    if int(score.get()) > ((60 / 100) * total.get()):
        message.set("Bravo " + your_name + ", tu as réussi! :) \n Tu as eu " + str(
            int(score.get() / total.get() * 100)) + " %.")
    else:
        message.set(
            your_name + " tu devrais réviser! :( \n Tu as eu " + str(int(score.get() / total.get() * 100)) + " %.")
    validate.config(state=tk.DISABLED)
    root.bind('<Return>', '')


def check_answer(event=None):
    global question_no, attempts, your_name
    attempts += 1
    message_label.config(font=("courier", 14))
    if question_no == 0:
        your_name = guess.get()
        message_label.config(font=("courier", 22))
        message.set("Bonjour " + str(your_name) + "! :)")
        guess.set("")
        poser_question()
        attempts = 0
    elif (guess.get()).lower() == answers[question_no].lower():  # Si bonne réponse
        message.set("Bonne réponse!")
        play("applause7.wav")
        guess.set("")
        score.set(score.get() + 4 - attempts)
        total.set(total.get() + 3)
        if nbr_questions > 1:
            poser_question()
            attempts = 0
        else:  # Il ne reste plus de questions
            msg_final()
    else:  # Si mauvaise réponse, il reste 1 ou 2 essais
        play("boo3.wav")
        if attempts < 2:
            message.set("Mauvaise réponse! \n Essaie encore, il te reste " + str(3 - attempts) + " essais")
            guess.set("")
        elif attempts == 2:
            message.set("Mauvaise réponse! \n Essaie encore, il te reste un dernier essai!")
            guess.set("")
        else:
            message.set("La bonne réponse est: " + answers[question_no])
            guess.set("")
            total.set(total.get() + 3)
            if nbr_questions > 1:
                poser_question()
                attempts = 0
            else:  # Il ne reste plus de questions
                msg_final()


# Defining the frames
left_frame = tk.Frame(root, bg="red")
center_frame = tk.LabelFrame(root, bg="#123456")
right_frame = tk.Frame(root, bg="green")

# Packing the frames
left_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)
center_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)
right_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)

# Content - Left Frame
points_frame = tk.LabelFrame(left_frame, text="Pointage", bg="red", fg="white")
points_frame.pack(pady=75)
tk.Label(points_frame, text="1er essai = 3 pts", bg="red", fg="white", font=("", 10, "bold"), width=15, height=2).pack()
tk.Label(points_frame, text="2e  essai = 2 pts", bg="red", fg="white", font=("", 10, "bold"), width=15, height=2).pack()
tk.Label(points_frame, text="3e  essai = 1 pt", bg="red", fg="white", font=("", 10, "bold"), width=15, height=2).pack()

# Content - Center Frame
tk.Label(center_frame, text="Me connais-tu?", font=("Courier", 22), bg="#123456", fg="white").pack(pady=10)
tk.Label(center_frame, textvariable=question, bg="#123456", fg="white", font=("Courrier", 14)).pack(pady=10)
tk.Entry(center_frame, textvariable=guess).pack(pady=10)
validate = tk.Button(center_frame, text="Valide ta réponse", state=tk.ACTIVE, command=check_answer)
validate.pack(pady=10, padx=200)
message_label = tk.Label(center_frame, textvariable=message, bg="#123456", fg="yellow")
message_label.pack(pady=10)

# Content - Right Frame
score_frame = tk.Frame(right_frame, bg="green")
score_frame.pack(pady=75)
tk.Label(score_frame, text="Ton pointage", bg="green", font=("Courier", 14)).pack(pady=5)
tk.Label(score_frame, textvariable=score, bg="green", font=("Courier", 18, "bold")).pack(pady=5)
w = Canvas(score_frame, width=20, height=0, bd=0, highlightthickness=0)
w.pack()
w.create_line(0, 0, 200, 0, fill="black")
tk.Label(score_frame, textvariable=total, bg="green", font=("Courier", 18, "bold")).pack(pady=5)

root.bind('<Return>', check_answer)

root.mainloop()

# TODO: Dessiner la barre de fraction pour le pointage - Done!
# TODO: Encadrer et centrer la légende - Done !
# TODO: Texte plus gros, en couleur(?) - Bande en couleur premier tier et 3e tier - Done!
# TODO: demander prénom et ajouter Bravo{prénom} - Done!
#  avec un son (applaudissement ou boooo) - Done!
# TODO: Mettre une image en fond d'écran
# TODO: animation ou image(main hight five)
# TODO: Si la réponse est vide: "Écrit quelque chose!"
# TODO: différents type de réponses
#  : Réponse courte
#  : Choix de réponse
#  : Vrai ou faux


