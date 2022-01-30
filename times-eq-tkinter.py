from tkinter import *
import random
import tkinter.messagebox
root = Tk()
root.resizable(False, False)


true=0

run2=False
run=True

good=0
bad=0


def valueerror():
    tkinter.messagebox.showwarning("Warning","Value Error")

def equation():

    x = random.randrange(100)
    y = random.randrange(100)
    z = ()
    true_answer = x * y


    def equal():
        global b
        global run2
        b=e.get()
        run2=True
        kontrola(label2)
    def destroy():
        e.destroy()
        label.destroy()
        label2.destroy()
        label3.destroy()
        label4.destroy()
        button.destroy()

    label=Label(root,text=("what is "+ str(x) +" * "+ str(y)+" ?"),bg="blue2",fg="snow",bd=4,relief=SUNKEN,width=70)
    label.grid(row= 0, column=0,columnspan=3)
    e=Entry(root,width=60,borderwidth=10,)
    e.grid(row=4,rowspan=2,column=0,columnspan=8)
    label2=Label(root,text=(z),bg="blue2",fg="snow",bd=4,relief=SUNKEN,width=40)
    label2.grid(row= 6, column=1)
    button=Button(root,text="corrector",padx=7,pady=4,command=equal)
    button.grid(row=4, column=2,rowspan=1,columnspan=30)
    label3=Label(root,text="bad: "+str(bad),fg="snow",bd=4,relief=SUNKEN,bg="red")
    label3.grid(row=6,column=0)
    label4 = Label(root, text="good: " + str(good), fg="snow", bd=4, relief=SUNKEN,bg="green" )
    label4.grid(row=6, column=2)


    def kontrola(label2):
        global run2
        if run2==True:
            try:
                if int(b)== true_answer:
                    label2["text"]="true"
                    label2["bg"] = "green"
                    good1()
                    run2 = False
                    root.after(2500,destroy)
                    root.after(2500, equation)


                elif int(b) != true_answer:
                    label2["text"]=("false, it is "+ str(true_answer))
                    label2["bg"]="red"
                    bad1()
                    run2 = False
                    root.after(2500,destroy)
                    root.after(2500, equation)

            except ValueError:

                valueerror()

    #root.bind("<Return>", equal)


def bad1():
    global bad
    bad+=1
def good1():
    global good
    good+=1

equation()

root.mainloop()

