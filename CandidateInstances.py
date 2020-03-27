# CANDIDATE INFORMATION
candidates_line = list()
filename = 'GSUCandidates.txt'
with open(filename) as f:
    for line in f:
        line = line.strip()
        candidates_line.append(line)
    pass


# Candidate classes, all the candidates are taken and made into class objects here (Ahmed Hamad 001049653)
class Candidate:
    def __init__(self, position, first, last, firstpref, secondpref, thirdpref, fourthpref):
        self.first = first
        self.last = last
        self.position = position
        self.firstpref = int(firstpref)
        self.secondpref = int(secondpref)
        self.thirdpref = int(thirdpref)
        self.fourthpref = int(fourthpref)

    # Class method used to create new candidates (Ahmed Hamad 001049653)
    @classmethod
    def add_candidate(cls, candidates_list):
        position, first, last, firstpref, secondpref, thirdpref, fourthpref = candidates_list.split(' ')
        return cls(position, first, last, firstpref, secondpref, thirdpref, fourthpref)

    # Class method used to increase vote count for specific candidate (Ahmed Hamad 001049653)
    def incrementPref(self, pref):
        if pref == "1st":
            self.firstpref = self.firstpref + 1
        elif pref == "2nd":
            self.secondpref = self.secondpref + 1
        elif pref == "3rd":
            self.thirdpref = self.thirdpref + 1
        elif pref == "4th":
            self.fourthpref = self.fourthpref + 1

    # Class method to clear previous votes incase user changes votes before final submit (Ahmed Hamad 001049653)
    def resetPref(self):
        self.firstpref = 0
        self.secondpref = 0
        self.thirdpref = 0
        self.fourthpref = 0


# Candidate classes defined below (Ahmed Hamad 001049653)
class President(Candidate):
    def __init__(self, position, first, last, firstpref, secondpref, thirdpref, fourthpref):
        super().__init__(position, first, last, firstpref, secondpref, thirdpref, fourthpref)

    pass


class GSU_Officer(Candidate):
    def __init__(self, position, first, last, firstpref, secondpref, thirdpref, fourthpref):
        super().__init__(position, first, last, firstpref, secondpref, thirdpref, fourthpref)

    pass


class Faculty_Officer(Candidate):
    def __init__(self, position, first, last, firstpref, secondpref, thirdpref, fourthpref):
        super().__init__(position, first, last, firstpref, secondpref, thirdpref, fourthpref)

    pass


# Lists holding all Class instances for candidates (Ahmed Hamad 001049653)
presidents = []
gsu_officers = []
art_faculty_officers = []
computing_faculty_officers = []
math_faculty_officers = []
sci_faculty_officers = []
# Adding Instances to lists above (Ahmed Hamad 001049653)
for line in candidates_line:
    if 'President' in line:
        president = President.add_candidate(line)
        presidents.append(president)
    elif 'GSU_Officer' in line:
        gsu_officer = GSU_Officer.add_candidate(line)
        gsu_officers.append(gsu_officer)
    elif 'Art_Faculty_Officer' in line:
        art_faculty_officer = Faculty_Officer.add_candidate(line)
        art_faculty_officers.append(art_faculty_officer)
    elif 'Math_Faculty_Officer' in line:
        math_faculty_officer = Faculty_Officer.add_candidate(line)
        math_faculty_officers.append(math_faculty_officer)
    elif 'Science_Faculty_Officer' in line:
        science_faculty_officer = Faculty_Officer.add_candidate(line)
        sci_faculty_officers.append(science_faculty_officer)
    elif 'Computing_Faculty_Officer' in line:
        computing_faculty_officer = Faculty_Officer.add_candidate(line)
        computing_faculty_officers.append(computing_faculty_officer)

pass