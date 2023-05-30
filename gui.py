from tkinter import *
from tkinter import messagebox
import jokehandler

jokehand =
jokehandler.Jokehandler("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=singel")

root = Tk ()
root.title("RoligHistoria")

# Create text widget and specify size.
textbox = Text (root, height = 10, width = 100, font="Helvetica", fg="purple" )

# Define the size of the window
root.geometry("1000x400")

# Create label
header = Label(root, text= "Dagens roliga historia")
header.config(font =("helvetica", 14))

Fact = """A man can be arrested in Italt for wering a skirt in public."""

def clickGetJokeButt ():


    textbox.delete("1.0","end")
    t_joke = jokehand.get_joke()
    textbox.insert(INSERT, t_joke)
    #print("click")



    button_getjoke = Button(text="Get Joke", padx=6, pady=6, command = clickGetJokeButt)
    # Create an Exit button.
    button_avsluta = Button(root, text = "Avsluta", padx=6,  pady=6, command =
    root.destroy)

    header.pack()
    textbox.pack()
    button_getjoke.pack()
    button_avsluta.pack()

    root.mainloop()