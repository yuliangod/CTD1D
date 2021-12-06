import tkinter as tk
from tkinter import messagebox
from whack_a_mole import WhackAMoleApp
from hangman import HangmanApp

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        snake_message = ("""
You are in the jungle pier about to embark on your quest to find the treasure. 

However, you chance upon a snake that threatens to endanger you. 

Feed the snake with adequate food to fatten the snake and slow it down. 

After winning, you can escape the snake and board the ship.
        """)
        self.snake_button = tk.Button(text="Snake", command=lambda: self.snake_button_command(self.whack_a_mole_button, snake_message))
        self.snake_button.pack()

        wam_message = ("""
After you escaped the snake, you're getting ready to board the ship to embark on your treasure hunt journey. 

However, he must first collect enough gold resources to help for the hunt. 
        """)
        self.whack_a_mole_button = tk.Button(text="Whack A Mole", command= lambda: self.new_window_command(WhackAMoleApp, self.hangman_button, wam_message), state="disabled")
        self.whack_a_mole_button.pack()

        hangman_message = ("""
Upon successfully collecting the good resources, you set sail to find your treasure. 

However, the navigation system on board only allows you to start the engine if you're able to pass a basic navigation test.          
        """)
        self.hangman_button = tk.Button(text="Hangman", command= lambda: self.new_window_command(HangmanApp, self.type_racer_button, hangman_message), state="disabled")
        self.hangman_button.pack()

        typeracer_message = ("""
After clearing the navigation test, you begin sailing to the treasure island. 

However, you soon notices that pirates are quickly approaching the island too. 

In order to get to the island before the pirates, you must increase the ship’s speed.        
        """)
        self.type_racer_button = tk.Button(text="Typeracer", command= lambda: self.new_window_command(HangmanApp, self.battleship_button, typeracer_message), state="active")
        self.type_racer_button.pack()

        self.battleship_button = tk.Button(text="Battleship", command=self.battleship_command)
        self.battleship_button.pack()

    def on_closing(self, app, window, button_enable_on_win):
        #window is to choose which window to destroy, index is to edit won_list to enable buttons
        window.destroy()
        print(app.won_boolean)
        self.master.deiconify()

        if app.won_boolean == True:
            button_enable_on_win["state"] = "active"

    def new_window_command(self, window_class, button_enable_on_win, message):
        self.master.withdraw()
        messagebox.showinfo("", message)
        self.new_window = tk.Toplevel(self.master)
        self.new_window.geometry("300x300")

        self.new_app = window_class(self.new_window)
        self.new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(self.new_app, self.new_window, button_enable_on_win))      #on closing of window, check if game has been won

        self.new_app.mainloop()

    #open snake game when button is clicked
    def snake_button_command(self, button_enabled_on_win,  message):
        messagebox.showinfo("", message)
        button_enabled_on_win["state"] = "active"
        import snake
        
    def test_command(self):
        from test import test
        test()

    def battleship_command(self):
        messagebox.showinfo("", "Please go back to your python shell for the final game")
        self.master.destroy()
        import battleship

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    myapp = App(root)
    myapp.mainloop()