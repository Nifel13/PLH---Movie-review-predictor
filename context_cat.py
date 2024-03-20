import nltk
"""nltk.download('wordnet')
nltk.download('sentiwordnet')
nltk.download('omw-1.4')"""
from textblob import TextBlob
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from random import randint

wordlist = ["bomb","house","guitar","plane","sea","saturn","atom","beer","sex"]
best_words = []
hidden_word = wn.synsets(wordlist[randint(0, len(wordlist)-1)])
hidden_word_str = hidden_word[0].lemmas()[0].name().lower()

# calculate the distance between the word and the hidden word
print("\n\n")
print("""      ::::::::   ::::::::  ::::    ::: ::::::::::: :::::::::: :::    ::: ::::::::::: :::::::::: 
    :+:    :+: :+:    :+: :+:+:   :+:     :+:     :+:        :+:    :+:     :+:     :+:         
   +:+        +:+    +:+ :+:+:+  +:+     +:+     +:+         +:+  +:+      +:+     +:+          
  +#+        +#+    +:+ +#+ +:+ +#+     +#+     +#++:++#     +#++:+       +#+     +#++:++#      
 +#+        +#+    +#+ +#+  +#+#+#     +#+     +#+         +#+  +#+      +#+     +#+            
#+#    #+# #+#    #+# #+#   #+#+#     #+#     #+#        #+#    #+#     #+#     #+#             
########   ########  ###    ####     ###     ########## ###    ###     ###     ##########       """)
print("\n\n")

def print_best_words(best_words):
    best_words.sort(key=lambda x: x[1], reverse=True)
    for word, distance in best_words:
        if distance == 1:
            end = True
        word = TextBlob(word).translate(to="cat")
        print(f"{word}: {(1/distance**3.5):.0f}")

end = False
while end == False:
    word = str(input("Enter a word: "))
    word = TextBlob(word).lower()
    word_eng = word.translate(to="en")
    if word_eng == hidden_word_str:
        print("You found the word!")
        end = True
        break
    if word == "help_debug":
        print(hidden_word_str)
    synscores = []
    for synset in wn.synsets(word):
        distance = hidden_word[0].wup_similarity(synset)
        if distance is not None:
            synscores.append((synset.lemmas()[0].name(), distance))
    if len(synscores) > 0:
        if max(synscores, key=lambda x: x[1]) == 1:
            print("You found the word!")
            end = True
        best_words.append(max(synscores, key=lambda x: x[1]))
        print_best_words(best_words)
print("\n\n") 
print(""" .d8888b.   .d8888b.  
d88P  Y88b d88P  Y88b 
888    888 888    888 
888        888        
888  88888 888  88888 
888    888 888    888 
Y88b  d88P Y88b  d88P 
 "Y8888P88  "Y8888P88 """)