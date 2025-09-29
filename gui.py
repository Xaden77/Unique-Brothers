import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from tkcalendar import Calendar
from calc import Calculator

class Win1(tk.Tk):
    def __init__(self,logic):
        super().__init__()
        self.logic=logic
        self.date_var = tk.StringVar()
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()
        self.geometry(f"{self.screenWidth}x{self.screenHeight}")
        self.configure(bg="skyblue")
        img = Image.open(r"C:\Codes\Projects\Ub\img.jpg")
        img = img.resize((self.screenWidth//2, self.screenHeight//4), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)
        imglabel = tk.Label(self, image=self.photo)
        imglabel.pack(pady=10) 
        self.entry = tk.Entry(self, textvariable=self.date_var, font=("Arial", 12),state="readonly",width=14)
        self.submit = tk.Button(self, text="Select Date",width=10,height=1,background="blue",foreground="yellow",activebackground="lightblue",font=("Arial Black", 12), command=self.open_calendar)
        self.submit.place(x=self.screenWidth/5.5,y=self.screenHeight/3)
        self.entry.place(x=self.screenWidth/3.36,y=self.screenHeight/2.92)

    def open_calendar(self):
        self.top = tk.Toplevel(self)  
        self.top.grab_set()          
        self.cal = Calendar(
            self.top,
            selectmode="day",
            date_pattern="dd/mm/yyyy", 
            locale="en_US"
        )
        self.cal.pack(padx=20, pady=20)
        tk.Button(self.top, text="Submit",width=10,height=1,background="blue",foreground="yellow",activebackground="lightblue",font=("Arial Black", 12), command=self.interface).pack(pady=5)

    def interface(self):
        self.submit.config(state="disabled")
        self.date_var.set(self.cal.get_date())
        self.s_no=tk.IntVar(value=1)
        self.sourceCount=tk.StringVar(value=f"Source {self.s_no.get()}")
        self.purchase=tk.StringVar(value="Online Expense")
        self.top.destroy()
        self.frame = tk.Frame(self, bg="skyblue",borderwidth=2,relief="groove")
        self.frame.place(x=self.screenWidth/5.5,y=self.screenHeight/2.5)
        label1 = tk.Label(self.frame, text="Cash Income", background="skyblue", font=("Arial Black", 12))
        self.entry1 = tk.Entry(self.frame)
        label2 = tk.Label(self.frame, text="UPI Income", background="skyblue", font=("Arial Black", 12))
        self.entry2 = tk.Entry(self.frame)
        label6 = tk.Label(self.frame, text="Credit Income", background="skyblue", font=("Arial Black", 12))
        self.entry6 = tk.Entry(self.frame)
        label0= tk.Label(self.frame, textvariable=self.purchase, background="skyblue", font=("Arial Black", 12))
        label3 = tk.Label(self.frame,textvariable=self.sourceCount, background="skyblue", font=("Arial Black", 12))
        self.entry3 = tk.Entry(self.frame)
        label4 = tk.Label(self.frame, text="Amount", background="skyblue", font=("Arial Black", 12))
        self.entry4 = tk.Entry(self.frame)
        label5 = tk.Label(self.frame, text="Cash in hand", background="skyblue", font=("Arial Black", 12))
        self.entry5 = tk.Entry(self.frame)
        donebtn = tk.Button(self.frame,text="Store Data",width=13,height=1,background="blue",foreground="yellow",activebackground="lightblue",font=("Arial Black", 12),command=self.store)
        contbtn = tk.Button(self.frame,text="Add",width=5,height=1,background="blue",foreground="yellow",activebackground="lightblue",font=("Arial Black", 12),command=self.cont)
        killbtn = tk.Button(self.frame,text="Kill Entry",width=13,height=1,background="blue",foreground="yellow",activebackground="lightblue",font=("Arial Black", 12),command=self.kill)
        switchbtn = tk.Button(self.frame,text="Switch",width=10,height=1,background="blue",foreground="yellow",activebackground="lightblue",font=("Arial Black", 12),command=self.switch)
        rembtn = tk.Button(self.frame,text="Remove",width=7,height=1,background="blue",foreground="yellow",activebackground="lightblue",font=("Arial Black", 12),command=self.rem)
        calbtn = tk.Button(self.frame,text="Calculator",width=13,height=1,background="blue",foreground="yellow",activebackground="lightblue",font=("Arial Black", 12),command=self.calc)
        label1.grid(row=0, column=0, sticky="w", pady=5,padx=5,)
        self.entry1.grid(row=0, column=2, pady=5,padx=5)
        label2.grid(row=1, column=0, sticky="w", pady=5,padx=5)
        self.entry2.grid(row=1, column=2, pady=5,padx=5)
        label6.grid(row=2, column=0, sticky="w", pady=5,padx=5)
        self.entry6.grid(row=2, column=2, pady=5,padx=5)
        label0.grid(row=3, column=0,sticky="w", pady=5,padx=5)
        switchbtn.grid(row=3, column=2, pady=5,padx=5)
        label3.grid(row=4, column=0, sticky="w", pady=5,padx=5)
        self.entry3.grid(row=4, column=2, pady=5,padx=5)
        label4.grid(row=5, column=0, sticky="w", pady=5,padx=5)
        self.entry4.grid(row=5, column=2, pady=5,padx=5)
        label5.grid(row=7, column=0, sticky="w", pady=5,padx=5)
        self.entry5.grid(row=7, column=2, pady=5,padx=5)
        rembtn.grid(row=6, column=2,sticky="e",pady=10)
        contbtn.grid(row=6, column=2,sticky="w",pady=10)
        donebtn.grid(row=8, column=0,pady=10,padx=5)
        killbtn.grid(row=8, column=2,pady=10,padx=5)
        calbtn.grid(row=9, column=0,pady=10,padx=0)
        self.view()

    def view(self):
        if hasattr(self, "vframe") and self.vframe.winfo_exists():
            self.vframe.destroy()
        self.vframe = tk.Frame(self, bg="skyblue",borderwidth=2)
        self.vframe.place(x=self.screenWidth/2.5,y=self.screenHeight/3)
        content=self.logic.view()
        contents=tk.StringVar(value=content)
        label=tk.Label(self.vframe, textvariable=contents, background="skyblue", font=("Courier", 12))
        label.pack(side=tk.LEFT)

    def calc(self):
        Calculator(self)
        
    def store(self):
        state=self.logic.store(self.date_var.get(),self.entry1.get(),self.entry2.get(),self.entry3.get(),self.entry4.get(),self.entry5.get(),self.entry6.get(),self.purchase.get())
        if state == 1:
            msg.showwarning("Invalid Entry","Please check your entires")
            return
        if state ==2:
            flag=False
            ch=msg.askyesno("File exists",f"do you want to overite data on{self.date_var.get()}")
            if not ch:
                return
            else:
                flag=True
        state= self.logic.store2(self.date_var.get())     
        if state ==3:
            flag=True
            ch=msg.askyesno("Eroor","Previous day file not found\nContinue with todays as first?")
            if not ch:
                self.kill()
                return
        state=self.logic.store3(self.entry1.get(),self.entry2.get(),self.entry6.get(),self.entry5.get())
        if state==1:
            msg.showinfo("Success",f"file Stored in c:\\ub\\{self.date_var.get()}.docx")
            self.frame.place_forget()
            self.vframe.place_forget()
            self.entry.config(state="normal")
            self.entry.delete(0,tk.END)
            self.entry.config(state="readonly")
            self.submit.config(state="normal")
            self.logic.kill()
        elif state==0:
            msg.showerror("Error","File not stored\nTry Again")
    
    def cont(self):
        state=self.logic.cont(self.entry3.get(),self.entry4.get(),self.purchase.get())
        if state == 1:
            msg.showwarning("Invalid Entry","Please check your entires")
            return
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0,tk.END)
        self.s_no.set(self.s_no.get()+1)
        self.sourceCount.set(f"Source {self.s_no.get()}")
        self.entry3.focus_set()
        self.view()

    def rem(self):
        state=self.logic.rem()
        if state == 1:
            msg.showwarning("Invalid operation","No more data to be reomoved")
            return
        self.view()
        self.s_no.set(self.s_no.get()-1)
        self.sourceCount.set(f"Source {self.s_no.get()}")

    def kill(self):
        ans=msg.askyesno("Warning",f"do you want to terminate entries")
        if ans:
            self.frame.place_forget()
            self.vframe.place_forget()
            self.entry.config(state="normal")
            self.entry.delete(0,tk.END)
            self.entry.config(state="readonly")
            self.submit.config(state="normal")
            self.logic.kill()
        else:
            return

        self.logic.kill()
    
    def switch(self):
        if self.purchase.get()=="Online Expense":
            self.purchase.set("Cash Expense")
        else:
            self.purchase.set("Online Expense")

        self.logic.switch()


if __name__ =="__main__":
    class Test():
        def store(self,test1,test2,test3,test4,test5,test6,test7,test8):
            print("store logic ")
        def store2(self,test1,test2,test3,test4,test5,test6):
            print("store2 executed")
        def cont(self,test1,test2,test3):
            print("continue logic")
        def kill(self):
            print("kill logic")
        def switch(self):
            print("switch logic")
        def rem(self):
            print("remove logic")
        def view(self):
            print("View logic")
            w1, w2, w3 = "Elephant", "Ant", "Dinosaur"
            left_aligned   = f"{w1:<32}{w2:<32}{w3:<32}"
            return left_aligned
    app =Win1(Test())
    app.mainloop()