import datetime
import tkinter as tk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 20


class Timer:
    
    def __init__(self, canvas: tk.Canvas, window: tk, timer_label, status_label: tk.Label, check_label: tk.Label):
        
        self.canvas = canvas
        self.window = window
        self.timer_label = timer_label
        self.status_label = status_label
        self.check_label = check_label
        self.reps = 1
        self.check_mark = ""
        self.reset_time()
        self.run = None
    
    def reset_time(self):
        
        self.work_time = datetime.timedelta(seconds= WORK_MIN)
        self.short_br_time = datetime.timedelta(seconds= SHORT_BREAK_MIN)
        self.long_br_time = datetime.timedelta(minutes= LONG_BREAK_MIN)
        self.second = datetime.timedelta(seconds= 1)

    def work_timer(self):
        
        self.status_label.config(text= "Work", fg= GREEN)
        if self.work_time >= self.second:
            self.canvas.itemconfig(self.timer_label, text= str(self.work_time)[2:])
            self.work_time = self.work_time - self.second
        
        elif int(self.work_time.seconds) == 0:
            self.check_mark += " ✓"
            self.canvas.itemconfig(self.timer_label, text= str(self.work_time)[2:])
            self.check_label.config(text= self.check_mark)
            self.reps += 1
            self.reset_time()
            return
    

    def short_br_timer(self):
        
        self.status_label.config(text= "Short Break", fg= PINK)
        if self.short_br_time >= self.second:
            self.canvas.itemconfig(self.timer_label, text= str(self.short_br_time)[2:])
            self.short_br_time = self.short_br_time - self.second
        
        elif int(self.short_br_time.seconds) == 0:
            self.canvas.itemconfig(self.timer_label, text= str(self.short_br_time)[2:])
            self.reps += 1
            self.reset_time()
            return
        
    def long_br_timer(self):
        
        self.status_label.config(text= "Long Break", fg= RED)
        if self.long_br_time >= self.second:
            self.canvas.itemconfig(self.timer_label, text= str(self.long_br_time)[2:])
            self.long_br_time = self.long_br_time - self.second
        
        elif int(self.long_br_time.seconds) == 0:
            self.canvas.itemconfig(self.timer_label, text= str(self.short_br_time)[2:])
            self.reset_time()
            self.reps += 1


    def count_down(self):

        if self.reps == 1 or self.reps == 3 or self.reps == 5 or self.reps == 7:
            self.work_timer()
            self.window.after(1000, self.count_down)

        elif self.reps == 2 or self.reps == 4 or self.reps == 6:
            self.short_br_timer()
            self.window.after(1000, self.count_down)

        elif self.reps == 8:
            self.long_br_timer()
            self.window.after(1000, self.count_down)

    def reset_all(self):
        
        self.reset_time()
        self.reps = 1
        self.canvas.itemconfig(self.timer_label, text= "00:00")
        self.status_label.config(text= "Timer", font= (FONT_NAME, 30, "bold"), bg= "#E8F9FD", fg= "#59CE8F")
        self.check_mark = ""
        self.check_label.config(text= self.check_mark)
        
        


#lambda: timer_object.count_down(window, timer_label)

# long_br_time = datetime.timedelta(minutes= LONG_BREAK_MIN)
# print(int(long_br_time.seconds))