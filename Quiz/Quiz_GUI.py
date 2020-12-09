import tkinter as tk

root = tk.Tk()
root.title("Quiz")
root.iconphoto(False, tk.PhotoImage(file="quiz.png"))
tk.Label(text="Quiz sur les polygones", bg="grey", fg="black", width=78).grid(row=0, column=0, columnspan=2)
tk.Label(text='Devinez la figure géométrique', width=70).grid(row=1, column=0)
tk.Label(text="Pointage").grid(row=1, column=1)

questions = ["Une figure à trois côtés s\'appelle:", "Une figure à six côtés s\'appelle:", "Les figures à quatre côtés s\'appelle:\n a) Triangles\n b) Heptagones\n c) Quadrilatères\n d) Hendécagones\n'", "Question 4"]
answers = ["Triangle", "hexagone", "c", "Réponse 4"]

question = tk.StringVar()
question_no = 0
question.set(questions[question_no])
guess = tk.StringVar()
message = tk.StringVar()
score = tk.IntVar()
attempts = 0


def check_answer():
    global question_no, attempts
    if guess.get() == answers[question_no]:
        message.set("Bonne réponse!")
        guess.set("")
        score.set(score.get() + 3 - attempts)
        attempts = 0
        question_no += 1
        question.set(questions[question_no])
    elif attempts < 2 and guess.get() != answers[question_no]:
        message.set("Mauvaise réponse, Essaie encore, il te reste " + str(2 - attempts) + " essai(s)")
        guess.set("")
        attempts += 1
    else:
        message.set("La bonne réponse est: " + answers[question_no])
        guess.set("")
        attempts = 0
        question_no += 1
        question.set(questions[question_no])


tk.Label(textvariable=question).grid(row=3, column=0)
tk.Entry(root, textvariable=guess).grid(row=4, column=0)
tk.Button(root, text="Valide ta réponse", command=check_answer).grid(row=5, column=0)
tk.Label(textvariable=message).grid(row=6, column=0)
tk.Label(textvariable=score).grid(row=2, column=1)
root.mainloop()
