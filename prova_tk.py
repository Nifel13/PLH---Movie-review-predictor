import tkinter as tk
from nltk.corpus import wordnet as wn
from random import randint

wordlist = ["bomb","house","guitar","plane","sea","saturn","atom","beer","sex"]

def generate_word():
    hidden_word = wn.synsets(wordlist[randint(0, len(wordlist)-1)])
    hidden_word_str = hidden_word[0].lemmas()[0].name().lower()
    word_label.config(text=hidden_word_str)

root = tk.Tk()

word_label = tk.Label(root, text="")
word_label.pack()

generate_button = tk.Button(root, text="Generate Word", command=generate_word)
generate_button.pack()

root.mainloop()