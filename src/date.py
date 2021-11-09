import math

class Date:
	months = { 
		12: 31,
		11: 30, 
		10: 31, 
		9: 30, 
		8: 31, 
		7: 31, 
		6: 30, 
		5: 31, 
		4: 30, 
		3: 31, 
		2: 28, 
		1: 31 
	}
	
	def __init__(self, year, month, day):  # constructor
		self.year = year
		self.month = month
		self.day = day
	
	def dayOfYear(self): 
		totalDays = 0
		totalDays += Date.months[self.month]
		totalDays += self.day
		return totalDays

	def compareDate(self, date):
		yearsDifferenceInDays = math.fabs(self.year - date.year) # 
		daysDifference = math.fabs(self.dayOfYear() - date.dayOfYear())
		totalDifference = math.fabs(yearsDifferenceInDays - daysDifference)
		totalDifference = totalDifference / 30
		
		if (totalDifference > 60):
			return 60

		return totalDifference
	
