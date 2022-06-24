import ScrapPage as sc
from tkinter import Tk,Label

Titres = sc.getTirePage()
Description = sc.getDescriptionPage()
root = Tk()

for tit, des in zip(Titres, Description):
    label = Label(root, text=tit)
    label.grid()
    label2 = Label(root, text=des)
    label2.grid()
    label3 = Label(root, text="///////////////////////////////////////////////////")
    label3.grid()
root.mainloop()