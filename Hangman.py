import random
Chosen_word=''
Word_list=['Cars','Apple','Phone','Pens','Orange','Colour']
Chosen_word=random.choice(Word_list).lower()
Display=[]

for i in Chosen_word:
    Display.append('_')
print(Display)    

lives=6
end_of_game= False
while not end_of_game:
    guess=input("Guess a letter: ").lower()
    for position in range(len(Chosen_word)):
        letter=Chosen_word[position]
        #print(f'Current postion: {position}\n Current letter: {letter}\n Guessed letter: {guess}')
        if letter==guess:
            Display[position]=letter
    if guess not in Chosen_word:
        print("You lost a life")
        lives -= 1
        print(lives)
        if lives == 0:
            print("Game over")
            print(Chosen_word)
            end_of_game=True    

    
    print(Display)
    if "_" not in Display:
        end_of_game=True
        print("You won")
        print(Chosen_word)