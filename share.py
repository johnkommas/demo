from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.minsize(height=500, width=900)
root.geometry("300x300+120+120")


def s():
    frame = ttk.Frame(root)
    frame.place(x=375, y=200)
    frame.config(heigh=50, width=50)
    frame.config(relief=RIDGE)
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    my_list = Listbox(frame, yscrollcommand=scrollbar.set)
    ent = Entry(root)
    ent.place(x=375, y=370)
    for line in range(100):
        my_list.insert(END, "IP " + str(line))

    my_list.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=my_list.yview)
    lab2 = Label(root, text="choose specific IP").place(x=270, y=370)
    b2 = Button(text="next", command=two).place(x=600, y=400)


def two():
    top = Toplevel()
    top.minsize(height=500, width=900)
    top.geometry("300x300+120+120")
    top.title("vaccine")

    def sel():
        selection = "You selected the option " + str(var.get())

        frame = ttk.Frame(top)
        frame.place(x=375, y=250)
        frame.config(heigh=50, width=50)
        frame.config(relief=RIDGE)
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox(frame, yscrollcommand=scrollbar.set)
        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)

        def r():
            messagebox.showinfo(title="port will close", message="names of port")

        CheckVar1 = IntVar()
        C1 = Checkbutton(top, text="close resky ports", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20,
                         command=r)
        C1.place(x=375, y=400)

        for line in range(100):
            mylist.insert(END, "port number " + str(line + 1))

        b2 = Button(top, text="next", command=three).place(x=600, y=400)

    lab = Label(top, text='select port scanning method', font=40).place(x=375, y=100)
    var = IntVar()
    R1 = Radiobutton(top, text="TCP", variable=var, value=1,
                     command=sel)
    R1.place(x=375, y=150)

    R2 = Radiobutton(top, text="UDP", variable=var, value=2,
                     command=sel)
    R2.place(x=375, y=170)

    R3 = Radiobutton(top, text="SYN", variable=var, value=3,
                     command=sel)
    R3.place(x=375, y=190)
    R4 = Radiobutton(top, text="SCANNING ALL PORTS", variable=var, value=4,
                     command=sel)
    R4.place(x=375, y=210)
    b2 = Button(top, text="skip", command=three).place(x=600, y=430)


def three():
    top2 = Toplevel()

    top2.minsize(height=500, width=900)
    top2.geometry("300x300+120+120")
    top2.title("vaccine")

    def a():
        frame = ttk.Frame(top2)
        frame.place(x=375, y=200)
        frame.config(heigh=200, width=200)
        frame.config(relief=RIDGE)
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox(frame, yscrollcommand=scrollbar.set)

        for line in range(100):
            mylist.insert(END, " vulnerrabilites name / link")

        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)
        lab2 = Label(top2, text="to solve vulnerrabilites copy the link ").place(x=270, y=370)
        b3 = Button(top2, text="next", command=four).place(x=600, y=400)

    b = Button(top2, text="scan vulnerrabilites", width=25, height=4, bg='gray', fg='black', command=a).place(
        x=350,
        y=60)
    b2 = Button(top2, text="skip", command=four).place(x=600, y=430)


def four():
    top3 = Toplevel()

    top3.minsize(height=500, width=900)
    top3.geometry("300x300+120+120")
    top3.title("vaccine")

    def i():
        lab = Label(top3, text="IDS is active ", font=30).place(x=350, y=300)
        b3 = Button(top3, text="next", command=five).place(x=600, y=400)

    b = Button(top3, text="active IDS", width=40, height=15, bg='gray', fg='black', command=i).place(x=350, y=40)

    b2 = Button(top3, text="skip", command=five).place(x=600, y=430)


def five():
    top4 = Toplevel()

    top4.minsize(height=500, width=900)
    top4.geometry("300x300+120+120")
    top4.title("vaccine")

    def p():
        lab2 = Label(top4, text="iptable is active ", font=30).place(x=350, y=300)

    b2 = Button(top4, text="active iptable", width=40, height=15, bg='gray', fg='black', command=p).place(x=350, y=40)
    b3 = Button(top4, text="end", command=quit).place(x=600, y=430)


b = Button(text="check devices on network", width=25, height=4, bg='gray', fg='black', command=s).place(x=350, y=60)

root.mainloop()
