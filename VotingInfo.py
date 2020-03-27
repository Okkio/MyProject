# VOTING AND COUNTING VOTES
from GUI import *
#Lists holding all votes temporarily Ahmed Hamad 001049653
president_votes = []
gsuofficer_votes = []
compfacofficer_votes = []
scifacofficer_votes = []
mathfacofficer_votes = []
artfacofficer_votes = []
Final_Tally = []


# COUNTING FUNCTIONS
#Function to run all counting functions Ahmed Hamad 001049653
def superCount():
    count()
    countpres()
    countgsu()
    countcomp()
    countart()
    countmath()
    countsci()
    orderVotes()

#Export votes after finally submitting Ahmed Hamad 001049653
def count():
    with open("VoteSaves.txt", "r") as undumpfile:
        for _ in undumpfile:
            Final_Tally.append(_)

#Count votes for each position functions below Ahmed Hamad 001049653
def countpres():
    counter = 0

    for _ in presidents:
        presidents[counter].resetPref()
        for line in Final_Tally:
            if presidents[counter].position + " " + presidents[counter].first + " " + presidents[
                counter].last + "1st" in line:
                presidents[counter].incrementPref("1st")
            elif presidents[counter].position + " " + presidents[counter].first + " " + presidents[
                counter].last + "2nd" in line:
                presidents[counter].incrementPref("2nd")
            elif presidents[counter].position + " " + presidents[counter].first + " " + presidents[
                counter].last + "3rd" in line:
                presidents[counter].incrementPref("3rd")
            elif presidents[counter].position + " " + presidents[counter].first + " " + presidents[
                counter].last + "4th" in line:
                presidents[counter].incrementPref("4th")
        counter += 1


def countgsu():
    counter = 0

    for _ in gsu_officers:
        gsu_officers[counter].resetPref()
        for line in Final_Tally:
            if gsu_officers[counter].position + " " + gsu_officers[counter].first + " " + gsu_officers[
                counter].last + "1st" in line:
                gsu_officers[counter].incrementPref("1st")
            elif gsu_officers[counter].position + " " + gsu_officers[counter].first + " " + gsu_officers[
                counter].last + "2nd" in line:
                gsu_officers[counter].incrementPref("2nd")
            elif gsu_officers[counter].position + " " + gsu_officers[counter].first + " " + gsu_officers[
                counter].last + "3rd" in line:
                gsu_officers[counter].incrementPref("3rd")
            elif gsu_officers[counter].position + " " + gsu_officers[counter].first + " " + gsu_officers[
                counter].last + "4th" in line:
                gsu_officers[counter].incrementPref("4th")
        counter += 1


def countmath():
    counter = 0

    for _ in math_faculty_officers:
        math_faculty_officers[counter].resetPref()
        for line in Final_Tally:
            if math_faculty_officers[counter].position + " " + math_faculty_officers[counter].first + " " + \
                    math_faculty_officers[counter].last + "1st" in line:
                math_faculty_officers[counter].incrementPref("1st")
            elif math_faculty_officers[counter].position + " " + math_faculty_officers[counter].first + " " + \
                    math_faculty_officers[counter].last + "2nd" in line:
                math_faculty_officers[counter].incrementPref("2nd")
            elif math_faculty_officers[counter].position + " " + math_faculty_officers[counter].first + " " + \
                    math_faculty_officers[counter].last + "3rd" in line:
                math_faculty_officers[counter].incrementPref("3rd")
            elif math_faculty_officers[counter].position + " " + math_faculty_officers[counter].first + " " + \
                    math_faculty_officers[counter].last + "4th" in line:
                math_faculty_officers[counter].incrementPref("4th")
        counter += 1


def countsci():
    counter = 0

    for _ in sci_faculty_officers:
        sci_faculty_officers[counter].resetPref()
        for line in Final_Tally:
            if sci_faculty_officers[counter].position + " " + sci_faculty_officers[counter].first + " " + \
                    sci_faculty_officers[counter].last + "1st" in line:
                sci_faculty_officers[counter].incrementPref("1st")
            elif sci_faculty_officers[counter].position + " " + sci_faculty_officers[counter].first + " " + \
                    sci_faculty_officers[counter].last + "2nd" in line:
                sci_faculty_officers[counter].incrementPref("2nd")
            elif sci_faculty_officers[counter].position + " " + sci_faculty_officers[counter].first + " " + \
                    sci_faculty_officers[counter].last + "3rd" in line:
                sci_faculty_officers[counter].incrementPref("3rd")
            elif sci_faculty_officers[counter].position + " " + sci_faculty_officers[counter].first + " " + \
                    sci_faculty_officers[counter].last + "4th" in line:
                sci_faculty_officers[counter].incrementPref("4th")
        counter += 1


def countcomp():
    counter = 0

    for _ in computing_faculty_officers:
        computing_faculty_officers[counter].resetPref()
        for line in Final_Tally:
            if computing_faculty_officers[counter].position + " " + computing_faculty_officers[counter].first + " " + \
                    computing_faculty_officers[counter].last + "1st" in line:
                computing_faculty_officers[counter].incrementPref("1st")
            elif computing_faculty_officers[counter].position + " " + computing_faculty_officers[counter].first + " " + \
                    computing_faculty_officers[counter].last + "2nd" in line:
                computing_faculty_officers[counter].incrementPref("2nd")
            elif computing_faculty_officers[counter].position + " " + computing_faculty_officers[counter].first + " " + \
                    computing_faculty_officers[counter].last + "3rd" in line:
                computing_faculty_officers[counter].incrementPref("3rd")
            elif computing_faculty_officers[counter].position + " " + computing_faculty_officers[counter].first + " " + \
                    computing_faculty_officers[counter].last + "4th" in line:
                computing_faculty_officers[counter].incrementPref("4th")
        counter += 1


def countart():
    counter = 0

    for _ in art_faculty_officers:
        art_faculty_officers[counter].resetPref()
        for line in Final_Tally:
            if art_faculty_officers[counter].position + " " + art_faculty_officers[counter].first + " " + \
                    art_faculty_officers[counter].last + "1st" in line:
                art_faculty_officers[counter].incrementPref("1st")
            elif art_faculty_officers[counter].position + " " + art_faculty_officers[counter].first + " " + \
                    art_faculty_officers[counter].last + "2nd" in line:
                art_faculty_officers[counter].incrementPref("2nd")
            elif art_faculty_officers[counter].position + " " + art_faculty_officers[counter].first + " " + \
                    art_faculty_officers[counter].last + "3rd" in line:
                art_faculty_officers[counter].incrementPref("3rd")
            elif art_faculty_officers[counter].position + " " + art_faculty_officers[counter].first + " " + \
                    art_faculty_officers[counter].last + "4th" in line:
                art_faculty_officers[counter].incrementPref("4th")
        counter += 1


# DISPLAYING VOTES
#List that store the data to display post voting (Ahmed Hamad 001049653)
presidents_display = []
gsu_officers_display = []
math_faculty_officers_display = []
computing_faculty_officers_display = []
sci_faculty_officers_display = []
art_faculty_officers_display = []
collective_display = ["presidents_display", "gsu_officers_display", "gsu_officers_display","gsu_officers_display",
                      "math_faculty_officers_display", "computing_faculty_officers_display",
                      "sci_faculty_officers_display", "art_faculty_officers_display"]

# Appending the data to the lists above then sorting it (Ahmed Hamad 001049653)
def orderVotes():
    l = 0
    for _ in presidents:
        presidents_display.append(
            presidents[l].first + " " + presidents[l].last + "/" + str(presidents[l].firstpref) + "/" + str(
                presidents[l].secondpref) + "/" + str(presidents[l].thirdpref) + "/" + str(presidents[l].fourthpref))
        l += 1
    l = 0
    for _ in gsu_officers:
        gsu_officers_display.append(
            gsu_officers[l].first + " " + gsu_officers[l].last + "/" + str(gsu_officers[l].firstpref) + "/" + str(
                gsu_officers[l].secondpref) + "/" + str(gsu_officers[l].thirdpref) + "/" + str(
                gsu_officers[l].fourthpref))
        l += 1
    l = 0
    for _ in math_faculty_officers:
        math_faculty_officers_display.append(
            math_faculty_officers[l].first + " " + math_faculty_officers[l].last + "/" + str(
                math_faculty_officers[l].firstpref) + "/" + str(math_faculty_officers[l].secondpref) + "/" + str(
                math_faculty_officers[l].thirdpref) + "/" + str(math_faculty_officers[l].fourthpref))
        l += 1
    l = 0
    for _ in computing_faculty_officers:
        computing_faculty_officers_display.append(
            computing_faculty_officers[l].first + " " + computing_faculty_officers[l].last + "/" + str(
                computing_faculty_officers[l].firstpref) + "/" + str(
                computing_faculty_officers[l].secondpref) + "/" + str(
                computing_faculty_officers[l].thirdpref) + "/" + str(computing_faculty_officers[l].fourthpref))
        l += 1
    l = 0
    for _ in sci_faculty_officers:
        sci_faculty_officers_display.append(
            sci_faculty_officers[l].first + " " + sci_faculty_officers[l].last + "/" + str(
                sci_faculty_officers[l].firstpref) + "/" + str(sci_faculty_officers[l].secondpref) + "/" + str(
                sci_faculty_officers[l].thirdpref) + "/" + str(sci_faculty_officers[l].fourthpref))
        l += 1
    l = 0
    for _ in art_faculty_officers:
        art_faculty_officers_display.append(
            art_faculty_officers[l].first + " " + art_faculty_officers[l].last + "/" + str(
                art_faculty_officers[l].firstpref) + "/" + str(art_faculty_officers[l].secondpref) + "/" + str(
                art_faculty_officers[l].thirdpref) + "/" + str(art_faculty_officers[l].fourthpref))
        l += 1


#function for sorting the lists by name (Ahmed Hamad 001049653)
    def sortDisplay(list):
        def splitList(line):
            name, wantedNumber, otherNumbers, otherNumbers1, otherNumbers2 = line.split('/')
            return name



        list.sort(key=splitList)

    sortDisplay(presidents_display)
    sortDisplay(gsu_officers_display)
    sortDisplay(math_faculty_officers_display)
    sortDisplay(sci_faculty_officers_display)
    sortDisplay(computing_faculty_officers_display)
    sortDisplay(art_faculty_officers_display)
#function to sort the data by FirstPreference votes used in GUI.py (Ahmed Hamad 001049653)
def splitListWin(line):
    name, wantedNumber, otherNumbers, otherNumbers1, otherNumbers2 = line.split('/')
    return wantedNumber