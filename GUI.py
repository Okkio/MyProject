# MAIN FILE GUI + BACKEND
from VotingInfo import *
from CandidateInstances import *
from HackathonTask1 import *
from tkinter import *
import tkinter.messagebox as tm
import tkinter
import random
import time
import datetime
from tkinter import ttk
import csv


def main():
    root = Tk()

# VoteStart Class : Start Page Of The GUI (Phakonekham Phichit 001041931)
class VoteStart:
    def __init__(self, master):
        self.master = master
        self.master.title("Start Page")
        self.master.geometry("630x500")
        self.master.config(bg='forest green')
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()

        self.lbTitle = Label(self.frame, text="Greenwich Student Union Election Voting", bg="azure", width="350",
                             relief="ridge", height="5", bd=5, font=("Helvetica", 13, "bold")).pack(pady=20)
        self.login_start = Button(self.frame, text="LOGIN", height="2", width="15", bd=3, bg="grey",
                                  font=("Helvetica", 12, "bold"), command=self.wombocombo).pack(pady=10)
        self.Exit = Button(self.frame, text="EXIT", height="2", width="10", bd=3, bg="grey",
                           font=("Helvetica", 10, "bold"), command=self.exit).pack()
        self.comment= Button(self.frame, text="COMMENT", height="2", width="10", bd=3, bg="grey",
                           font=("Helvetica", 10, "bold"), command=self.comment).pack()

    #Exit function to exit the Start page (Phakonekham Phichit 001041931)
    def exit(self):
        self.exit = tm.askyesno("Start Page", "Are You Sure You Want To Exit")
        if self.exit == 1:
            self.destory_window()

            return
    def comment(self):
        self.destory_window()
        task1()

    #This functions does 2 mulitiple functions,
    # this acts as our transition function that closes the previous window and open new window
    def wombocombo(self):
        self.destory_window()
        self.new_window()

        # destory the current window
    def destory_window(self):
        self.master.destroy()
  #Create a new window Tk() window in Login_Account
    def new_window(self):
        self.newWindow = Tk()
        self.app = Login_Account(self.newWindow)

    #destory the current window
    def destory_window(self):
        self.master.destroy()


# Login Screen (Phakonekham Phichit 001041931)
class Login_Account(VoteStart):
    def __init__(self, master):
        self.master = master
        self.master.title("Account_Login")
        self.master.geometry('620x500')
        self.master.config(bg='forest green')
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()

        self.lbAcTitle = Label(self.frame, text="Please Enter Your Details", bg="azure", width="350", relief="ridge",
                               height="5", font=("Helvetica", 15, "bold")).pack(pady=20)

        self.Username = StringVar()
        self.Password = StringVar()

        def return_1(*args):
            self.Login_System()

#Username and Password Entry (Phakonekham Phichit 001041931)
        self.lblUsername = Label(self.frame, text="Username").pack()
        self.txtUsername = Entry(self.frame, textvariable=self.Username, width="20", bd=5).pack(pady=10)

        self.lblPassword = Label(self.frame, text="Password").pack()

        self.txtPassword = Entry(self.frame, textvariable=self.Password, width="20", show="*", bd=5)
        self.txtPassword.bind("<Return>", return_1)
        self.txtPassword.pack(pady=10)

        self.login_start = Button(self.frame, text="LOGIN", height="1", width="15", bd=2,
                                  font=("Helvetica", 12, "bold"), bg="grey", command=self.Login_System).pack(pady=5)

    # Username/Password check (Phakonekham Phichit 001041931)
    def Login_System(self):
        global user
        global password
        user = self.Username.get()
        password = self.Password.get()
# Login credential check (Ahmed Hamad 001049653)
        voters = open("StudentVoters.txt", "r")

        with voters as file:
            for line in file:
                if not user:
                    tm.showerror('Invalid', 'Invalid Username/Password')
                    break

                elif not password:
                    tm.showerror('Invalid', 'Invalid Username/Password')
                    break
                elif user + " " + password in line:
                    superCount()
                    self.PassOrGo()
                    break

            else:
                tm.showerror('Invalid', 'Invalid Username/Password')

    # Marks account as 'Voted' After final submission (Ahmed Hamad 001049653)
    def voted(self):
        voters = open("StudentVoters.txt", "r+")
        voted = open("VotedOrNot.txt", "a")
        global line_2
        for line in voters:
            if user + " " + password in line:
                voted.write(user + " " + "Voted\n")
                break
        voted.close()
#Check if account is marked as 'Voted' (Ahmed Hamad 001049653)
    def PassOrGo(self):
        voted_1 = open("VotedOrNot.txt", "r")
        global hasnotvoted
        for _ in voted_1:
            if user + " " + "Voted" in _:
                result = tm.askquestion("Voting Complete",
                                        "You have already voted, would you like to view the results?", icon='warning')
                if result == 'yes':

                    self.master.destroy()
                    self.newWindow = Tk()
                    self.app = Result(self.newWindow)

                    break
                else:
                    break
        else:
            self.timecheck()

 #Time Restriction Function (Ahmed Hamad 001049653)

    def timecheck(self):
        date1 = datetime.datetime(2021, 1, 29)
        if datetime.datetime.now() < date1:
            tm.showinfo('Login Success', 'Welcome' + " " + user)
            self.destory_window()
            self.new_window()
        else:
            tm.showerror('Election Closed', 'The Election time period has elapsed')

    def new_window(self):
        self.newWindow = Tk()
        self.app = Position(self.newWindow)


# Pick position screen (Phakonekham Phichit 001041931)
class Position(Login_Account):
    def __init__(self, master):
        self.master = master
        self.master.title("Cast Voting Positions")
        self.master.geometry('620x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lbPsTitle = Label(self.frame, text="VOTE YOUR CANDIDATES", width="350", relief="ridge", bg="azure",
                               height="5", font=("Helvetica", 15, "bold")).pack(pady=20)

      #Positions Selection Buttons (Phakonekham Phichit 001041931)

        self.pres_start = Button(self.frame,text="President", height="1", width="25", bd=2,
                                 font=("Helvetica", 12, "bold"), command=self.pre_window)
        self.pres_start.pack(pady=5)

        self.gsu_start = Button(self.frame, text="GSU Officer", height="1", width="25", bd=2,
                                font=("Helvetica", 12, "bold"), command=self.gsu_window)
        self.gsu_start.pack(pady=5)

        self.math_start = Button(self.frame, text="Math Faculty Officer", height="1", width="25", bd=2,
                                 font=("Helvetica", 12, "bold"), command=self.math_window)
        self.math_start.pack(pady=5)

        self.sci_start = Button(self.frame, text="Science Faculty Officer", height="1", width="25", bd=2,
                                font=("Helvetica", 12, "bold"), command=self.sci_window)
        self.sci_start.pack(pady=5)

        self.comp_start = Button(self.frame, text="Computing Faculty Officer", height="1", width="25", bd=2,
                                 font=("Helvetica", 12, "bold"), command=self.comp_window)
        self.comp_start.pack(pady=5)

        self.art_start = Button(self.frame, text="Art Faculty Officer", height="1", width="25", bd=2,
                                font=("Helvetica", 12, "bold"), command=self.art_window)
        self.art_start.pack(pady=5)

        self.cast_submit = Button(self.frame, text="SUBMIT", height="1", width="25", bd=2,

                                 font=("Helvetica", 12, "bold"), bg="grey", command=self.final_submit).pack(pady=5)

        #FUNCTIONS FOR DISABLING AND ENABLING EACH BUTTON RESPECTIVELY (Ahmed Hamad 001049653)
        global disablePres
        def disablePres():
            return self.pres_start.configure(state=DISABLED)


        global disableGsu

        def disableGsu():
            return self.gsu_start.configure(state=DISABLED)

        global disableMath

        def disableMath():
            return self.math_start.configure(state=DISABLED)

        global disableSci

        def disableSci():
            return self.sci_start.configure(state=DISABLED)

        global disableComp

        def disableComp():
            return self.comp_start.configure(state=DISABLED)

        global disableArt

        def disableArt():
            return self.art_start.configure(state=DISABLED)

        global enablePres

        def enablePres():
            return self.pres_start.configure(state=NORMAL)

        global enableGsu

        def enableGsu():
            return self.gsu_start.configure(state=NORMAL)

        global enableMath

        def enableMath():
            return self.math_start.configure(state=NORMAL)

        global enableSci

        def enableSci():
            return self.sci_start.configure(state=NORMAL)

        global enableComp

        def enableComp():
            return self.comp_start.configure(state=NORMAL)

        global enableArt

        def enableArt():
            return self.art_start.configure(state=NORMAL)





      # Create Position Selection Windowws (Phakonekham Phichit 001041931)
    def pre_window(self):
        self.newWindow = Tk()
        self.app = Pres(self.newWindow)
        disablePres()

    def gsu_window(self):
        self.newWindow = Tk()
        self.app = Gsu_off(self.newWindow)
        disableGsu()
    def math_window(self):
        self.newWindow = Tk()
        self.app = Math(self.newWindow)
        disableMath()
    def sci_window(self):
        self.newWindow = Tk()
        self.app = Sci(self.newWindow)
        disableSci()
    def comp_window(self):
        self.newWindow = Tk()
        self.app = Comp(self.newWindow)
        disableComp()
    def art_window(self):
        self.newWindow = Tk()
        self.app = Art(self.newWindow)
        disableArt()
  # Final Vote Submission Function (Ahmed Hamad 001049653)
    def final_submit(self):
        result = tm.askquestion("Confirm", "Are you sure you wish to submit?", icon='warning')
        if result == 'yes':
            tm.showinfo("Voting Complete","Thank you for voting, Login again to view results")
            self.master.destroy()
            with open("VoteSaves.txt", "a") as dumpfile:
                motherlist = [president_votes, gsuofficer_votes, mathfacofficer_votes, compfacofficer_votes,
                              scifacofficer_votes, artfacofficer_votes]
                i = 0
                for _ in motherlist:
                    for _ in motherlist[i]:
                        dumpfile.write(_ + "\n")
                    i += 1
            global count

            superCount()
            self.voted()
        else:
            pass


# President voting screen(Phakonekham Phichit 001041931)
class Pres(Position):
    def __init__(self, master):
        self.master = master
        self.master.title("President")
        self.master.geometry('620x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb1 = Label(self.frame, text="Presidential Candidates", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)

#President voting GUI (Phakonekham Phichit 001041931)
        #List used to display data from class objects (Ahmed Hamad 001049653)
        president_1 = []
        pres1counter = 0
        for _ in presidents:
            president_1.append(presidents[pres1counter].first + " " + presidents[pres1counter].last)
            pres1counter += 1
            
        #President combobocx GUI Phakonekham Phichit 001041931)
        self.presidentselecta = Label(self.frame, text="First Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.president_box = StringVar()
        global president_chosena
        president_chosena = ttk.Combobox(self.frame, width=20, state='readonly')
        president_chosena['values'] = list(president_1)
        president_chosena.pack(side=TOP, fill=X, anchor=W, expand=YES)
        president_chosena.current(0)
        president_chosena.set("")

        self.presidentselectb = Label(self.frame, text="Second Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.president_boxb = StringVar()
        president_chosenb = ttk.Combobox(self.frame, width=20, state='readonly')
        president_chosenb['values'] = list(president_1)
        president_chosenb.pack(side=TOP, fill=X, anchor=W, expand=YES)
        president_chosenb.current(0)
        president_chosenb.set("")

        self.presidentselectc = Label(self.frame, text="Third Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.president_boxc = StringVar()
        president_chosenc = ttk.Combobox(self.frame, width=20, state='readonly')
        president_chosenc['values'] = list(president_1)
        president_chosenc.pack(side=TOP, fill=X, anchor=W, expand=YES)
        president_chosenc.current(0)
        president_chosenc.set("")

        self.presidentselectd = Label(self.frame, text="Fourth Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.president_boxd = StringVar()
        president_chosend = ttk.Combobox(self.frame, width=20, state='readonly')
        president_chosend['values'] = list(president_1)
        president_chosend.pack(side=TOP, fill=X, anchor=W, expand=YES)
        president_chosend.current(0)
        president_chosend.set("")

#Confirm vote (Ahmed Hamad 001049653)

        #President Duplicate Check (Ahmed Hamad 001049653)

        def votecheck():

            result = tm.askquestion("Confirm", "Are you sure you wish to confirm?", icon='warning')
            if result == 'yes':
                votefirst()

            else:
                pass
        def votefirst():
            if "" in {president_chosena.get(), president_chosenb.get(), president_chosenc.get(),
                      president_chosend.get()}:
                tm.showerror('Preference not selected', 'Please select all preferences')
            elif president_chosena.get() in {president_chosenb.get(), president_chosenc.get(), president_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif president_chosenb.get() in {president_chosena.get(), president_chosenc.get(), president_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif president_chosenc.get() in {president_chosena.get(), president_chosenb.get(), president_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif president_chosenb.get() in {president_chosena.get(), president_chosenc.get(), president_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            else:
                president_votes.append("President" + " " + president_chosena.get() + "1st")
                president_votes.append("President" + " " + president_chosenb.get() + "2nd")
                president_votes.append("President" + " " + president_chosenc.get() + "3rd")
                president_votes.append("President" + " " + president_chosend.get() + "4th")
                tm.showinfo('Voting Saved', 'Your votes have been saved')

                self.back_pos1()


        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 10, "bold"), command=self.back_pos).pack(side=LEFT, anchor="sw")



        self.confirm = Button(self.frame, text="Confirm", height="2", width="6", bd=2,
                              font=("Helvetica", 10, "bold"), command=votecheck).pack(side=LEFT, fill=BOTH,expand=YES)

#Functions used for going back in back and confirm button (Ahmed Hamad 001049653)

    def back_pos1(self):
        self.destory_window()
        disablePres()
        return
    def back_pos(self):
        self.destory_window()
        enablePres()

        return


# GSU officer voting screen(Phakonekham Phichit 001041931)
class Gsu_off(Pres):
    def __init__(self, master):
        self.master = master
        self.master.title("GSU Candidates")
        self.master.geometry('620x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb2 = Label(self.frame, text="Greenwich Student Union Candidates", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)


        # List used to display data from class objects (Ahmed Hamad 001049653)
        gsuofficers_1 = []
        gsu1counter = 0
        for _ in gsu_officers:
            gsuofficers_1.append(gsu_officers[gsu1counter].first + " " + gsu_officers[gsu1counter].last)
            gsu1counter += 1

        #GSU Officer(Phakonekham Phichit 001041931)
        self.gsuselecta = Label(self.frame, text="First Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.gsu_box = StringVar()
        gsu_chosena = ttk.Combobox(self.frame, width=20, state='readonly')
        gsu_chosena['values'] = list(gsuofficers_1)
        gsu_chosena.pack(side=TOP, fill=X, anchor=W, expand=YES)
        gsu_chosena.current(0)
        gsu_chosena.set("")

        self.gsuselectb = Label(self.frame, text="Second Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.gsu_boxb = StringVar()
        gsu_chosenb = ttk.Combobox(self.frame, width=20, state='readonly')
        gsu_chosenb['values'] = list(gsuofficers_1)
        gsu_chosenb.pack(side=TOP, fill=X, anchor=W, expand=YES)
        gsu_chosenb.current(0)
        gsu_chosenb.set("")

        self.gsuselectc = Label(self.frame, text="Third Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.gsu_boxc = StringVar()
        gsu_chosenc = ttk.Combobox(self.frame, width=20, state='readonly')
        gsu_chosenc['values'] = list(gsuofficers_1)
        gsu_chosenc.pack(side=TOP, fill=X, anchor=W, expand=YES)
        gsu_chosenc.current(0)
        gsu_chosenc.set("")

        self.gsuselectd = Label(self.frame, text="Fourth Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.gsu_boxd = StringVar()
        gsu_chosend = ttk.Combobox(self.frame, width=20, state='readonly')
        gsu_chosend['values'] = list(gsuofficers_1)
        gsu_chosend.pack(side=TOP, fill=X, anchor=W, expand=YES)
        gsu_chosend.current(0)
        gsu_chosend.set("")

#Confirmation check (Ahmed Hamad 001049653)
        def votecheck():

            result = tm.askquestion("Confirm", "Are you sure you wish to confirm?", icon='warning')
            if result == 'yes':
                votefirst()

            else:
                pass

          #President GSU Officer Duplication Check(Ahmed Hamad 001049653)

        def votefirst():

            if "" in {gsu_chosena.get(), gsu_chosenb.get(), gsu_chosenc.get(), gsu_chosend.get()}:
                tm.showerror('Preference not selected', 'Please select all preferences')
            elif gsu_chosena.get() in {gsu_chosenb.get(), gsu_chosenc.get(), gsu_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif gsu_chosenb.get() in {gsu_chosena.get(), gsu_chosenc.get(), gsu_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif gsu_chosenc.get() in {gsu_chosena.get(), gsu_chosenb.get(), gsu_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif gsu_chosenb.get() in {gsu_chosena.get(), gsu_chosenc.get(), gsu_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            else:
                gsuofficer_votes.append("GSU_Officer" + " " + gsu_chosena.get() + "1st")
                gsuofficer_votes.append("GSU_Officer" + " " + gsu_chosenb.get() + "2nd")
                gsuofficer_votes.append("GSU_Officer" + " " + gsu_chosenc.get() + "3rd")
                gsuofficer_votes.append("GSU_Officer" + " " + gsu_chosend.get() + "4th")
                tm.showinfo('Voting Saved', 'Your votes have been saved')
                self.back_pos1()

        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 10, "bold"), command=self.back_pos).pack(side=LEFT)


        self.confirm = Button(self.frame, text="Confirm", height="2", width="6", bd=2,
                              font=("Helvetica", 10, "bold"), command=votecheck).pack(side=LEFT, fill=BOTH,
                                                                                      expand=YES)

# Functions used for going back in back and confirm button (Ahmed Hamad 001049653)
    def back_pos1(self):
        self.destory_window()
        disableGsu()
        return
    def back_pos(self):
        self.destory_window()
        enableGsu()

        return

#Math Class, Main Window GUI(Phakonekham Phichit 001041931)
class Math(Pres):
    def __init__(self, master):
        self.master = master
        self.master.title("Math Faculty Officer Candidates")
        self.master.geometry('620x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb3 = Label(self.frame, text="Faculty of Mathematics Officer Candidates", width="350", relief="ridge",
                         bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)
        # List used to display data from class objects (Ahmed Hamad 001049653)
        mathfacofficer_1 = []
        mathcounter = 0
        for _ in math_faculty_officers:
            mathfacofficer_1.append(
                math_faculty_officers[mathcounter].first + " " + math_faculty_officers[mathcounter].last)
            mathcounter += 1
#Confirmation check
        def votecheck():

            self.messagebox = tkinter.messagebox
            result = self.messagebox.askquestion("Confirm", "Are you sure you wish to confirm?", icon='warning')
            if result == 'yes':
                votefirst()

            else:
                pass
#Duplication check (Ahmed Hamad 001049653)
        def votefirst():

            if "" in {math_chosena.get(), math_chosenb.get(), math_chosenc.get(), math_chosend.get()}:
                tm.showerror('Preference not selected', 'Please select all preferences')
            elif math_chosena.get() in {math_chosenb.get(), math_chosenc.get(), math_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif math_chosenb.get() in {math_chosena.get(), math_chosenc.get(), math_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif math_chosenc.get() in {math_chosena.get(), math_chosenb.get(), math_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif math_chosenb.get() in {math_chosena.get(), math_chosenc.get(), math_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            else:
                mathfacofficer_votes.append("Math_Faculty_Officer" + " " + math_chosena.get() + "1st")
                mathfacofficer_votes.append("Math_Faculty_Officer" + " " + math_chosenb.get() + "2nd")
                mathfacofficer_votes.append("Math_Faculty_Officer" + " " + math_chosenc.get() + "3rd")
                mathfacofficer_votes.append("Math_Faculty_Officer" + " " + math_chosend.get() + "4th")
                tm.showinfo('Voting Saved', 'Your votes have been saved')
                self.back_pos1()

#Math FAC Combo GUI (Phakonekham Phichit 001041931)
        self.mathselecta = Label(self.frame, text="First Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.math_boxa = StringVar()
        math_chosena = ttk.Combobox(self.frame, width=20, state='readonly')
        math_chosena['values'] = list(mathfacofficer_1)
        math_chosena.pack(side=TOP, fill=X, anchor=W, expand=YES)
        math_chosena.current(0)
        math_chosena.set("")

        self.mathselectb = Label(self.frame, text="Second Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.math_boxb = StringVar()
        math_chosenb = ttk.Combobox(self.frame, width=20, state='readonly')
        math_chosenb['values'] = list(mathfacofficer_1)
        math_chosenb.pack(side=TOP, fill=X, anchor=W, expand=YES)
        math_chosenb.current(0)
        math_chosenb.set("")

        self.mathselectc = Label(self.frame, text="Third Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.math_boxc = StringVar()
        math_chosenc = ttk.Combobox(self.frame, width=20, state='readonly')
        math_chosenc['values'] = list(mathfacofficer_1)
        math_chosenc.pack(side=TOP, fill=X, anchor=W, expand=YES)
        math_chosenc.current(0)
        math_chosenc.set("")

        self.mathselectd = Label(self.frame, text="Fourth Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.math_boxd = StringVar()
        math_chosend = ttk.Combobox(self.frame, width=20, state='readonly')
        math_chosend['values'] = list(mathfacofficer_1)
        math_chosend.pack(side=TOP, fill=X, anchor=W, expand=YES)
        math_chosend.current(0)
        math_chosend.set("")


#Math FAC Button GUI (Phakonekham Phichit 001041931)
        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 10, "bold"), command=self.back_pos).pack(side=LEFT)



        self.confirm = Button(self.frame, text="Confirm", height="2", width="6", bd=2,
                              font=("Helvetica", 10, "bold"), command=votecheck).pack(side=LEFT, fill=BOTH,expand=YES)
#Functions used for going back in back and confirm button (Ahmed Hamad 001049653)
    def back_pos1(self):
        self.destory_window()
        disableMath()
        return

    def back_pos(self):
        self.destory_window()
        enableMath()

        return


#Sci Class, Science Fac officer Main window GUI (Phakonekham Phichit 001041931)

class Sci(Pres):
    def __init__(self, master):
        self.master = master
        self.master.title("Science Faculty Officer Candidates")
        self.master.geometry('620x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb4 = Label(self.frame, text="Faculty of Science Officer Candidates", width="350", relief="ridge",
                         bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)
        # List used to display data from class objects (Ahmed Hamad 001049653)
        scifacofficer_1 = []
        scicounter = 0
        for _ in sci_faculty_officers:
            scifacofficer_1.append(sci_faculty_officers[scicounter].first + " " + sci_faculty_officers[scicounter].last)
            scicounter += 1

#Confirmation check (Ahmed Hamad 001049653)
        def votecheck():

            result = tm.askquestion("Confirm", "Are you sure you wish to confirm?", icon='warning')
            if result == 'yes':
                votefirst()

            else:
                pass
#Duplication check (Ahmed Hamad 001049653)
        def votefirst():

            if "" in {sci_chosena.get(), sci_chosenb.get(), sci_chosenc.get(), sci_chosend.get()}:
                tm.showerror('Preference not selected', 'Please select all preferences')
            elif sci_chosena.get() in {sci_chosenb.get(), sci_chosenc.get(), sci_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif sci_chosenb.get() in {sci_chosena.get(), sci_chosenc.get(), sci_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif sci_chosenc.get() in {sci_chosena.get(), sci_chosenb.get(), sci_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif sci_chosenb.get() in {sci_chosena.get(), sci_chosenc.get(), sci_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            else:
                scifacofficer_votes.append("Science_Faculty_Officer" + " " + sci_chosena.get() + "1st")
                scifacofficer_votes.append("Science_Faculty_Officer" + " " + sci_chosenb.get() + "2nd")
                scifacofficer_votes.append("Science_Faculty_Officer" + " " + sci_chosenc.get() + "3rd")
                scifacofficer_votes.append("Science_Faculty_Officer" + " " + sci_chosend.get() + "4th")
                tm.showinfo('Voting Saved', 'Your votes have been saved')
                self.back_pos1()

#Science FAC Combo GUI (Phakonekham Phichit 001041931)
        self.scisciselecta = Label(self.frame, text="First Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.sci_boxa = StringVar()
        sci_chosena = ttk.Combobox(self.frame, width=20, state='readonly')
        sci_chosena['values'] = list(scifacofficer_1)
        sci_chosena.pack(side=TOP, fill=X, anchor=W, expand=YES)
        sci_chosena.current(0)
        sci_chosena.set("")

        self.sciselectb = Label(self.frame, text="Second Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.sci_boxb = StringVar()
        sci_chosenb = ttk.Combobox(self.frame, width=20, state='readonly')
        sci_chosenb['values'] = list(scifacofficer_1)
        sci_chosenb.pack(side=TOP, fill=X, anchor=W, expand=YES)
        sci_chosenb.current(0)
        sci_chosenb.set("")

        self.sciselectc = Label(self.frame, text="Third Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.sci_boxc = StringVar()
        sci_chosenc = ttk.Combobox(self.frame, width=20, state='readonly')
        sci_chosenc['values'] = list(scifacofficer_1)
        sci_chosenc.pack(side=TOP, fill=X, anchor=W, expand=YES)
        sci_chosenc.current(0)
        sci_chosenc.set("")

        self.sciselectd = Label(self.frame, text="Fourth Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.sci_boxd = StringVar()
        sci_chosend = ttk.Combobox(self.frame, width=20, state='readonly')
        sci_chosend['values'] = list(scifacofficer_1)
        sci_chosend.pack(side=TOP, fill=X, anchor=W, expand=YES)
        sci_chosend.current(0)
        sci_chosend.set("")


#Math FAC Button GUI (Phakonekham Phichit 001041931)

        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 10, "bold"), command=self.back_pos).pack(side=LEFT)



        self.confirm = Button(self.frame, text="Confirm", height="2", width="6", bd=2,
                              font=("Helvetica", 10, "bold"), command=votecheck).pack(side=LEFT, fill=BOTH,expand=YES)
        #Functions used for going back in back and confirm button (Ahmed Hamad 001049653)

    def back_pos1(self):
        self.destory_window()
        disableSci()
        return
    def back_pos(self):
        self.destory_window()
        enableSci()

        return

#Comp Class, Computing Fac officer Main window GUI (Phakonekham Phichit 001041931)

class Comp(Pres):
    def __init__(self, master):
        self.master = master
        self.master.title("Computing Faculty Officer Candidates")
        self.master.geometry('620x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb5 = Label(self.frame, text="Faculty of Computing Officer Candidates", width="350", relief="ridge",
                         bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)
        # List used to display data from class objects (Ahmed Hamad 001049653)
        compfacofficer_1 = []
        compcounter = 0
        for _ in computing_faculty_officers:
            compfacofficer_1.append(
                computing_faculty_officers[compcounter].first + " " + computing_faculty_officers[compcounter].last)
            compcounter += 1


#Confirmation check (Ahmed Hamad 001049653)
        def votecheck():

            result = tm.askquestion("Confirm", "Are you sure you wish to confirm?", icon='warning')
            if result == 'yes':
                votefirst()

            else:
                pass
#Duplication Check (Ahmed Hamad 001049653)
        def votefirst():

            if "" in {comp_chosena.get(), comp_chosenb.get(), comp_chosenc.get(), comp_chosend.get()}:
                tm.showerror('Preference not selected', 'Please select all preferences')
            elif comp_chosena.get() in {comp_chosenb.get(), comp_chosenc.get(), comp_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif comp_chosenb.get() in {comp_chosena.get(), comp_chosenc.get(), comp_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif comp_chosenc.get() in {comp_chosena.get(), comp_chosenb.get(), comp_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif comp_chosenb.get() in {comp_chosena.get(), comp_chosenc.get(), comp_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            else:
                compfacofficer_votes.append("Computing_Faculty_Officer" + " " + comp_chosena.get() + "1st")
                compfacofficer_votes.append("Computing_Faculty_Officer" + " " + comp_chosenb.get() + "2nd")
                compfacofficer_votes.append("Computing_Faculty_Officer" + " " + comp_chosenc.get() + "3rd")
                compfacofficer_votes.append("Computing_Faculty_Officer" + " " + comp_chosend.get() + "4th")
                tm.showinfo('Voting Saved', 'Your votes have been saved')
                self.back_pos1()

#Comp FAC Combo GUI  (Phakonekham Phichit 001041931)
        self.compselecta = Label(self.frame, text="First Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.comp_boxa = StringVar()
        comp_chosena = ttk.Combobox(self.frame, width=20, state='readonly')
        comp_chosena['values'] = list(compfacofficer_1)
        comp_chosena.pack(side=TOP, fill=X, anchor=W, expand=YES)
        comp_chosena.current(0)
        comp_chosena.set("")

        self.compselectb = Label(self.frame, text="Second Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.comp_boxb = StringVar()
        comp_chosenb = ttk.Combobox(self.frame, width=20, state='readonly')
        comp_chosenb['values'] = list(compfacofficer_1)
        comp_chosenb.pack(side=TOP, fill=X, anchor=W, expand=YES)
        comp_chosenb.current(0)
        comp_chosenb.set("")

        self.compselectc = Label(self.frame, text="Third Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.comp_boxc = StringVar()
        comp_chosenc = ttk.Combobox(self.frame, width=20, state='readonly')
        comp_chosenc['values'] = list(compfacofficer_1)
        comp_chosenc.pack(side=TOP, fill=X, anchor=W, expand=YES)
        comp_chosenc.current(0)
        comp_chosenc.set("")

        self.compselectd = Label(self.frame, text="Fourth Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.comp_boxd = StringVar()
        comp_chosend = ttk.Combobox(self.frame, width=20, state='readonly')
        comp_chosend['values'] = list(compfacofficer_1)
        comp_chosend.pack(side=TOP, fill=X, anchor=W, expand=YES)
        comp_chosend.current(0)
        comp_chosend.set("")

#Comp FAC Button GUI (Phakonekham Phichit 001041931)

        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 10, "bold"), command=self.back_pos).pack(side=LEFT)



        self.confirm = Button(self.frame, text="Confirm", height="2", width="6", bd=2,
                              font=("Helvetica", 10, "bold"), command=votecheck).pack(side=LEFT, fill=BOTH,
                                                                                      expand=YES)
# Functions used for going back in back and confirm button (Ahmed Hamad 001049653)                                                                                     expand=YES)

    def back_pos1(self):
        self.destory_window()
        disableComp()
        return

    def back_pos(self):
        self.destory_window()
        enableComp()

        return


# Art Class,Fac officer GUI (Phakonekham Phichit 001041931)

class Art(Pres):
    def __init__(self, master):
        self.master = master
        self.master.title("Art Faculty Officer Candidates")
        self.master.geometry('620x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb6 = Label(self.frame, text="Faculty of Art Officer Candidates", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)
        # List used to display data from class objects (Ahmed Hamad 001049653)
        artfacofficer_1 = []
        artcounter = 0
        for _ in art_faculty_officers:
            artfacofficer_1.append(art_faculty_officers[artcounter].first + " " + art_faculty_officers[artcounter].last)
            artcounter += 1

#Confirmation check (Ahmed Hamad 001049653)
        def votecheck():

            result = tm.askquestion("Confirm", "Are you sure you wish to confirm?", icon='warning')
            if result == 'yes':
                votefirst()

            else:
                pass
#(Ahmed Hamad 001049653)
        def votefirst():

            if "" in {art_chosena.get(), art_chosenb.get(), art_chosenc.get(), art_chosend.get()}:
                tm.showerror('Preference not selected', 'Please select all preferences')
            elif art_chosena.get() in {art_chosenb.get(), art_chosenc.get(), art_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif art_chosenb.get() in {art_chosena.get(), art_chosenc.get(), art_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif art_chosenc.get() in {art_chosena.get(), art_chosenb.get(), art_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            elif art_chosenb.get() in {art_chosena.get(), art_chosenc.get(), art_chosend.get()}:
                tm.showerror('Duplicates found', 'There are duplicate votes!')
            else:
                artfacofficer_votes.append("Art_Faculty_Officer" + " " + art_chosena.get() + "1st")
                artfacofficer_votes.append("Art_Faculty_Officer" + " " + art_chosenb.get() + "2nd")
                artfacofficer_votes.append("Art_Faculty_Officer" + " " + art_chosenc.get() + "3rd")
                artfacofficer_votes.append("Art_Faculty_Officer" + " " + art_chosend.get() + "4th")
                tm.showinfo('Voting Saved', 'Your votes have been saved')
                self.back_pos1()

#Art FAC Combo GUI (Phakonekham Phichit 001041931)

        self.artselecta = Label(self.frame, text="First Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.art_boxa = StringVar()
        art_chosena = ttk.Combobox(self.frame, width=20, state='readonly')
        art_chosena['values'] = list(artfacofficer_1)
        art_chosena.pack(side=TOP, fill=X, anchor=W, expand=YES)
        art_chosena.current(0)
        art_chosena.set("")

        self.artselectb = Label(self.frame, text="Second Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.art_boxb = StringVar()
        art_chosenb = ttk.Combobox(self.frame, width=20, state='readonly')
        art_chosenb['values'] = list(artfacofficer_1)
        art_chosenb.pack(side=TOP, fill=X, anchor=W, expand=YES)
        art_chosenb.current(0)
        art_chosenb.set("")

        self.artselectc = Label(self.frame, text="Third Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.art_boxc = StringVar()
        art_chosenc = ttk.Combobox(self.frame, width=20, state='readonly')
        art_chosenc['values'] = list(artfacofficer_1)
        art_chosenc.pack(side=TOP, fill=X, anchor=W, expand=YES)
        art_chosenc.current(0)
        art_chosenc.set("")

        self.artselectd = Label(self.frame, text="Fourth Peference").pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.art_boxd = StringVar()
        art_chosend = ttk.Combobox(self.frame, width=20, state='readonly')
        art_chosend['values'] = list(artfacofficer_1)
        art_chosend.pack(side=TOP, fill=X, anchor=W, expand=YES)
        art_chosend.current(0)
        art_chosend.set("")

#Art FAC Button GUI (Phakonekham Phichit 001041931)
        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 10, "bold"), command=self.back_pos).pack(side=LEFT)



        self.confirm = Button(self.frame, text="Confirm", height="2", width="6", bd=2,
                              font=("Helvetica", 10, "bold"), command=votecheck).pack(side=LEFT, fill=BOTH,
                                                                                      expand=YES)
# Functions used for going back in back and confirm button (Ahmed Hamad 001049653)                                                                                     expand=YES)

    def back_pos1(self):
        self.destory_window()
        disableArt()
        return

    def back_pos(self):
        self.destory_window()
        enableArt()

        return


#Results Class, Results screen (submit button) (Phakonekham Phichit 001041931)
class Result():
    def __init__(self, master):
        self.master = master
        self.master.title("Voting Results")
        self.master.geometry('620x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb6 = Label(self.frame, text="Results", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=10)

        self.sum_final = Button(self.frame, text="Summary", height="1", width="25", bd=2,
                                font=("Helvetica", 12, "bold"), command=self.summary).pack(pady=5)

        self.pres_final = Button(self.frame, text="President", height="1", width="25", bd=2,
                                 font=("Helvetica", 12, "bold"), command=self.pre_sum).pack(pady=5)

        self.gsu_final = Button(self.frame, text="GSU Officer", height="1", width="25", bd=2,
                                font=("Helvetica", 12, "bold"), command=self.gsu_sum).pack(pady=5)

        self.math_final = Button(self.frame, text="Math Faculty Officer", height="1", width="25", bd=2,
                                 font=("Helvetica", 12, "bold"), command=self.math_sum).pack(pady=5)

        self.sci_final = Button(self.frame, text="Science Faculty Officer", height="1", width="25", bd=2,
                                font=("Helvetica", 12, "bold"), command=self.sci_sum).pack(pady=5)

        self.comp_final = Button(self.frame, text="Computing Faculty Officer", height="1", width="25", bd=2,
                                 font=("Helvetica", 12, "bold"), command=self.comp_sum).pack(pady=5)

        self.art_final = Button(self.frame, text="Art Faculty Officer", height="1", width="25", bd=2,
                                font=("Helvetica", 12, "bold"), command=self.art_sum).pack(pady=5)

        self.exit = Button(self.frame, text="Exit", height="1", width="25", bd=2,
                           font=("Helvetica", 12, "bold"), bg="grey", command=self.master.destroy).pack(pady=5)

#Create new windows for the resulted poositions from Cast Voting and Count  (Phakonekham Phichit 001041931)

    def back_sum(self):
        self.master.destroy()
        self.result_page()
        return

    def result_page(self):
        self.newWindow = Tk()
        self.app = Result(self.newWindow)

    def summary(self):
        self.master.destroy()
        self.newWindow = Tk()
        self.app = Sum(self.newWindow)

    def pre_sum(self):
        self.master.destroy()
        self.newWindow = Tk()
        self.app = Pres_sum(self.newWindow)

    def gsu_sum(self):
        self.master.destroy()
        self.newWindow = Tk()
        self.app = Gsu_sum(self.newWindow)

    def math_sum(self):
        self.master.destroy()
        self.newWindow = Tk()
        self.app = Math_sum(self.newWindow)

    def sci_sum(self):
        self.master.destroy()
        self.newWindow = Tk()
        self.app = Sci_sum(self.newWindow)

    def comp_sum(self):
        self.master.destroy()
        self.newWindow = Tk()
        self.app = Comp_sum(self.newWindow)

    def art_sum(self):
        self.master.destroy()
        self.newWindow = Tk()
        self.app = Art_sum(self.newWindow)

#Sum Class, Summary Window Main GUI (Phakonekham Phichit 001041931)

class Sum(Result):
    def __init__(self, master):
        self.master = master
        self.master.title("Summary Winners")
        self.master.geometry('1000x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb6 = Label(self.frame, text="Summary", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)

        tl_cols = ("Position", "Candidates")

        self.box = ttk.Treeview(self.frame, columns=tl_cols, show="headings")
        for col in tl_cols:
            self.box.heading(col, text=col)
            self.box.column(col, anchor=CENTER)
#Display summary (Ahmed Hamad 001049653)
        i = 0
        temppos = ["President", "GSU Officer 1", "GSU Officer 2", "GSU Officer 3", "Math Faculty Officer",
                   "Computing Faculty Officer", "Science Faculty Officer", "Art Faculty Officer"]
        for _ in collective_display:
            if temppos[i] == "GSU Officer 2":
                Name1, firstpref1, secondpref1, thirdpref1, fourthpref1 = \
                    sorted(globals()[collective_display[i]], key=splitListWin, reverse=TRUE)[1].split('/')
                self.box.insert("", "end", values=(temppos[i], Name1))
            elif temppos[i] == "GSU Officer 3":
                Name1, firstpref1, secondpref1, thirdpref1, fourthpref1 = \
                    sorted(globals()[collective_display[i]], key=splitListWin, reverse=TRUE)[2].split('/')
                self.box.insert("", "end", values=(temppos[i], Name1))
            else:

                Name1, firstpref1, secondpref1, thirdpref1, fourthpref1 = \
                    sorted(globals()[collective_display[i]], key=splitListWin, reverse=TRUE)[0].split('/')
                self.box.insert("", "end", values=(temppos[i], Name1))
            i += 1


        self.box.pack(fill=BOTH)



        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 8, "bold"), command=self.back_sum).pack(pady=15, side=LEFT)

        self.savenprint = Button(self.frame, text="Print", height="2", width="6", bd=2,
                                 font=("Helvetica", 8, "bold"), command=self.printSummary).pack(pady=15, side=RIGHT)
        #Function for printing summary to text file (Ahmed Hamad 001049653)
    def printSummary(self):

        summary_1 = open("Final Results.txt", "w")

        i = 0
        temppos = ["President", "GSU Officer 1", "GSU Officer 2", "GSU Officer 3", "Math Faculty Officer",
                   "Computing Faculty Officer", "Science Faculty Officer", "Art Faculty Officer"]
        for _ in collective_display:
            Name1, firstpref1, secondpref1, thirdpref1, fourthpref1 = \
                sorted(globals()[collective_display[i]], key=splitListWin, reverse=TRUE)[0].split('/')
            summary_1.write(temppos[i] +" "+ Name1 + "\n")
            i += 1
        tm.showinfo('Print Success', 'The voting summary has been printed to Final Results.txt')

#Pres_Sum, President results Window Main GUI (Phakonekham Phichit 001041931)

class Pres_sum(Result):
    def __init__(self, master):
        self.master = master
        self.master.title("President Winner")
        self.master.geometry('1000x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb6 = Label(self.frame, text="President", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)

        tl_cols3 = ("Candidates", "First Preference", "Second Preference", "Third Preference", "Fourth Preference")

        self.box = ttk.Treeview(self.frame, columns=tl_cols3, show="headings")
        for col in tl_cols3:
            self.box.heading(col, text=col)
            self.box.column(col, anchor=CENTER)
#Displaying president vote data (Ahmed Hamad 001049653)
        sum = 0

        for _ in presidents_display:
            Name, firstpref, secondpref, thirdpref, fourthpref = _.split('/')
            self.box.insert("", "end", values=(Name, firstpref, secondpref, thirdpref, fourthpref))
            sum = int(firstpref) + int(secondpref) + int(thirdpref) + int(fourthpref)

        Name1, firstpref1, secondpref1, thirdpref1, fourthpref1 = \
        sorted(presidents_display, key=splitListWin, reverse=TRUE)[0].split('/')

        if float(sum) <= 0:
            percent1 = 0
        else:
            percent1 = (float(firstpref1) / float(sum)) * 100

        self.box.pack(fill=BOTH)

        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 8, "bold"), command=self.back_sum).pack(pady=15, side=LEFT)

        self.lba = Label(self.frame, text="Winner:" + " " + Name1, width="10", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbb = Label(self.frame, text="Votes Received:" + " " + firstpref1, width="20", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbc = Label(self.frame, text="Total votes cast overall: %s" % (sum), width="25", relief="ridge",
                         bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbd = Label(self.frame, text=" Winner's Total Vote Percentage: %s" % int((percent1))+"%", width="30",
                         relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.savenprint = Button(self.frame, text="Print", height="2", width="6", bd=2,
                                 font=("Helvetica", 8, "bold")).pack(pady=15, side=RIGHT)

#Pres_Sum, GSU results Window Main GUI (Phakonekham Phichit 001041931)
class Gsu_sum(Result):
    def __init__(self, master):
        self.master = master
        self.master.title("Greenwich Student Union Winner")
        self.master.geometry('1000x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb6 = Label(self.frame, text="Greenwich Student Union Officer", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)

        tl_cols2 = ("Candidates", "First Preference", "Second Preference", "Third Preference", "Fourth Preference")

        self.box = ttk.Treeview(self.frame, columns=tl_cols2, show="headings")
        for col in tl_cols2:
            self.box.heading(col, text=col)
            self.box.column(col, anchor=CENTER)
    # Displaying gsuofficer vote data (Ahmed Hamad 001049653)
        sum = 0
        for _ in gsu_officers_display:
            Name, firstpref, secondpref, thirdpref, fourthpref = _.split('/')
            self.box.insert("", "end", values=(Name, firstpref, secondpref, thirdpref, fourthpref))
            sum = int(firstpref) + int(secondpref) + int(thirdpref) + int(fourthpref)

        Name1, firstpref1, secondpref1, thirdpref1, fourthpref1 = \
            sorted(gsu_officers_display, key=splitListWin, reverse=TRUE)[0].split('/')

        if float(sum) <= 0:
            percent1 = 0
        else:
            percent1 = (float(firstpref1) / float(sum)) * 100
        self.box.pack(fill=BOTH)

        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 8, "bold"), command=self.back_sum).pack(pady=15, side=LEFT)

        self.lba = Label(self.frame, text="Winner:" + " " + Name1, width="10", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbb = Label(self.frame, text="Votes Received:" + " " + firstpref1, width="20", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbc = Label(self.frame, text="Total votes cast overall: %s" % (sum), width="25", relief="ridge",
                         bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbd = Label(self.frame, text=" Winner's Total Vote Percentage: %s" % int((percent1))+"%", width="30",
                         relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

#Math_sum Class, Math results Window Main GUI (Phakonekham Phichit 001041931)
class Math_sum(Result):
    def __init__(self, master):
        self.master = master
        self.master.title("Mathematics Faculty Winner")
        self.master.geometry('1000x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb6 = Label(self.frame, text="Faculty of Mathematics", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)

        tl_cols1 = ("Candidates", "First Preference", "Second Preference", "Third Preference", "Fourth Preference")

        self.box = ttk.Treeview(self.frame, columns=tl_cols1, show="headings")
        for col in tl_cols1:
            self.box.heading(col, text=col)
            self.box.column(col, anchor=CENTER)
            # Displaying math officer vote data (Ahmed Hamad 001049653)
        sum = 0
        for _ in math_faculty_officers_display:
            Name, firstpref, secondpref, thirdpref, fourthpref = _.split('/')
            self.box.insert("", "end", values=(Name, firstpref, secondpref, thirdpref, fourthpref))
            sum = int(firstpref) + int(secondpref) + int(thirdpref) + int(fourthpref)

        Name1, firstpref1, secondpref1, thirdpref1, fourthpref1 = \
            sorted(math_faculty_officers_display, key=splitListWin, reverse=TRUE)[0].split('/')

        if float(sum) <= 0:
            percent1 = 0
        else:
            percent1 = (float(firstpref1) / float(sum)) * 100

        self.box.pack(fill=BOTH)

        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 8, "bold"), command=self.back_sum).pack(pady=15, side=LEFT)

        self.lba = Label(self.frame, text="Winner:" + " " + Name1, width="10", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbb = Label(self.frame, text="Votes Received:" + " " + firstpref1, width="20", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbc = Label(self.frame, text="Total votes cast overall: %s" % (sum), width="25", relief="ridge",
                         bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbd = Label(self.frame, text=" Winner's Total Vote Percentage: %s" % int((percent1))+"%", width="30",
                         relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

#Sci_sum class, Science Faculty results Window Main GUI (Phakonekham Phichit 001041931)
class Sci_sum(Result):
    def __init__(self, master):
        self.master = master
        self.master.title("Science Faculty Winner")
        self.master.geometry('1000x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb6 = Label(self.frame, text="Faculty of Science ", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)

        tl_colsa = ("Candidates", "First Preference", "Second Preference", "Third Preference", "Fourth Preference")

        self.box = ttk.Treeview(self.frame, columns=tl_colsa, show="headings")
        for col in tl_colsa:
            self.box.heading(col, text=col, anchor=CENTER)
        self.box.pack(fill=BOTH)
        # Displaying science officer vote data (Ahmed Hamad 001049653)
        sum = 0

        for _ in sci_faculty_officers_display:
            Name, firstpref, secondpref, thirdpref, fourthpref = _.split('/')
            self.box.insert("", "end", values=(Name, firstpref, secondpref, thirdpref, fourthpref))
            sum = int(firstpref) + int(secondpref) + int(thirdpref) + int(fourthpref)

        Name1, firstpref1, secondpref1, thirdpref1, fourthpref1 = \
            sorted(sci_faculty_officers_display, key=splitListWin, reverse=TRUE)[0].split('/')

        if float(sum) <= 0:
            percent1 = 0
        else:
            percent1 = (float(firstpref1) / float(sum)) * 100

        self.box.pack(fill=BOTH)

        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 8, "bold"), command=self.back_sum).pack(pady=15, side=LEFT)

        self.lba = Label(self.frame, text="Winner:" + " " + Name1, width="10", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbb = Label(self.frame, text="Votes Received:" + " " + firstpref1, width="20", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbc = Label(self.frame, text="Total votes cast overall: %s" % (sum), width="25", relief="ridge",
                         bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbd = Label(self.frame, text=" Winner's Total Vote Percentage: %s" % int((percent1))+"%", width="30",
                         relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

#Comp_sum Class, Computing Faculty results Window Main GUI (Phakonekham Phichit 001041931)
class Comp_sum(Result):
    def __init__(self, master):
        self.master = master
        self.master.title("Computing Faculty Winner")
        self.master.geometry('1000x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb6 = Label(self.frame, text="Faculty of Computing", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)

        tl_colsb = ("Candidates", "First Preference", "Second Preference", "Third Preference", "Fourth Preference")

        self.box = ttk.Treeview(self.frame, columns=tl_colsb, show="headings")
        for col in tl_colsb:
            self.box.heading(col, text=col, anchor=CENTER)
        self.box.pack(fill=BOTH)
        # Displaying computing officer vote data (Ahmed Hamad 001049653)
        sum = 0

        for _ in computing_faculty_officers_display:
            Name, firstpref, secondpref, thirdpref, fourthpref = _.split('/')
            self.box.insert("", "end", values=(Name, firstpref, secondpref, thirdpref, fourthpref))
            sum = int(firstpref) + int(secondpref) + int(thirdpref) + int(fourthpref)

        Name1, firstpref1, secondpref1, thirdpref1, fourthpref1 = \
            sorted(computing_faculty_officers_display, key=splitListWin, reverse=TRUE)[0].split('/')

        if float(sum) <= 0:
            percent1 = 0
        else:
            percent1 = (float(firstpref1) / float(sum)) * 100

        self.box.pack(fill=BOTH)

        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 8, "bold"), command=self.back_sum).pack(pady=15, side=LEFT)

        self.lba = Label(self.frame, text="Winner:" + " " + Name1, width="10", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbb = Label(self.frame, text="Votes Received:" + " " + firstpref1, width="20", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbc = Label(self.frame, text="Total votes cast overall: %s" % (sum), width="25", relief="ridge",
                         bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbd = Label(self.frame, text=" Winner's Total Vote Percentage: %s" % int((percent1))+"%", width="30",
                         relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

#Art_sum Class, Art Faculty results Window Main GUI (Phakonekham Phichit 001041931)
class Art_sum(Result):
    def __init__(self, master):
        self.master = master
        self.master.title("Art Faculty Winner")
        self.master.geometry('1000x500')
        self.master.config(bg="forest green")
        self.frame = Frame(self.master, bg='forest green')
        self.frame.pack()
        self.lb6 = Label(self.frame, text="Faculty of Art", width="350", relief="ridge", bg="azure",
                         height="5", font=("Helvetica", 15, "bold")).pack(pady=20)

        tl_colsc = ("Candidates", "First Preference", "Second Preference", "Third Preference", "Fourth Preference")

        self.box = ttk.Treeview(self.frame, columns=tl_colsc, show="headings")
        for col in tl_colsc:
            self.box.heading(col, text=col, anchor=CENTER)
        self.box.pack(fill=BOTH)
        # Displaying art officer vote data (Ahmed Hamad 001049653)
        sum = 0

        for _ in art_faculty_officers_display:
            Name, firstpref, secondpref, thirdpref, fourthpref = _.split('/')
            self.box.insert("", "end", values=(Name, firstpref, secondpref, thirdpref, fourthpref))
            sum = int(firstpref) + int(secondpref) + int(thirdpref) + int(fourthpref)

        Name1, firstpref1, secondpref1, thirdpref1, fourthpref1 = \
            sorted(art_faculty_officers_display, key=splitListWin, reverse=TRUE)[0].split('/')

        if float(sum) <= 0:
            percent1 = 0
        else:
            percent1 = (float(firstpref1) / float(sum)) * 100

        self.box.pack(fill=BOTH)

        self.back = Button(self.frame, text="Back", height="2", width="6", bd=2,
                           font=("Helvetica", 8, "bold"), command=self.back_sum).pack(pady=15, side=LEFT)

        self.lba = Label(self.frame, text="Winner:" + " " + Name1, width="10", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbb = Label(self.frame, text="Votes Received:" + " " + firstpref1, width="20", relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbc = Label(self.frame, text="Total votes cast overall: %s" % (sum), width="25", relief="ridge",
                         bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)

        self.lbd = Label(self.frame, text=" Winner's Total Vote Percentage: %s" % int((percent1))+"%", width="30",
                         relief="ridge", bg="azure",
                         height="2", font=("Helvetica", 8, "bold")).pack(side=LEFT, fill=X, anchor=W, expand=YES)


#Main Window Module(Phakonekham Phichit 001041931)

if __name__ == '__main__':
    root = Tk()
    app = VoteStart(root)
    root.mainloop()
