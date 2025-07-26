from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk

# def showmesage():
#     messagebox.showinfo(title="Sure",message="ยืนยันการสร้างไฟล์ใหม่")
#     window1 = Tk()
#     window1.title("New Window")
#     window1.geometry("1920x1280")
#     Label(window1, 
#           text ="HEY").pack()
#     window1.mainloop()

root=Tk()
root.geometry('800x600')
root.title("MY PROGRAM")
mymenu=Menu(root)
root.config(menu=mymenu)

def showhome():
    for widget in root.winfo_children():
        if widget != mymenu:
            widget.destroy()
    lbl=Label(root,text="This is a program coded in python",font=("Consolas",20),height=5).pack()
    image = Image.open("python-logo.png")
    root.image = ImageTk.PhotoImage(image)
    image_label = Label(root, image=root.image)
    image_label.pack()

def showgrade():
    for widget in root.winfo_children():
        if widget != mymenu:
            widget.destroy()
    root.columnconfigure([0,1,2,3,4],minsize=160)
    root.rowconfigure([0,1,2,3,4,5,6,7,8],minsize=50)
    lbl=Label(root,text="กรอกคะแนน",font=("Consolas",20),bg="green",fg="white").grid(row=0,column=2)
    lbl1=Label(root,text="คะแนนสอบกลางภาค :",font=("Consolas",15)).grid(row=1,column=1)
    lbl2=Label(root,text="คะแนนสอบปลายภาค :",font=("Consolas",15)).grid(row=2,column=1)
    def calgrade():
        a=txt1.get()
        b=txt2.get()
        sum=(a+b)
        '''
        if sum>=80:
            grade="A"
        elif sum>=75:
            grade="B+"
        elif sum>=70:
            grade="B"
        elif sum>=65:
            grade="C+"
        elif sum>=60:
            grade="C"
        elif sum>=55:
            grade="D+"
        elif sum>=50:
            grade="D"
        else:
            grade="F"
        '''
        match sum:
            case _ if sum>=80:
                grade="A"
            case _ if sum>=75:
                grade="B+"
            case _ if sum>=70:
                grade="B"
            case _ if sum>=65:
                grade="C+"
            case _ if sum>=60:
                grade="C"
            case _ if sum>=55:
                grade="D+"
            case _ if sum>=50:
                grade="D"
            case _ if sum<50:
                grade="F" 

        lbl3.config(text=f"คะแนนรวมกลางภาค: {a}")
        lbl4.config(text=f"คะแนนรวมปลายภาค: {b}")
        lbl5.config(text=f"คะแนนรวมทั้งหมด: {sum}")
        lbl6.config(text=f"เกรด: {grade}")

    txt1=IntVar()
    txt2=IntVar()
    Mytxt1=Entry(root,textvariable=txt1).grid(row=1, column=2)
    Mytxt2=Entry(root,textvariable=txt2).grid(row=2, column=2)
    btn1=Button(root,command=calgrade,text="คำนวณ").grid(row=3,column=2)
    lbl3 = Label(root,text="",font=("Consolas",15))
    lbl3.grid(row=5,column=2)
    lbl4 = Label(root,text="",font=("Consolas",15))
    lbl4.grid(row=6,column=2)
    lbl5 = Label(root,text="",font=("Consolas",15))
    lbl5.grid(row=7,column=2)
    lbl6 = Label(root,text="",font=("Consolas",15))
    lbl6.grid(row=8,column=2)


def notepad():
    for widget in root.winfo_children():
        if widget != mymenu:
            widget.destroy()
    button = Frame(root)
    button.pack()
    text_area=Text(root,font=("consolas", 12))
    text_area.pack(fill=BOTH,padx=5,pady=5)
    
    def new_file():
        res=messagebox.askquestion(title="เตือน",message="ต้องการสร้างไฟล์ใหม่มั้ย")
        if res == 'yes' :
            text_area.delete(1.0, END)

    def open_file():
        res=messagebox.askquestion(title="เตือน",message="ต้องการเปิดไฟล์หรือไม่")
        if res == 'yes' :
            file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file:
                text_area.delete(1.0, END)
                with open(file, "r") as f:
                    text_area.insert(END, f.read())
            
        

    def save_file():
        res=messagebox.askquestion(title="เตือน",message="ต้องการเซฟไฟล์หรือไม่")
        if res == 'yes' :
            file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file:
                with open(file, "w") as f:
                    f.write(text_area.get(1.0, END))

    Button(button, text="New", width=10, command=new_file).pack(side=LEFT,padx=5, pady=5)
    Button(button, text="Open", width=10, command=open_file).pack(side=LEFT,padx=5, pady=5)
    Button(button, text="Save", width=10, command=save_file).pack(side=LEFT,padx=5, pady=5)

    # submenu = Menu(mymenu)
    # submenu.add_command(label="New", command=new_file)
    # submenu.add_command(label="Open", command=open_file)
    # submenu.add_command(label="Save", command=save_file)

    # mymenu.add_cascade(label="File", menu=submenu)


def task():
    for widget in root.winfo_children():
        if widget != mymenu:
            widget.destroy()

    lbl = Label(root, text="รายการสิ่งที่ต้องทำ", font=("Consolas", 20), height=2)
    lbl.pack()

    frame = Frame(root)
    frame.pack(pady=10)

    listbox = Listbox(frame, width=50, height=15, font=("Consolas", 15))
    listbox.pack(side=LEFT, fill=BOTH)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    entry = Entry(root, font=("Consolas", 15))
    entry.pack(pady=10)

    def add_task():
        task = entry.get()
        if task != "":
            listbox.insert(END, task)
            entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "กรุณากรอกสิ่งที่ต้องทำก่อน")

    def delete_task():
        try:
            selected_task_index = listbox.curselection()[0]
            listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "กรุณาเลือกสิ่งที่ต้องการลบ")

    def clear_all_tasks():
        if messagebox.askyesno("Confirmation", "คุณแน่ใจหรือไม่ว่าต้องการลบรายการทั้งหมด?"):
            listbox.delete(0, END)

    btn_add = Button(root, text="เพิ่ม", font=("Consolas", 15), command=add_task)
    btn_add.pack(pady=5)

    btn_delete = Button(root, text="ลบรายการที่เลือก", font=("Consolas", 15), command=delete_task)
    btn_delete.pack(pady=5)

    btn_clear = Button(root, text="ลบทั้งหมด", font=("Consolas", 15), command=clear_all_tasks)
    btn_clear.pack(pady=5)

def click1():
    res=messagebox.askquestion(title="เตือน ",message="แน่ใจหร่อว่าจะปิด")
    if res == 'yes' :
        root.destroy()
    else :
        messagebox.showinfo('Return', 'ย้อนกลับ')

mymenu.add_cascade(label="HOME",command=showhome())
mymenu.add_cascade(label="Grade",command=showgrade)
notepad_menu = Menu(mymenu)
mymenu.add_cascade(label="Notepad", command=notepad)
mymenu.add_cascade(label="Task", command=task)
mymenu.add_cascade(label="Exit",command=click1)


root.mainloop()