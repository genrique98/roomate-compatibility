from date import Date
from preference import Preference
import math

class Student:
    def __init__(self, name, gender, birthdate, preference):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.preference = preference
        self.matched = False

    def compare(self, student):
        preferences = 0
        ageDifference = 0
        
        studentGender1 = student.gender
        studentGender2 = self.gender
        
        studentBirthdate1 = student.birthdate
        # studentBirthDate2 = self.birthdate
        
        stPref1 = student.preference # . what preference is it comparing?
        # stPref2 = self.preference #
        
        preferences = self.preference.comparePref(stPref1)
        ageDifference = self.birthdate.compareDate(studentBirthdate1)
        # preferences = math.fabs(stPref1 - stPref2) 
        # ageDifference = math.fabs(studentBirthdate1 - studentBirthDate2)
        
        compatibility = (40 - preferences) + (60 - ageDifference)
        
        if (studentGender1 != studentGender2 or ageDifference > 60):
            compatibility = 0
            
        return compatibility
