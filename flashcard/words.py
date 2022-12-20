import tkinter as tk
from PIL import ImageTk, Image  
import pandas as pd 
import random
import time

try:
    DF_TURKISH = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    DF_TURKISH = pd.read_csv("frequency_tr.csv")

class Word:
    def __init__(self, canvas: tk.Canvas, window: tk, card):
        self.words_df = DF_TURKISH
        self.window = window
        self.canvas = canvas
        self.front_img = ImageTk.PhotoImage(Image.open("card_front.png"))  
        self.back_img = ImageTk.PhotoImage(Image.open("card_back.png"))  
        self.word_label = canvas.create_text(400, 263, text= "Benzer", fill= "black", font= ("Ariel", 60, "bold"))
        self.lang_label = canvas.create_text(400, 150, text= "Title", fill= "black", font= ("Ariel", 40, "italic"))
        self.card = card
        self.tr_word = ""
        self.en_word = ""


    def word_gen(self):
   
        self.tr_word = self.words_df.sample()
        self.tr_word = self.tr_word.Turkish.tolist()[0]
        self.en_word = self.words_df[self.words_df["Turkish"] == self.tr_word]
        self.en_word = self.en_word.English.tolist()[0]
        self.canvas.itemconfig(self.card, image= self.front_img)
        self.canvas.itemconfig(self.lang_label, text= "Turkish", fill= "black")
        self.canvas.itemconfig(self.word_label, text= self.tr_word, fill= "black")
        self.window.after(3000, self.flipper)
        
    def check_button(self):
        self.word_gen()
        self.words_df = self.words_df[self.words_df.Turkish != self.tr_word]
        self.words_df.to_csv("Words_to_learn.csv", index= False)
        print(len(self.words_df))
    
    
    def flipper(self):
       
        self.canvas.itemconfig(self.card, image= self.back_img)
        self.canvas.itemconfig(self.lang_label, text= "English", fill= "white")
        self.canvas.itemconfig(self.word_label, text= self.en_word, fill= "white")


