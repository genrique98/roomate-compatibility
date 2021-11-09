import math

class Preference:
	
	def __init__(self, quietTime, music, reading, chatting):
		self.quietTime = quietTime
		self.music = music
		self.reading = reading
		self.chatting = chatting
	
	def comparePref(self, preference):
		total = 0

		music = math.fabs(self.music - preference.music)
		quietTime = math.fabs(self.quietTime - preference.quietTime)
		reading = math.fabs(self.reading - preference.reading)
		chatting = math.fabs(self.chatting - preference.chatting)
		total = music + quietTime + reading + chatting
		return total