import tkinter

# TODO: creeaza butoane, care activeaza varibile care detecteaza pe cel care initiaza conexiunea, el va fi server

class MakeWindow:
    root = tkinter.Tk()
    root.title("Heptagon")
    root.geometry('800x600')
    root.minsize(800, 600)

window = MakeWindow.root

def on_click():
    print("Testing")

btn = tkinter.Button(window, text="button 1", command=on_click)
btn.grid()

window.mainloop()