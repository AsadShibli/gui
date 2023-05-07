from tkinter import *
from dbhelper import Database
from tkinter import messagebox
from myapi import API
class NLPApp:
    def __init__(self):
        self.root = Tk()
        self.dbo = Database()
        self.apio = API()
        self.root.iconbitmap("resources/favicon.ico")
        self.root.title("NLPApp")
        self.root.configure(bg="#34495E")
        self.root.geometry("350x600")
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):

        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text="Enter email")
        label1.pack(pady=(5,10))
        self.email_input = Entry(self.root,width=45)
        self.email_input.pack(pady=(10,10),ipady=4)

        label2 = Label(self.root, text="Enter password")
        label2.pack(pady=(5, 10))
        self.password_input = Entry(self.root, width=45,show="*")
        self.password_input.pack(pady=(10, 10), ipady=4)

        login_btn = Button(self.root , text="Login",width=20,height=1,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text="Not a member ?")
        label3.pack(pady=(5, 10))

        register_btn = Button(self.root , text="register",width=20,height=1,command=self.register_gui)
        register_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text="Enter email")
        label1.pack(pady=(5, 10))
        self.email_input = Entry(self.root, width=45)
        self.email_input.pack(pady=(10, 10), ipady=4)

        label2 = Label(self.root, text="Enter name")
        label2.pack(pady=(5, 10))
        self.name_input = Entry(self.root, width=45)
        self.name_input.pack(pady=(10, 10), ipady=4)

        label3 = Label(self.root, text="Enter password")
        label3.pack(pady=(5, 10))
        self.password_input = Entry(self.root, width=45, show="*")
        self.password_input.pack(pady=(10, 10), ipady=4)

        login_btn = Button(self.root, text="Register", width=20, height=1,command=self.perform_register)
        login_btn.pack(pady=(10, 10))

        label4 = Label(self.root, text="Already registered ?")
        label4.pack(pady=(5, 10))

        register_btn = Button(self.root, text="Login now", width=20, height=1, command=self.login_gui)
        register_btn.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_register(self):
        email = self.email_input.get()
        name = self.name_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(email,name,password)

        if response:
            messagebox.showinfo("success","registration successful")
        else:
            messagebox.showerror("error","already email exists")

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo("success", "login successful")
            self.home_gui()
        else:
            messagebox.showerror("error", "login failed")

    def home_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=20, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        NER_btn = Button(self.root, text="Name Entity Analysis", width=20, height=4, command=self.NER_gui)
        NER_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text="Emotion Detect", width=20, height=4, command=self.Emotion_gui)
        emotion_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        heading2 = Label(self.root,text='Sentiment Analysis',bg='#34495E',fg='white')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana',20))

        label1 = Label(self.root, text="Enter Text")
        label1.pack(pady=(5, 10))
        self.sentiment_input = Entry(self.root, width=45)
        self.sentiment_input.pack(pady=(10, 10), ipady=4)

        Analysis_btn = Button(self.root, text="Analysis", width=20, height=1, command=self.sentiment_analysis)
        Analysis_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root,text='', bg="#34495E",fg="white")
        self.sentiment_result.pack()
        self.sentiment_result.configure(font=('verdana', 15))

        goback_btn = Button(self.root, text="Go Back", width=20, height=1, command=self.home_gui)
        goback_btn.pack(pady=(0, 10))

    def sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt =''
        for i in result['sentiment']:
            txt=  txt + (i)+"->"+ str(result['sentiment'][i])+ "\n"

        self.sentiment_result['text'] = txt
    def NER_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text="Enter Text")
        label1.pack(pady=(5, 10))
        self.ner_input = Entry(self.root, width=45)
        self.ner_input.pack(pady=(10, 10), ipady=4)

        Analysis_btn = Button(self.root, text="Analysis", width=20, height=1, command=self.ner_analysis)
        Analysis_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg="#34495E", fg="white")
        self.ner_result.pack()
        self.ner_result.configure(font=('verdana', 12))

        goback_btn = Button(self.root, text="Go Back", width=20, height=1, command=self.home_gui)
        goback_btn.pack(pady=(0, 10))

    def ner_analysis(self):
        text = self.ner_input.get()
        result = self.apio.NER_analysis(text)

        txt =''
        for i in result['entities']:
            for j in i:
                txt=  txt +  j + ":"+str(i[j])+"\n"
            txt += "\n\n"

        self.ner_result['text'] = txt

    def Emotion_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Detact', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text="Enter Text")
        label1.pack(pady=(5, 10))
        self.emotion_input = Entry(self.root, width=45)
        self.emotion_input.pack(pady=(10, 10), ipady=4)

        Analysis_btn = Button(self.root, text="Analysis", width=20, height=1, command=self.emotion_detact)
        Analysis_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg="#34495E", fg="white")
        self.emotion_result.pack(pady=(10,10))
        self.emotion_result.configure(font=('verdana', 12))

        goback_btn = Button(self.root, text="Go Back", width=20, height=1, command=self.home_gui)
        goback_btn.pack(pady=(0, 10))

    def emotion_detact(self):
        text = self.emotion_input.get()
        result = self.apio.emotion_detect(text)

        txt = ''
        for i in result['emotion']:
            txt += i + ":" + str(result['emotion'][i])+"\n\n"

        self.emotion_result['text'] = txt

nlp = NLPApp()
