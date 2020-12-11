import tkinter as tk

root = tk.Tk()
root.title("Quiz")
root.iconphoto(False, tk.PhotoImage(file="quiz.png"))
tk.Label(text="Quiz sur les polygones", bg="grey", fg="black", width=78).grid(row=0, column=0, columnspan=2)
tk.Label(text="Devinez la figure géométrique.", width=70).grid(row=1, column=0)
tk.Label(text="Pointage").grid(row=1, column=1)

questions = ["Une figure à trois côtés s\'appelle:",
             "Une figure à six côtés s\'appelle:",
             "Les figures à quatre côtés s\'appelle:\n a) Triangles\n b) Heptagones\n c) Quadrilatères\n d) Hendécagones\n",
             "Une figure à cinq côtés s\'appelle:",
             "Une figure à huit côtés s\'appelle:",
             "Vrai ou faux?  Un énnéagone est une figure géométrique à 11 côtés?"
             ]
answers = ["Triangle",
           "Hexagone",
           "c",
           "Pentagone",
           "Octogone",
           "Faux"
           ]

question = tk.StringVar()
question_no = 0
question.set(questions[question_no])
guess = tk.StringVar()
message = tk.StringVar()
score = tk.IntVar()
total = tk.IntVar()
attempts = 0


def check_answer():
    global question_no, attempts
    if (guess.get()).lower() == answers[question_no].lower():
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
        if question_no == len(questions):
            print("fini")

        #    if float(score.get()) > 12: # ((60 / 100) * (score.get() / total)):
        #       tk.Label(final, text="Bravo, tu as réussi! :) ").pack()
        #    else:
        #        tk.Label(final, text="Tu devrais réviser! ;) ").pack()
        #    tk.Button(text="Fermer", command=exit()).pack()
        question.set(questions[question_no])
    total.set(" sur " + str(question_no * 3))


tk.Label(textvariable=question).grid(row=3, column=0)
tk.Entry(root, textvariable=guess).grid(row=4, column=0)
tk.Button(root, text="Valide ta réponse", command=check_answer).grid(row=5, column=0)
tk.Label(textvariable=message).grid(row=6, column=0)
tk.Label(textvariable=score).grid(row=2, column=1)
tk.Label(textvariable=total).grid(row=3, column=1)

# TODO: Mettre fin lorsqu'il ne reste plus de question
# TODO: "Enter" = Boutton click
# TODO: Fenêtre finale: "Tu as eu x/y = z% Bravo ou Tu dois réviser!
# TODO: Mettre une image en fond d'écran
# TODO: Afficher combien de points pour chaque tentative
root.mainloop()
