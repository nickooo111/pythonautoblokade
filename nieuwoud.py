import math
from Tkinter import *

def enter():
  nieuw = ment.get()
  oud = ment2.get()
  if nieuw.isdigit() and oud.isdigit(): 
    uitkomst = (float(nieuw) - float(oud)) / float(oud) * 100
    if float(uitkomst) < 0:
      stijgingdaling = "daling"
    if float(uitkomst) == 0:
      stijgingdaling = "geen verandering"
    if float(uitkomst) > 0:
      stijgingdaling = "stijging"

    print(uitkomst)
    print(stijgingdaling)
    root2 = Tk()
    root2.title("rekenmachine economie") 
    root2.geometry("500x500")
    label1 = Label(root2, text=float(uitkomst)) .pack()
    label2 = Label(root2, text=stijgingdaling) .pack()
    root2.geometry("500x500")
    root2.mainloop()
  else:
    def is_float(nieuw):
        try:
            float(nieuw)
            return True
        except ValueError:
            return False

    def is_float2(oud):
        try:
            float(oud)
            return True
        except ValueError:
            return False
   
    if is_float == True and is_float2 == True:
      print(uitkomst)
    else:
      print("Er zijn letters of tekens gevonden!")


def enter2():
  nieuw = ment.get()
  oud = ment2.get()
  if nieuw.isdigit() and oud.isdigit(): 
    uitkomst = (float(nieuw) - float(oud)) / float(oud) * 100 + 100
    if float(uitkomst) < 100:
      stijgingdaling = "daling"
    if float(uitkomst) == 100:
      stijgingdaling = "geen verandering"
    if float(uitkomst) > 100:
      stijgingdaling = "stijging"

    print(uitkomst)
    print(stijgingdaling)
    root2 = Tk()
    root2.title("rekenmachine economie") 
    root2.geometry("500x500")
    label1 = Label(root2, text=float(uitkomst)) .pack()
    label2 = Label(root2, text=stijgingdaling) .pack()
    root2.geometry("500x500")
    root2.mainloop()
  else:
    def is_float(nieuw):
        try:
            float(nieuw)
            return True
        except ValueError:
            return False

    def is_float2(oud):
        try:
            float(oud)
            return True
        except ValueError:
            return False
   
    if is_float == True and is_float2 == True:
      print(uitkomst)
    else:
      print("Er zijn letters of tekens gevonden!")

root = Tk()
root.title("rekenmachine economie") 
root.geometry("500x500")
ment = StringVar()
ment2 = StringVar()
label1 = Label(root, text="Nieuw:") .pack()
e = Entry(root, textvariable=ment, text="Nieuw: ").pack()
label2 = Label(root, text="Oud:") .pack()
e2 = Entry(root, textvariable=ment2, text="Oud: ").pack()
button = Button(root, text="Berekenen", command = enter).pack()
button = Button(root, text="Berekenen stijging", command = enter2).pack()
root.geometry("500x500")
root.mainloop()