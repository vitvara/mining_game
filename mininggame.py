import tkinter as tk
from tkinter import ttk
from threading import Thread
import time


class mining_game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.moneyint = 100
        self.head = ttk.Label(self, text="Miner Game")
        self.money = ttk.Label(self, text="100")
        self.minerlist = []
        self.geometry('300x300')
        self.colect_but = ttk.Button(self, text="COLECT", command=self.colect)
        self.button = ttk.Button(self, text="Add miner", command=self.addminer)
        self.head.pack()
        self.button.pack()
        self.colect_but.pack()
        self.money.pack()
        self.check_addminer()

    def check_addminer(self):
        if self.moneyint >= 100:
            self.button.state(["!disabled"])
        else:
            self.button.state(["disabled"])
        self.after(10, self.check_addminer)

    def colect(self):
        for i in self.minerlist:
            self.moneyint += i.colect_money()
            self.money['text'] = str(self.moneyint)

    def addminer(self):

        self.moneyint -= 100
        self.money['text'] = str(self.moneyint)
        self.minerlist.append(Miner(self))


class Miner(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.progressbar = ttk.Progressbar(
            parent, length=100, mode="determinate")
        self.progressbar.pack()
        self.runthread(self.progressbar)
        self.money = 0
        self.time = 0.01
        self.level = 0

    def runthread(self, progressbar):
        print("running thread ... ")
        self.thread = Thread(target=lambda: self.task(progressbar))
        self.thread.start()
        self.after(10, self.check_thread)

    def upgrade(self):
        pass

    def colect_money(self):
        m = self.money
        self.money = 0
        self.runthread(self.progressbar)
        return m

    def check_thread(self):
        if self.thread.is_alive():
            self.after(10, self.check_thread)
        else:
            if self.money == 100:
                pass
            else:
                self.money += 10
                print("finish")
                self.runthread(self.progressbar)
                print(self.money)

    def task(self, progressbar):
        for i in range(101):
            progressbar['value'] = i
            time.sleep(self.time)


if __name__ == "__main__":
    app = mining_game()
    app.mainloop()
