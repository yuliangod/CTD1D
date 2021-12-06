import tkinter as tk
import time
import random
from threading import Thread

class WhackAMoleApp(tk.Frame):
    def __init__(self, master, rows=5, columns=5):
        super().__init__(master)
        
        self._rows = rows
        self._columns = columns

        self._pass_score = 10   #minimum points needed to win the game

        #app layout
        self.info_frame = tk.Frame(self.master)
        self.info_frame.pack()
        self.score_label = tk.Label(self.info_frame, text="Score: 0")
        self.score_label.grid(row=0, column=0)
        self.mole_lable = tk.Label(self.info_frame, text=f"Moles: 0/10")
        self.mole_lable.grid(row=0, column=1)

        self.start_frame = tk.Frame(self.master)
        self.start_frame.pack()
        self.start_info_label = tk.Label(self.start_frame, text=f"Click the gold bars to score points!\n\nDo not to click on the bombs as\npoints will be deducted!\n\nScore above {self._pass_score} points to win!")
        self.start_info_label.grid(row=0, column=0)
        self.start_button = tk.Button(self.start_frame, text="start", command=self.threaded_start_command)
        self.start_button.grid(row=1, column=0)

        self.game_frame = tk.Frame(self.master)
        self.game_frame.pack()
    
        #scoring
        self.score = 0
        self.mole_count = 0

        #gameplay
        self.mole_value_list = [0]*8 + [1,2]   #0 is real mole, 1 is fake mole, if fake mole is clicked deduct points
        random.shuffle(self.mole_value_list)
        self.mole_value = self.mole_value_list[self.mole_count]

        self.won_boolean = False    #check if game has been won already

        #images
        self.gold_photo = tk.PhotoImage(file="images/goldbar.png")
        self.bomb_photo = tk.PhotoImage(file="images/bomb.png")
    
    def start_command(self):
        self.create_buttons()
        self.enable_rand_button()
        self.start_frame.destroy()
    
    #fix problem when fake mole is the first mole to pop out
    def threaded_start_command(self):
        t1 = Thread(target=self.start_command)
        t1.start()
        t2 = Thread(target=self.check_fake_mole)
        t2.start()

    def create_buttons(self):
        self.button_list = []
        for i in range(self._rows):
            for column in range(self._columns):
                button = tk.Button(self.game_frame, width="4", height="2", state="disable", command=self.threaded_button_command, bg="white", relief="flat", padx=5, pady=5)
                button.grid(row=i + 1, column=column, padx=2, pady=2)
                self.button_list.append(button)

    def enable_rand_button(self):
        self.start_time = time.time()   #time to calculate score
        self.index = random.randrange(self._rows*self._columns)
        self.button_list[self.index]["state"] = "normal"
        self.button_list[self.index]["relief"] = "raised"
        
        if self.mole_value == 0:
            
            self.button_list[self.index].config(image=self.gold_photo, width="40", height="40")

            #self.button_list[self.index]["bg"] = "green"
            
        else:
            self.button_list[self.index].config(image=self.bomb_photo, width="40", height="40")
            #self.button_list[self.index]["bg"] = "red"

    def random_delay(self, max_time=1):
        delay = random.uniform(0, max_time)
        time.sleep(delay)

    def button_command(self):
        #calculate score
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        if self.mole_value == 0:
            self.score += (1/self.time_taken)
        else:
            self.score -= (1/self.time_taken)

        #update game info
        self.mole_count += 1
        if self.mole_count < 10:
            self.mole_value = self.mole_value_list[self.mole_count]
        self.score_label["text"] = f"Score: {self.score:.2f}"
        self.mole_lable["text"] = f"Moles: {self.mole_count}/10"

        #end game if mole has been clicked 10 times
        if self.mole_count == 10:
            self.game_over()
            return None

        #continue flow of the game
        if self.mole_count < 10:
            self.button_list[self.index].config(state="disabled", relief="flat", bg="white", image="", width="4", height="2")
            self.random_delay(1)    #change delay of mole appearing         
            self.enable_rand_button()

    def check_fake_mole(self):
        if self.mole_count < 10:
            if self.mole_value == 1:
                time.sleep(2)
                if self.mole_value == 1:
                    self.end_time = time.time()
                    self.time_taken = self.end_time - self.start_time
                    self.score += (1/self.time_taken)   #give back scores deducted away


                    self.button_command()

            if self.mole_value == 2:
                time.sleep(2)
                if self.mole_value == 2:
                    self.end_time = time.time()
                    self.time_taken = self.end_time - self.start_time
                    self.score += (1/self.time_taken)   #give back scores deducted away

                    self.button_command()

    #fix problem of button remaining depressed
    def threaded_button_command(self):
        t1 = Thread(target=self.button_command)
        t1.start()    
        t2 = Thread(target=self.check_fake_mole)
        t2.start()        

       

    #game over screen 
    def game_over(self):     #update pass score to set points needed to pass
        self.game_frame.destroy()
        self.game_over_frame = tk.Frame(self.master)
        self.game_over_frame.pack()


        if self.score >= self._pass_score:
            self.game_over_label = tk.Label(self.game_over_frame, text=f"Congrats, you scored over {self._pass_score}, \nyou can move on to the next stage now!")
            self.game_over_label.pack()
            self.won_boolean = True
        else:
            self.game_over_label = tk.Label(self.game_over_frame, text=f"Sorry, you scored below {self._pass_score}, \nrestart the game?")
            self.game_over_label.pack()

            self.restart_game_button = tk.Button(self.game_over_frame, text="Restart game", command=self.restart_game_command)
            self.restart_game_button.pack()

    def restart_game_command(self):
        self.game_frame.destroy()
        self.info_frame.destroy()
        self.game_over_frame.destroy()
        self.__init__(self.master, self._rows, self._columns)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    myapp = WhackAMoleApp(root, 5, 5)
    myapp.mainloop()
   