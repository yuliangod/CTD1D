#!/usr/bin/env python
# coding: utf-8


from tkinter import *
import time
import random

class TyperacerApp(Frame):
    def __init__(self, master):
        super().__init__(master)      

        self.master.title("Typeracer")
        
        self.info_frame = Frame(self.master)
        self.info_frame.pack()
        
        #start
        self.start_label = Label(self.info_frame, text="Type the word correctly to win this game!\n Would you like to start?")
        self.start_label.grid(row=0, column=0)
        self.start_button = Button(self.info_frame, text="start", command = self.game_wc)
        self.start_button.grid(row=1, column=0)     

        #gameplay variables
        self.num_words_typed = 0

        self.start = time.time()

        self.word_list = ['christmas','lemon','wallet','speaker','personal','vegetable','jumble','trust','trouble',
                'forest', 'insert','yacht','green','recycle','dustbin','classroom','keyboard',
                'damage','kitchen','jacket','ivory','stationary','lanyard','lockscreen','printer'] 
        
        self.won_boolean = False

        #images
        self.bg = PhotoImage(file="images\sea.png")

    def check(self):
      
        self.word_wrong_label = Label(self.game_frame, text = ' ')  
        word = self.word_input.get()
        
        if word != self.random_word : #if word typed is spelt wrongly
            #self.word_wrong_label = Label(self.game_frame, text = 'Sorry, that\'s not it, try again! ')
            #self.word_wrong_label.grid(row=3, column=0)
            self.wrong_word_label = self.game_canvas.create_text(20, 100, anchor="nw", text='Sorry, that\'s not it, try again! ')
            
            #self.word_input = Entry(self.game_frame, bd = 5)
            #self.word_input.grid(row=0, column=4)
        
        elif word == self.random_word:  #word is spelt correctly
            self.num_words_typed += 1
            self.game_frame.destroy()
            #print(self.random_word)
            self.word_list.remove(self.random_word)
            #print(self.word_list)
            self.game_wc()      
            
            
    def end_game(self):
        Time_taken = (self.end - self.start)/60
        Type_speed = round (15 / Time_taken , 2 ) 
        if Type_speed >= 12:   
            self.won_boolean = True
            #self.end_game_label = Label(self.game_frame, text = 'Congrats!!! Your ship is moving at ' + str(Type_speed) + 'words/min.\nYou were faster than the pirates')
            #self.end_game_label.grid(row=2, column=0)
            self.end_game_label = self.game_canvas.create_text(20, 100, anchor="nw", text='Congrats!!! Your ship is moving at ' + str(Type_speed) + 'words/min.\nYou were faster than the pirates')

        else :
            #self.try_again_label = Label(self.game_frame, text = 'Your ship is moving at ' + str(Type_speed) + 'words/min, whch is too slow. The pirates have caught up with you. Try again!')
            #self.try_again_label.grid(row=2, column=0)
            self.try_again_label = self.game_canvas.create_text(20, 100, anchor="nw", text='Your ship is moving at ' + str(Type_speed) + 'words/min,\nwhch is too slow.\nThe pirates have caught up with you. Try again!')

            self.restart_button = Button(self.game_frame, text="Restart", command = self.restart_command)
            self.restart_button.place(x=20, y=200)
            #self.start_button_canvas = self.game_canvas.create_window(100, 150, anchor="nw", window=self.start_button)
    
    def enter_button_command(self, event):
        self.check()  #Bind the Enter Key to Call an event   

        if self.num_words_typed == 15: #end game when 15 words are typed
            self.end = time.time()
            self.game_canvas.delete('all')
            #self.enter_button.destroy()
            self.end_game()

    def game_wc(self):
        self.info_frame.destroy()

        self.game_frame = Frame(self.master)
        self.game_frame.pack()    

        self.game_canvas = Canvas(self.game_frame, width=300, height=300)
        self.game_canvas.pack(fill="both", expand=True)
        self.game_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.random_word = random.choice(self.word_list) # choosing the element 

        #self.word_label = Label(self.game_frame, text = self.random_word)
        #self.word_label.grid(row=0, column=0)  
        self.word_label = self.game_canvas.create_text(20, 40, anchor="nw", text=self.random_word)

        self.word_input = Entry(self.game_frame, bd = 5)
        #self.word_input.grid(row=0,column=1)
        self.word_input.focus_set()
        self.world_input_canvas = self.game_canvas.create_window(100, 40, anchor="nw", window=self.word_input)

        self.master.bind('<Return>' , self.enter_button_command)

    def restart_command(self):
        self.num_words_typed = 0

        self.start = time.time()

        self.word_list = ['christmas','lemon','wallet','speaker','personal','vegetable','jumble','trust','trouble',
                'forest', 'insert','yacht','green','recycle','dustbin','classroom','keyboard',
                'damage','kitchen','jacket','ivory','stationary','lanyard','lockscreen','printer'] 
        self.game_frame.destroy()
        self.game_wc()

if __name__ == "__main__":       
    root = Tk()
    root.geometry("300x300")
    myapp = TyperacerApp(root)
    myapp.mainloop()



