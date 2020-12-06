import tkinter as tk

# Setup de la fenêtre
root = tk.Tk()
root.title("Quiz")
root.iconphoto(False, tk.PhotoImage(file="quiz.png"))
titre = tk.Label(text="Quiz sur les polynômes", bg="grey", fg="black", width=50).pack()
sous_titre = tk.Label(text='Devinez la figure géométrique').pack()

# List des questions et des réponses
questions = ["Question 1", "Question 2", "Question 3", "Question 4"]
guesses = ["réponse 1", "réponse 2", "réponse 3", "Réponse 4"]

# Déclaration des variables
score = 0
num_question = 0
i = 0
guess = tk.StringVar()


def check_answer():
    global i
    if guess.get() != guesses[i]:
        answer_key = tk.Label(text="Try again!").pack()
        guess.set("")
    else:
        answer_key = tk.Label(text="Bonne réponse!").pack()
        answer_key = tk.Label(text=" ").pack()
        i += 1
        question = tk.Label(text=questions[i]).pack()
        entryGuess = tk.Entry(root, textvariable=guess).pack()
        validate = tk.Button(root, text="Valide ta réponse", command=check_answer).pack()


question = tk.Label(text=questions[i]).pack()
entryGuess = tk.Entry(root, textvariable=guess).pack()
validate = tk.Button(root, text="Valide ta réponse", command=check_answer).pack()

root.mainloop()
