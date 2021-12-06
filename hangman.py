import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

class HangmanApp(tk.Frame):

    def get_word(self):
        return random.choice(self.words).lower()
    
    def __init__(self,master):
        super().__init__(master)

        self.master.title("Hangman")
        #info frame
        self.info_frame = tk.Frame(self.master)
        self.info_frame.pack()
        self.start_button = tk.Button(self.info_frame, text="start", command=self.game_start_0_function)
        self.start_button.pack()

        self.game_frame = tk.Frame(self.info_frame)
        self.game_frame.pack()

        self.words = ['Singapore', 'Vietnam', 'Brunei', 'Laos', 'Cambodia','Phillipines', 'Malaysia']

        self.alphabet = ('abcdefghijklmnopqrstuvwxyz')

        self.word = self.get_word()

        self.letters_guessed = []
        
        self.tries = 5
        
        self.guessed = False

        self.a = str(len(self.word))

        #check if game has been won
        self.won_boolean = False

    #1. command when start button is clicked (start button)
    def game_start_0_function(self):
        self.info_frame.destroy()
        self.welcome_frame = tk.Frame(self.master)
        self.welcome_frame.pack()
        welcome_label = Label(self.welcome_frame, text=
                              """Hi! It's time for a game of Hangman!
            The theme of this Hangman game would be
            'Guess the South East Asian country'
            The computer will generate a country and
            you will try to guess what the country is.
            ==============================
            Good Luck! Have fun playing""")
        welcome_label.pack()
        play_game_button = Button(self.welcome_frame, text="Play", command=self.game_run)
        play_game_button.pack()
    
    #2. tell user how many letters are in the word (play button)
    def game_run(self):
        self.welcome_frame.destroy()
        self.game_run_frame = tk.Frame(self.master)
        self.game_run_frame.pack()
        game_line_1 = Label(self.game_run_frame, text="The word contains "+self.a+" letters.")
        game_line_1.pack()
        game_line_2 = Label(self.game_run_frame, text="letters:" +len(self.word)*"-"+ "")
        game_line_2.pack()
        self.decision_2_submit_button = Button(self.game_run_frame, text="ok", command=self.game_start_3_function)
        self.decision_2_submit_button.pack()

    #3. prompt user to enter a alphabet or word (ok button)
    def game_start_3_function(self):
        self.decision_2_submit_button.destroy()

        self.guess_frame = tk.Frame(self.master)
        self.guess_frame.pack()
        
        game_line_3 = Label(self.guess_frame, text="You have " +str(self.tries)+ " tries for this word")
        game_line_3.pack()
        game_line_4 = Label(self.guess_frame, text="Guess a letter in the word or enter the full word")
        game_line_4.pack()
        global user_decision_1
        user_decision_1 = Entry(self.guess_frame)
        user_decision_1.pack()
        self.decision_1_submit_button = Button(self.guess_frame, text="submit", command=self.game_start_4_function)
        self.decision_1_submit_button.pack()

    #4. submit input and check if its correct
    def game_start_4_function(self):
        user_input = user_decision_1.get().lower()
        if len(user_input)==1:

            if user_input not in self.alphabet:
                messagebox.showinfo("Info","You did not enter a letter. Check your input and try again")
                
                self.guess_frame.destroy()
                self.game_start_3_function()

            elif user_input in self.letters_guessed:
                messagebox.showinfo("Info","You have already guessed the letter before. Try another letter!")
               

                self.guess_frame.destroy()
                self.game_start_3_function()

            elif user_input not in self.word:
                messagebox.showinfo("Info","Oops! That letter is not in the word. Guess another one!")
                self.letters_guessed.append(user_input)
                self.tries -=1

                self.guess_frame.destroy()
                self.game_start_3_function()

            elif user_input in self.word:
                messagebox.showinfo("Info","Great! You guessed a correct letter!")
                self.letters_guessed.append(user_input)

                self.guess_frame.destroy()
                self.game_start_3_function()

            else:
                messagebox.showinfo("Info","Check your entry! You might have entered a wrong input")
                
                self.guess_frame.destroy()
                self.game_start_3_function()

        elif len(user_input) == len(self.word):
            if user_input == self.word:
                messagebox.showinfo("Info","Awesome! You guessed the word correctly!")
                self.decision_1_submit_button.destroy()
                self.guessed = True
                decision_2_submit_button = Button(self.guess_frame, text="Next Country", command=self.game_start_1_function)
                decision_2_submit_button.pack()

                
                
            else:
                messagebox.showinfo("Info","Sorry, wrong guess! :((( Please try again!")
                self.tries -=1

                self.guess_frame.destroy()
                self.game_start_3_function()

        else:
            messagebox.showinfo("Info","The length of your guess is not the same as the length of the correct word. Try again.")
            self.tries -=1
            self.guess_frame.destroy()
            self.game_start_3_function()


        status = ''
        if self.guessed == False:
            for letter in self.word:
                if letter in self.letters_guessed:
                    status += letter
                else:
                    status += '_ '
            game_line_13 = Label(self.guess_frame, text= status)
            game_line_13.pack()

        if status == self.word:
            game_line_14 = Label(self.guess_frame, text= "Great job! You guessed the word correctly!")
            game_line_14.pack()
            self.guessed = True

        elif self.tries == 0:
            game_line_15 = Label(self.guess_frame, text= "Oops! You ran out of guesses and you couldn't guess the word.")
            game_line_15.pack()

    #5. button to get to next game if word is guessed correctly
    def game_start_1_function(self):
        self.words.remove(self.word.capitalize())

        self.guess_frame.destroy()
        self.game_run_frame.destroy()

        #win condition
        if len(self.words) == 0:
            win_label = tk.Label(self.master, text="Congrats! You have completed the game!")
            win_label.pack()
            self.won_boolean = True
            
            return None

        self.word = self.get_word()

        #reset variables
        self.word = self.get_word()
        self.letters_guessed = []
        self.tries = 5
        self.guessed = False
        self.a = str(len(self.word))

        self.welcome_frame = tk.Frame(self.master)
        self.welcome_frame.pack()
        play_game_button = Button(self.welcome_frame, text="Play", command=self.game_run)
        play_game_button.pack()

if __name__ == "__main__":   
    root = tk.Tk()
    myapp=HangmanApp(root)
    myapp.mainloop()

