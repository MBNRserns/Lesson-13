from tkinter import *
import speech_recognition as sr
#from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

root=Tk()
root.title("Speech to Text Conversion")
root.geometry("700x500")

def record():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything")
        audio = r.listen(source)
        try:
            text= r.recognize_google(audio)
        except:
            text="Sorry could not recognize your voice"
        txt.delete(1.0, END)
        txt.insert(END,text)

def save():
    fout=asksaveasfile(defaultextension=".txt")
    if fout:
        print(txt.get(1.0,END),file=fout)
    else:
        messagebox.showinfo("Warning", "Text not Saved")


lbl= Label(root, text="Speech To Text", font= "bold, 30")
lbl.grid(row=0, column=1, padx=20, pady=20)

txt= Text(root, height= 4, width= 40)
txt.grid(row=1, column=1, padx=20, pady=20)

translate= Button(root, text= "Click to Record", command= record, width= 20,height=2, bg="red")
translate.grid(row=1, column=0, padx=20, pady=20)

sav= Button(root, text="Save Text", command=save, width= 15, bg="Yellow")
sav.grid(row=1, column=2, padx=20, pady=20)

root.mainloop()