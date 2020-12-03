import tkinter as tk

root = tk.Tk()
root.title("Quiz")
root.iconphoto(False, tk.PhotoImage(file="quiz.png"))
# Autre méthode pour icon: root.iconbitmap("quiz.ico")

titre = tk.Label(text="Quiz sur les polynômes", bg="grey", fg="black", width=50)
titre.pack()

def check_answer():
    print("OK")

score = 0
num_question = 0
question = tk.Label(text='Devinez la figure géométrique')
question.pack()
question1 = tk.Label(text='Une figure à trois côtés s\'appelle: ')
question1.pack()
guess1 = tk.Entry(root)
guess1.pack()
valide = tk.Button(root, text="Valide ta réponse", command=check_answer)
valide.pack()


# check_guess(guess1, 'triangle')



root.mainloop()
