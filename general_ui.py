import tkinter as tk
from whack_a_mole import WhackAMoleApp
from hangman import HangmanApp

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.snake_won = False      #check if snake game has been won yet

        self.whack_a_mole_button = tk.Button(text="Whack A Mole", command= lambda: self.new_window_command(WhackAMoleApp, self.hangman_button))
        self.whack_a_mole_button.pack()

        self.hangman_button = tk.Button(text="Hangman", command= lambda: self.new_window_command(HangmanApp, self.snake_button), state="disabled")
        self.hangman_button.pack()

        self.snake_button = tk.Button(text="Snake", command=self.snake_button_command,state="disabled")
        self.snake_button.pack()

        self.type_racer_button = tk.Button(text="Typeracer", command= lambda: self.new_window_command(HangmanApp, self.type_racer_button), state="disabled")
        self.type_racer_button.pack()

    def on_closing(self, app, window, button_enable_on_win):
        #window is to choose which window to destroy, index is to edit won_list to enable buttons
        window.destroy()
        print(app.won_boolean)
        self.master.deiconify()

        if app.won_boolean == True:
            button_enable_on_win["state"] = "active"

    def new_window_command(self, window_class, button_enable_on_win):
        self.master.withdraw()
        self.new_window = tk.Toplevel(self.master)
        self.new_window.geometry("300x300")

        self.new_app = window_class(self.new_window)
        self.new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(self.new_app, self.new_window, button_enable_on_win))      #on closing of window, check if game has been won

        self.new_app.mainloop()

    #open snake game when button is clicked
    def snake_button_command(self):
        self.type_racer_button["state"] = "active"
        import snake
        


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    myapp = App(root)
    myapp.mainloop()