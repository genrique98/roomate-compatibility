import csv
from date import Date
from preference import Preference
from student import Student

class Match:

    def __main__():
        students = []
        currentScore = 0
        maxScore = 0
        bestMatch = -1

        # populate students array with roster data
        with open('../FullRoster.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                date = row[2].split('-')
                date = Date(int(date[0]), int(date[1]), int(date[2]))

                pref = Preference(int(row[3]), int(row[4]), int(row[5]), int(row[6]))

                student = Student(row[0], row[1], date, pref)
                students.append(student)
                
        for student in students:
            maxScore = 0 # reset score for next student
            bestMatch = -1
            if (student.matched == False):
            	for j, another in enumerate(students):
                    if(student.matched == False):
                        if (another.matched == False and student != another):
                            currentScore = student.compare(another)
                            if(currentScore > maxScore):
                                bestMatch = j
                                maxScore = currentScore
							
            student.matched = True
            if (bestMatch != -1):
                students[bestMatch].matched = True
                print(student.name + " matches with " + students[bestMatch].name + " with score: ", maxScore)
            elif (bestMatch == -1 and student.matched == True):
                print("--" + student.name + " has no matches.")

Match.__main__()
