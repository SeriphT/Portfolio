#Sabastian Taton
#March 11, 2019
#GUIs

from tkinter import *
#######EXAMPLES#######
"""Labels"""
# root = Tk()
# root.after(1000, root.config(bg = "green"))
# root.title("this GUI is running at 95 YEETS per YOINK")
# root.geometry("500x500")
#
# app = Frame(root)
# app.grid()
#
# lbl = Label(app, text=" \n ABCDEFGHIJKLMNOPQRSTUVWXYZ \n 1234567890", fg = "dark green", bg = "green", font = "Wingdings 32" )
# lbl.pack()
#
# root.mainloop()

"""Buttons"""
# root = Tk()
#
# root.config(bg = "black")
# root.title("Lzy buttons")
# root.geometry("500x500")
#
# mainframe = Frame(root)
# mainframe.grid()
# mainframe.config(bg = "black")
# bttn1 = Button(mainframe, text = "Button 1", bg = "black", fg = "red")
# bttn1.grid()
# bttn2 = Button(mainframe, text = "Not button 2", bg = "black", fg = "purple")
# bttn2.grid()
# bttn3 = Button(mainframe)
# bttn3.grid()
# bttn3.config(text = "Totally button 1 (3)", bg = "black", fg = "pink")

"""Dividing into Classes"""
# class Application(Frame):
#     def __init__(self,master):
#         super(Application, self).__init__(master)
#         self.grid()
#         self.createWidgets()
#     def createWidgets(self):
#         label = Label(text = "these are buttons")
#         label.grid()
#         self.bttn1 = Button(self)
#         self.bttn1.grid()
#         self.bttn1.config(text = "789", font = "Wingdings 12")
#         self.bttn2 = Button(self)
#         self.bttn2.grid()
#         self.bttn2.config(text="abc", font = "Script 12")
#         self.bttn3 = Button(self)
#         self.bttn3.grid()
#         self.bttn3.config(text = "correct", font = "Algerian 12")
#
# root = Tk()
# root.title("Buttons 2.0")
# root.geometry("200x200")
# app = Application(root)

"""Clicker count"""
# class Application(Frame):
#     def __init__(self, master):
#         super(Application, self).__init__(master)
#         self.grid()
#         self.bttn_clicks = 0
#         self.createWidgets()
#         self.label
#     def createWidgets(self):
#         self.label = Label(text = "\t\t\t\t0")
#         self.label.grid()
#         self.bttn1 = Button(text = "Add")
#         self.bttn1.grid()
#         self.bttn1["command"] = self.add_count
#         self.bttn2 = Button(text="Subtract")
#         self.bttn2.grid()
#         self.bttn2["command"] = self.sub_count
#         self.bttn3 = Button(text="mult by 3")
#         self.bttn3.grid()
#         self.bttn3["command"] = self.multiply_count
#         self.bttn4 = Button(text="Div by 2")
#         self.bttn4.grid()
#         self.bttn4["command"] = self.divide_count
#     def add_count(self):
#         self.bttn_clicks += 1
#         self.label["text"] = "Total Count: " + str(self.bttn_clicks)
#     def sub_count(self):
#         self.bttn_clicks -= 1
#         self.label["text"] = "Total Count: " + str(self.bttn_clicks)
#     def multiply_count(self):
#         self.bttn_clicks *= 3
#         self.label["text"] = "Total Count: " + str(self.bttn_clicks)
#     def divide_count(self):
#             self.bttn_clicks /= 2
#             self.label["text"] = "Total Count: " + str(self.bttn_clicks)
# root = Tk()
# root.title("Counter")
# root.geometry("200x200")
# app = Application(root)

"""Grid layouts"""
# class Application(Frame):
#     def __init__(self,master):
#         super(Application,self).__init__(master)
#         self.grid()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.label = Label(self, text = "Enter password for the secret of life")
#         self.label.grid(row = 0, column = 0, columnspan = 2, sticky = W)
#         self.pw_lbl = Label(self, text = "Password: ")
#         self.pw_lbl.grid(row=2, column=0, sticky=W)
#         self.pw_entry = Entry(self)
#         self.pw_entry.grid(row=2, column=1, sticky=W)
#         self.bttn1 = Button(text = "press to continue",command = self.reveal)
#         self.bttn1.grid(row = 2, column = 1, sticky = W)
#         self.secret = Text(width = 50, height = 2, wrap = WORD)
#         self.secret.grid(row=3, column=0, columnspan=2, sticky=W)
#
#     def reveal(self):
#         password = self.pw_entry.get()
#         if password == "secret":
#             message = "Here's the secret of life.............. 42"
#             self.secret.delete(0.0, END)
#             self.secret.insert(0.0, message)
#         else:
#             message = "That's is not correct. No secrets for you."
#             self.secret.delete(0.0, END)
#             self.secret.insert(0.0, message)

"""Check Boxes and Radio"""
# class Application(Frame):
#     def __init__(self,master):
#         super(Application,self).__init__(master)
#         self.grid()
#         self.createWidgets()
#
#     def createWidgets(self):
#         Label(text = "Choose your favorite movie type").grid(row = 0, column = 0, sticky = W)
#         # Label(text = "Select all that apply:").grid(row = 1,sticky = W)
#
#         # self.action = BooleanVar()
#         # self.romance = BooleanVar()
#         # self.fantasy = BooleanVar()
#
#         # self.check_box_1 = Checkbutton(text = "Action", variable = self.action, command = self.update_text)
#         # self.check_box_1.grid(row = 2,sticky = W)
#         # self.check_box_2 = Checkbutton(text="Romance", variable = self.romance, command = self.update_text)
#         # self.check_box_2.grid(row=3,sticky = W)
#         # self.check_box_3 = Checkbutton(text="Fantasy", variable = self.fantasy, command = self.update_text)
#         # self.check_box_3.grid(row=4,sticky = W)
#         # self.text_box = Text(width = 30, height = 5, wrap = WORD)
#         # self.text_box.grid(row = 5,columnspan = 3,sticky = W)
#
#         self.favorite = StringVar()
#         self.favorite.set(None)
#
#         self.bttn = Radiobutton(text="Action", variable = self.favorite, value = "action", command = self.update_text)
#         self.bttn2 = Radiobutton(text="Comedy", variable = self.favorite, value = "comedy", command = self.update_text)
#         self.bttn3 = Radiobutton(text="Fantasy", variable = self.favorite, value = "fantasy", command = self.update_text)
#         self.bttn.grid()
#         self.bttn2.grid()
#         self.bttn3.grid()
#
#         self.text_box = Text(width=30, height=5, wrap=WORD)
#         self.text_box.grid(row = 5,columnspan = 3,sticky = W)
#     def update_text(self):
#         # likes = ""
#         # if self.action.get():
#         #     likes += "You like action movies\n"
#         # if self.romance.get():
#         #     likes += "You like romance movies\n"
#         # if self.fantasy.get():
#         #     likes += "You like fantasy movies"
#         # self.text_box.delete(0.0, END)
#         # self.text_box.insert(0.0,likes)
#         message = 'Your favorite movie type is '
#         message += self.favorite.get()
#         self.text_box.delete(0.0, END)
#         self.text_box.insert(0.0,message)

"""MAD LIBS"""
class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        Label(self,text = "Enter information to create your story").grid(row = 0,columnspan=3,sticky=W)
        Label(self,text="Noun:").grid(row=1, sticky=W)
        Label(self,text="Verb:").grid(row=2, sticky=W)
        Label(self,text="Person:").grid(row=3, sticky=W)
        Label(self,text= "Select adjectives").grid(row=4, stick=W)
        Label(self,text= "Select one verb").grid(row=5,stick=W)
        Button(self, text = "Click for story", command =self.update_text).grid(row=6, sticky=W)

        self.ent_box_1 = Entry(self).grid(row=1, column=1, sticky=W)
        self.ent_box_2 = Entry(self).grid(row=2, column=1, sticky=W)
        self.ent_box_3 = Entry(self).grid(row=3, column=1, sticky=W)

        self.bouncing = BooleanVar()
        self.ostrobogulus = BooleanVar()
        self.electrifying= BooleanVar()

        self.check_box_1 = Checkbutton(self,text = "bouncing", variable = self.bouncing)
        self.check_box_1.grid(row = 4,column = 1,sticky = W)
        self.check_box_2 = Checkbutton(self,text="ostrobogulus", variable = self.ostrobogulus)
        self.check_box_2.grid(row=4,column=2,sticky = W)
        self.check_box_3 = Checkbutton(self,text="electrifying", variable = self.electrifying)
        self.check_box_3.grid(row=4,column=3,sticky = W)

        self.part = StringVar()
        self.part.set(None)

        self.bttn = Radiobutton(self,text="head", variable=self.part, value="head")
        self.bttn2 = Radiobutton(self,text="index finger", variable = self.part, value = "index finger")
        self.bttn3 = Radiobutton(self,text="patella", variable = self.part, value = "patella")
        self.bttn.grid(row = 5,column = 1,sticky = W)
        self.bttn2.grid(row = 5,column = 2,sticky = W)
        self.bttn3.grid(row = 5,column = 3,sticky = W)


        self.text_box = Text(width = 70, height = 5, wrap = WORD)
        self.text_box.grid(row = 7,columnspan = 3,sticky = W)

    def update_text(self):
        noun = self.ent_box_1.get()
        verb = self.ent_box_2.get()
        person = self.ent_box_3.get()
        body_part = self.part.get()
        adjectives = ""
        if self.electrifying.get():
            adjectives += "electrifying"
        if self.ostrobogulus.get():
            adjectives += "ostrobogulus"
        if self.bouncing.get():
            adjectives += "bouncing"

        story = ""
root = Tk()
root.title("Movie Chooser")
root.geometry()
app = Application(root)
root.mainloop()