import json
import tkinter as tk
#from PIL import Image, ImageTk
from tkinter import BOTH, Canvas, font
from winsound import *

root = tk.Tk()
questionLabel = tk.StringVar()
guessLabel = tk.StringVar()
messageLabel = tk.StringVar()
validate = tk.Button()
score = tk.IntVar()
total = tk.IntVar()

# font = "georgia"
# font = "hellosmartie"
font = "kg happy"

# Retourne une liste généréée à partir d'un json selon une clé
# Le .json a été créé à partir d'un code dans "genere_json"
def read_json(path):
    values = []
    with open(path) as q:
        return json.load(q)        

def play(file):
    return PlaySound(file, SND_FILENAME)

def poser_question():
    global questionLabel, attempts, questionIndex
    
    attempts = 0

    if (questionIndex + 1) >= len(questionAnswerList):
        msg_final()
    else:
        questionIndex += 1
        questionLabel.set(questionAnswerList[questionIndex]["question"])
        guessLabel.set("")

def msg_final():
    global validate, messageLabel

    scoreAsNumber = score.get()
    totalAsNumber = total.get()
    ratio = scoreAsNumber / totalAsNumber if totalAsNumber > 0 else 0
    passingRatio = 0.6
    ratioAsString = str(int(ratio * 100))

    if ratio > passingRatio:
        messageLabel.set("Bravo " + userName + ", tu as réussi! :) \n Tu as eu " + ratioAsString + " %.")
    else:
        messageLabel.set(
            userName + " tu devrais réviser! :( \n Tu as eu " + ratioAsString + " %.")

    validate.config(state=tk.DISABLED)  # does not seems to work
    root.bind('<Return>', '')

def check_answer(event=None):    
    global questionIndex, attempts, userName
    attempts += 1
    maxAttempts = 3 # replace with questionAnswerList[questionIndex]["maxAttempts"].get() eventually
   
    answer = questionAnswerList[questionIndex]["answer"]

    if questionIndex == 0:  # Pour avoir le nom du joueur
        userName = guessLabel.get()
        messageLabel.set("Bonjour " + str(userName) + "! :)")       
        poser_question()
    elif (guessLabel.get()).lower() == answer.lower():  # Si bonne réponse
        messageLabel.set("Bonne réponse!")
        guessLabel.set("")
        score.set(score.get() + 4 - attempts)
        total.set(total.get() + 3)
        # play("applause7.wav")
        if len(questionAnswerList) > 1:
            poser_question()
        else:  # Il ne reste plus de questions
            msg_final()
    else:  # Si mauvaise réponse, il reste 1 ou 2 essais
        # play("boo3.wav")
        if attempts == maxAttempts - 1:
            messageLabel.set("Mauvaise réponse! \n Essaie encore, il te reste un dernier essai!")
            guessLabel.set("")            
        elif attempts < maxAttempts:
            messageLabel.set("Mauvaise réponse! \n Essaie encore, il te reste " + str(maxAttempts - attempts) + " essais")
            guessLabel.set("")        
        else:
            messageLabel.set("La bonne réponse est: " + answer)
            total.set(total.get() + 3)
            poser_question()

def setupUI():
    # Setup de la fenêtre
    
    root.geometry("1100x400")
    root.update_idletasks()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root.title("Quiz sur les polygones")
    root.iconphoto(False, tk.PhotoImage(file="quiz.png"))
    root.state('zoomed')
    root.bind('<Return>', check_answer)
    # root.resizable(1100, 400)
    
    # Defining the frames
    left_frame = tk.Frame(root, bg="red")
    center_frame = tk.LabelFrame(root, bg="#123456")
    right_frame = tk.Frame(root, bg="green")

    # Packing the frames
    left_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)
    center_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)
    right_frame.pack(side=tk.LEFT, fill=BOTH, expand=True)

    # Content - Left Frame
    points_frame = tk.LabelFrame(left_frame, text="Pointage", bg="red", fg="white", font=(font, 10))
    points_frame.pack(pady=75)
    tk.Label(points_frame, text="1er essai = 3 pts", bg="red", fg="white", font=(font, 10), width=15, height=2).pack()
    tk.Label(points_frame, text="2e  essai = 2 pts", bg="red", fg="white", font=(font, 10), width=15, height=2).pack()
    tk.Label(points_frame, text="3e  essai = 1 pt", bg="red", fg="white", font=(font, 10), width=15, height=2).pack()

    # Content - Center Frame
    '''
    # Image as bg
    canvas = tk.Canvas(center_frame, width=600, height=800)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("quiz.png").resize((600, 800), Image.ANTIALIAS))
    canvas.background = img
    bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
    '''
    tk.Label(center_frame, text="Devine la figure géométrique!", font=(font, 22), bg="#123456", fg="white").pack(pady=10)
    tk.Label(center_frame, textvariable=questionLabel, bg="#123456", fg="white", font=(font, 14)).pack(pady=10)
    tk.Entry(center_frame, textvariable=guessLabel, width=20, font=(font, 14)).pack(pady=10)
    validate = tk.Button(center_frame, text="Valide ta réponse ou ENTER", bd=8, relief=tk.RAISED, font=(font, 12),
                        state=tk.ACTIVE, command=check_answer)
    validate.pack(pady=10, padx=200)    
    message_label = tk.Label(center_frame, textvariable=messageLabel, bg="#123456", fg="yellow")
    message_label.config(font=(font, 14))
    message_label.pack(pady=10)

    # Content - Right Frame
    score_frame = tk.Frame(right_frame, bg="green")
    score_frame.pack(pady=75)
    tk.Label(score_frame, text="Ton pointage", bg="green", font=(font, 14)).pack(pady=5)
    tk.Label(score_frame, textvariable=score, bg="green", font=(font, 18, "bold")).pack(pady=5)
    w = Canvas(score_frame, width=20, height=0, bd=0, highlightthickness=0)
    w.pack()
    w.create_line(0, 0, 200, 0, fill="black")
    tk.Label(score_frame, textvariable=total, bg="green", font=(font, 18, "bold")).pack(pady=5)
   
def startQuiz():    
    poser_question()    
    
# Génère une liste des questions et une liste des réponses
questionAnswerList = read_json("questions_answers.json")
questionIndex = -1
attempts = 0
userName = ""

setupUI()
startQuiz()

root.mainloop()

# TODO: Plein écran: - Done!
# TODO: Changer le font - Done!
# TODO: Mettre une image en fond d'écran dans center_frame
# TODO: animation ou image(main hight five)
# TODO: Si la réponse est vide: "Écrit quelque chose!"
# TODO: différents type de réponses
#  : Réponse courte
#  : Choix de réponse
#  : Vrai ou faux
# TODO: Bind "esc" to close program
#  and add button "Fermer" ou "recommencer"
# TODO: Play sound after printing messsage and updating score

