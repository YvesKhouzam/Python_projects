import json
import tkinter as tk

# Setup de la fenêtre
root = tk.Tk()
root.title("Quiz")
root.iconphoto(False, tk.PhotoImage(file="quiz.png"))
tk.Label(text="Les polygones", bg="grey", fg="black").grid(row=0, column=0, columnspan=3)
tk.Label(text="Devinez la figure géométrique.", width=70).grid(row=1, column=1)
tk.Label(text="Pointage").grid(row=1, column=2)


# Retourne une liste généréée à partir d'un json selon une clé
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
tk.Label(textvariable=question).grid(row=3, column=1)
question.set(questions[question_no])
guess = tk.StringVar()
tk.Entry(root, textvariable=guess).grid(row=4, column=1)
message = tk.StringVar()
score = tk.IntVar()
total = 0
attempts = 0


def poser_question():
    global nbr_questions, question_no, total
    question_no += 1
    nbr_questions -= 1
    question.set(questions[question_no])
    total += 3


def msg_final():
    if float(score.get()) > 12:  # ((60 / 100) * (score.get() / total)):
        message.set("Bravo, tu as réussi! :) ")
    else:
        message.set("Tu devrais réviser! :( ")
    validate.config(state=tk.DISABLED)


def check_answer():
    global question_no, attempts
    attempts += 1
    if (guess.get()).lower() == answers[question_no].lower():  # Si bonne réponse
        message.set("Bonne réponse!")
        guess.set("")
        score.set(score.get() + 4 - attempts)
        if nbr_questions > 1:
            poser_question()
            attempts = 0
        else:  # Il ne reste plus de questions
            msg_final()
    else:  # Si mauvaise réponse
        if attempts < 3:  # Il reste 1 ou 2 essais
            message.set("Mauvaise réponse, Essaie encore, il te reste " + str(3 - attempts) + " essai(s)")
            guess.set("")
        else:
            message.set("La bonne réponse est: " + answers[question_no])
            guess.set("")
            if nbr_questions > 0:
                poser_question()
                attempts = 0
            else:  # Il ne reste plus de questions
                msg_final()

    # total.set(" sur " + str(question_no * 3))


validate = tk.Button(root, text="Valide ta réponse", state=tk.ACTIVE, command=check_answer)
validate.grid(row=5, column=1)
tk.Label(textvariable=message).grid(row=6, column=1)
tk.Label(textvariable=score).grid(row=2, column=2)
tk.Label(textvariable=total).grid(row=3, column=2)

# TODO: "Enter" = Boutton click
# TODO: Fenêtre finale: "Tu as eu x/y = z% Bravo ou Tu dois réviser!
# TODO: Mettre une image en fond d'écran
# TODO: Afficher combien de points pour chaque tentative
root.mainloop()
