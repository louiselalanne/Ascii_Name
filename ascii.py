from tkinter import *

root = Tk()
root.title("Ascii Project")
root.geometry("400x400")
root.configure(background = "pink")

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.3, anchor=CENTER)
label = Label(root, text="Nome em Ascii: ", bg="light yellow")
label.place(relx=0.5,rely=0.5,anchor=CENTER)

def asciiConverter():
    input = enter_word.get()

    for letter in input :
        label["text"] += str(ord(letter)) + " "

btn = Button(root, text="Clique Aqui", command=asciiConverter, bg='yellow', fg='purple')
btn.place(relx =0.5, rely=0.4,anchor=CENTER)

root.mainloop()