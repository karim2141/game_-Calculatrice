import tkinter as tk
import random
from tkinter import messagebox
def generate_question():
    global correct_answer
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    
    question_label.config(text=f"{num1} {operator} {num2}")
    generate_options(correct_answer)
def generate_options(correct):
    options = [correct]
    while len(options) < 4:
        wrong_answer = random.randint(correct - 10, correct + 10)
        if wrong_answer != correct and wrong_answer not in options:
            options.append(wrong_answer)
    random.shuffle(options)
    for i, btn in enumerate(buttons):
        btn.config(text=options[i])
def check_answer(user_answer):
    global score
    if user_answer == correct_answer:
        score += 1
        score_label.config(text=f"Score: {score}")
        root.config(bg="lightgreen")
        messagebox.showinfo("Bonne réponse !", "Bravo ! Continue comme ça !")
    else:
        root.config(bg="red")
        messagebox.showerror("Mauvaise réponse", f"La bonne réponse était {correct_answer}.")
    
    root.config(bg="lightblue")
    generate_question()
root = tk.Tk()
root.title("Jeu de Calculatrice pour Enfants")
root.geometry("400x400")
root.config(bg="lightblue")
score = 0
correct_answer = 0

name_label = tk.Label(root, text="KARIM MAÂLI", font=("Arial", 28, "bold"), bg="lightblue", fg="darkblue")
name_label.pack(pady=10)

title_label = tk.Label(root, text="Jeu de Calculatrice", font=("Arial", 20, "bold"), bg="lightblue", fg="darkblue")
title_label.pack(pady=10)

question_label = tk.Label(root, text="", font=("Arial", 20), bg="lightblue")
question_label.pack(pady=20)

buttons_frame = tk.Frame(root, bg="lightblue")
buttons_frame.pack(pady=20)
buttons = []
for i in range(4):
    btn = tk.Button(buttons_frame, text="", font=("Arial", 16), width=5, height=2, bg="yellow", 
                    command=lambda i=i: check_answer(int(buttons[i]['text'])))
    btn.grid(row=i//2, column=i%2, padx=10, pady=10)
    buttons.append(btn)

score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 16), bg="lightblue")
score_label.pack(pady=10)

generate_question()

root.mainloop()

