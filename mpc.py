import sys
import winsound
import threading
from tkinter import *

def main():
    mGui = Tk()

    mGui.geometry()
    mGui.title('Python Sampler')

    mlabel = Label(text = 'Python Sampler', font = 'Impact')
    mlabel.grid(row = 0, column = 1)

    def play(sound):
        t = threading.Thread(target = winsound.PlaySound('%s.wav' % sound, winsound.SND_ASYNC | winsound.SND_FILENAME))
        t.start()

    for i in range(1, 4):
        for j in range(0, 3):
            button = Button(command = lambda i = i, j = j: play(3 * (i - 1) + j + 1), bd = 5)
            button.grid(row = i, column = j,  padx = 5, pady = 5)
            button.config(width = 20, height = 10)

    mGui.mainloop()

if __name__ == '__main__':
    main()
