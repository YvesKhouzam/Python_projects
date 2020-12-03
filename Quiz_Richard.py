import tkinter as tk

root = tk.Tk()
root.title("Les polygones")

t = tk.Text(root, width=50, height=5)

t.grid(row=0, column=0, padx=10, pady=10)
t.insert(tk.END, "Question: \nNumber 1")
t.delete(tk.END)
t.insert(tk.END, "Question: \nNumber 2")

root.mainloop()

def check_guess(guess, answer):
    global score
    global num_question
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Bonne réponse!')
            score = score + 3 - attempt
            still_guessing = False
            num_question = num_question + 3
        else:
            if attempt < 2:
                guess = input('Mavaise réponse.  Essaie encore. ')
            attempt = attempt + 1

    if attempt == 3:
        print('La bonne réponse est ' + answer)
        num_question = num_question + 3


score = 0
num_question = 0
print('Devinez la figure géométrique')
guess1 = input('Une figure à trois côtés s\'appelle: ')
check_guess(guess1, 'triangle')
guess2 = input('Une figure à six côtés s\'appelle: ')
check_guess(guess2, 'hexagone')
guess3 = input(
    'Les figures à quatre côtés s\'appelle:\n a) Triangles\n b) Heptagones\n c) Quadrilatères\n d) Hendécagones\n')
check_guess(guess3, 'c')
guess4 = input('Une figure à cinq côtés s\'appelle: ')
check_guess(guess4, 'pentagone')
guess5 = input('Une figure à huit côtés s\'appelle: ')
check_guess(guess5, 'octogone')
guess6 = input('Vrai ou faux?  Un énnéagone est une figure géométrique à 11 côtés?')
check_guess(guess6, 'Faux')
print('Ton score est de ' + str(score), 'sur ' + str(num_question))
if score > 12:
    print('Bravo!')
else:
    print('Tu dois t\'améliorer.')


