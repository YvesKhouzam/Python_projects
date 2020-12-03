import tkinter as tk

root = tk.Tk()
root.title("Quiz")
root.iconphoto(False, tk.PhotoImage(file="quiz.png"))
# Autre méthode pour icon: root.iconbitmap("quiz.ico")

titre = tk.Label(text="Quiz sur les polynômes", bg="grey", fg="black", width=50)
titre.pack()

score = 0
num_question = 0
question1 = tk.Label(text='Devinez la figure géométrique')
question1.pack()
#guess1 = tk.Entry('Une figure à trois côtés s\'appelle: ')
#guess1.pack()
# check_guess(guess1, 'triangle')



root.mainloop()
