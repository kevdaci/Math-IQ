from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.storage.jsonstore import JsonStore
from random import randint


class StartScreen(Screen):
	pass

class MenuScreen(Screen):
	pass

class AddingScreen(Screen):
    num1 = randint(1,50)
    num2 = randint(1,50)
    score = 0

    def __init__(self, **kwargs):
    	super(AddingScreen, self).__init__(**kwargs)

    def first_label(self):
    	if self.num1 < 10 and self.num2 < 10:
    		return " %5d" %(self.num1)
    	elif self.num1 < 10:
    		return " %6d" %(self.num1)
    	else:
    		return " %5d" %(self.num1)

    def second_label(self):
		if self.num1 < 10 and self.num2 < 10:
			return "+%4d" %(self.num2)
		elif self.num2 < 10:
			return "+%4d" %(self.num2)
		else:
			return "+%4d" %(self.num2)

    def produce_numbers(self):
    	self.num1 = randint(1,50)
    	self.num2 = randint(1,50)

    def align_labels(self):
    	self.produce_numbers()
    	if self.num1 < 10 and self.num2 < 10:
    		self.label1.text = " %5d" %(self.num1)
    		self.label2.text = "+%4d" %(self.num2)
    	elif self.num2 < 10:
    		self.label1.text = " %4d" %(self.num1)
    		self.label2.text = "+%4d" %(self.num2)
    	elif self.num1 < 10:
    		self.label1.text = " %6d" %(self.num1)
    		self.label2.text = "+%4d" %(self.num2)
    	else:
    		self.label1.text = " %5d" %(self.num1)
    		self.label2.text = "+%4d" %(self.num2)

    def assign_labels(self):
    	self.align_labels()
    	if self.score > 0:
    		self.s.text = "Score: " + str(self.score)
    	else:
    		self.s.text = ""

    def update_score(self):
    	self.score += 1

    def give_final_score(self):
    	return self.score

    def check_addition(self):
    	num_answer = int(self.answer.text)
    	return num_answer == self.num1 + self.num2

    def update_adding_screen(self):
    	self.update_score()
    	self.assign_labels()
    	self.answer.text = ""

    def restart_adding_screen(self):
    	self.score = 0
    	self.assign_labels()
    	self.answer.text = ""

class SubstractingScreen(Screen):
	num1 = randint(1,9)
	num2 = randint(1,50)
	score = 0

	def first_label(self):
		max_num = max([self.num1, self.num2])
		min_num = min([self.num1, self.num2])
		if max_num < 10 and min_num < 10:
			return " %5d" %(max_num)
		elif max_num > 10:
			return " %4d" %(max_num)
		else:
			return " %5d" %(max_num)

	def second_label(self):
		max_num = max([self.num1, self.num2])
		min_num = min([self.num1, self.num2])
		return "-%5d" %(min_num)

	def produce_numbers(self):
		self.num1 = randint(1,50)
		self.num2 = randint(1,50)

	def align_labels(self):
		self.produce_numbers()
		max_num = max([self.num1, self.num2])
		min_num = min([self.num1, self.num2])
		if max_num < 10 and min_num < 10:
			self.label1.text = " %5d" %(max_num)
			self.label2.text = "-%5d" %(min_num)
		if min_num < 10:
			self.label1.text = " %4d" %(max_num)
			self.label2.text = "-%5d" %(min_num)
		else:
			self.label1.text = " %5d" %(max_num)
			self.label2.text = "-%5d" %(min_num)

	def assign_labels(self):
		self.align_labels()
		if self.score > 0:
			self.s.text = "Score: " + str(self.score)
		else:
			self.s.text = ""

	def update_score(self):
		self.score += 1

	def give_final_score(self):
		return self.score

	def check_substraction(self):
		num_answer = int(self.answer.text)
		if self.num1 < self.num2:
			return (num_answer * -1) == self.num1 - self.num2
		else:
			return num_answer == self.num1 - self.num2

	def update_substracting_screen(self):
		self.update_score()
		self.assign_labels()
		self.answer.text = ""

	def restart_substracting_screen(self):
		self.score = 0
		self.assign_labels()
		self.answer.text = ""


class MultiplyingScreen(Screen):
	num1 = randint(1,20)
	num2 = randint(1,20)
	op_label1 = " %5d" %(num1)
	op_label2 = "x%5d" %(num2)
	score = 0

	def first_label(self):
		if self.num1 < 10 and self.num2 < 10:
			return " %5d" %(self.num1)
		elif self.num1 < 10:
			return " %6d" %(self.num1)
		else:
			return " %5d" %(self.num1)

	def second_label(self):
		if self.num1 < 10 and self.num2 < 10:
			return "x%4d" %(self.num2)
		elif self.num2 < 10:
			return "x%4d" %(self.num2)
		else:
			return "x%4d" %(self.num2)

	def produce_numbers(self):
		self.num1 = randint(1,20)
		self.num2 = randint(1,20)

	def align_labels(self):
		self.produce_numbers()
		if self.num1 < 10 and self.num2 < 10:
			self.label1.text = " %5d" %(self.num1)
			self.label2.text = "x%4d" %(self.num2)
		elif self.num2 < 10:
			self.label1.text = " %4d" %(self.num1)
			self.label2.text = "x%4d" %(self.num2)
		elif self.num1 < 10:
			self.label1.text = " %6d" %(self.num1)
			self.label2.text = "x%4d" %(self.num2)
		else:
			self.label1.text = " %5d" %(self.num1)
			self.label2.text = "x%4d" %(self.num2)

	def assign_labels(self):
		self.align_labels()
		if self.score > 0:
			self.s.text = "Score: " + str(self.score)
		else:
			self.s.text = ""

	def update_score(self):
		self.score += 1

	def give_final_score(self):
		return self.score

	def restart_score(self):
		self.score = 0

	def check_multiplication(self):
		num_answer = int(self.answer.text)
		return num_answer == self.num1 * self.num2

	def update_multiplying_screen(self):
		self.update_score()
		self.assign_labels()
		self.answer.text = ""

	def restart_multiplying_screen(self):
		self.score = 0
		self.assign_labels()
		self.answer.text = ""

class IncorrectScreen(Screen):
	pass

class ScorePopup(Popup):
	pass

class ErrorPopup(Popup):
	pass

class FinalScreen(Screen):
	pass

class ScoreScreen(Screen):
	scores = []
	add = []
	subst = []
	mult = []
	file = "scores.txt"
	scores_store = JsonStore("scores.json")

	def read_scores(self):
		if self.scores_store.exists("scores"):
			line = self.scores_store.get("scores")['hscores']
			self.scores = line
		else:
			self.scores = []

	def append_score(self, mode, name, score):
		self.read_scores()
		pair = [int(score), name]
		if mode not in self.scores:
			self.scores.append(mode)
			self.scores.append(pair)
		else:
			self.scores.insert(self.scores.index(mode) + 1, pair)

	def modify_high_scores(self, mode, name, score):
		self.append_score(mode, name, score)
		beginning = self.scores.index(mode) + 1
		end = 0

		if mode == "adding":
			index = self.scores.index(mode) + 1
			while index < len(self.scores):
				if self.scores[index] == "substracting" or self.scores[index] == "multiplying":
					end = index
					break
				else:
					self.add.append(self.scores[index])
				index += 1
				end = index
			self.sort_section(self.add, beginning, end)

		if mode == "substracting":
			index = self.scores.index(mode) + 1
			while index < len(self.scores):
				if self.scores[index] == "adding" or self.scores[index] == "multiplying":
					end = index
					break
				else:
					self.subst.append(self.scores[index])
				index += 1
				end = index
			self.sort_section(self.subst, beginning, end)

		if mode == "multiplying":
			index = self.scores.index(mode) + 1
			while index < len(self.scores):
				if self.scores[index] == "adding" or self.scores[index] == "substracting":
					end = index
					break
				else:
					self.mult.append(self.scores[index])
				index += 1
				end = index
			self.sort_section(self.mult, beginning, end)

		self.add = []
		self.subst = []
		self.mult = []
		self.write_scores()

	def sort_section(self, sect, beg, end):
		sect.sort()
		sect = sect[::-1]
		if len(sect) > 5:
			del sect[5:]
		self.scores[beg:end] = sect

	def write_scores(self):
		self.scores_store["scores"] = {"hscores": self.scores}

	def write_addition_scores(self):
		self.read_scores()
		labels = []
		pass_adding = False
		count  = 1
		self.category.text = "High Scores - Addition"

		try:
			index = self.scores.index("adding") + 1
		except:
			self.empty_score_labels(labels)
			count, index = 100, 100

		while index < len(self.scores) or count < 6:
			try:
				if (self.scores[index] == "substracting" or self.scores[index] == "multiplying") or pass_adding:
					pass_adding = True
					if count < 6:
						raise Exception()
				else:
					labels.append(self.scores[index])
			except:
					labels.append([0, "N/A"])
			index += 1
			count += 1

		self.score_label1_name.text = "1. %-7s" %(labels[0][1])
		self.score_label1_score.text = str(labels[0][0])
		self.score_label2_name.text = "2. %-5s" %(labels[1][1])
		self.score_label2_score.text = str(labels[1][0])
		self.score_label3_name.text = "3. %-5s" %(labels[2][1])
		self.score_label3_score.text = str(labels[2][0])
		self.score_label4_name.text = "4. %-5s"  %(labels[3][1])
		self.score_label4_score.text = str(labels[3][0])
		self.score_label5_name.text = "5. %-5s" %(labels[4][1])
		self.score_label5_score.text = str(labels[4][0])

	def write_substraction_scores(self):
		self.read_scores()
		labels = []
		pass_substracting = False
		count  = 1
		self.category.text = "High Scores - Substraction"

		try:
			index = self.scores.index("substracting") + 1
		except:
			self.empty_score_labels(labels)
			count, index = 100, 100

		while index < len(self.scores) or count < 6:
			try:
				if (self.scores[index] == "adding" or self.scores[index] == "multiplying") or pass_substracting:
					pass_substracting = True
					if count < 6:
						raise Exception()
				else:
					labels.append(self.scores[index])
			except:
					labels.append([0, "N/A"])
			index += 1
			count += 1

		self.score_label1_name.text = "1. %-7s" %(labels[0][1])
		self.score_label1_score.text = str(labels[0][0])
		self.score_label2_name.text = "2. %-5s" %(labels[1][1])
		self.score_label2_score.text = str(labels[1][0])
		self.score_label3_name.text = "3. %-5s" %(labels[2][1])
		self.score_label3_score.text = str(labels[2][0])
		self.score_label4_name.text = "4. %-5s"  %(labels[3][1])
		self.score_label4_score.text = str(labels[3][0])
		self.score_label5_name.text = "5. %-5s" %(labels[4][1])
		self.score_label5_score.text = str(labels[4][0])

	def write_multiplication_labels(self):
		self.read_scores()
		labels = []
		pass_multiplying = False
		count  = 1
		self.category.text = "High Scores - Multiplication"
		try:
			index = self.scores.index("multiplying") + 1
		except:
			self.empty_score_labels(labels)
			count, index = 100, 100
		while index < len(self.scores) or count < 6:
			try:
				if (self.scores[index] == "adding" or self.scores[index] == "multiplying") or pass_multiplying:
					pass_substracting = True
					if count < 6:
						raise Exception()
				else:
					labels.append(self.scores[index])
			except:
					labels.append([0, "N/A"])
			index += 1
			count += 1
		self.score_label1_name.text = "1. %-7s" %(labels[0][1])
		self.score_label1_score.text = str(labels[0][0])
		self.score_label2_name.text = "2. %-5s" %(labels[1][1])
		self.score_label2_score.text = str(labels[1][0])
		self.score_label3_name.text = "3. %-5s" %(labels[2][1])
		self.score_label3_score.text = str(labels[2][0])
		self.score_label4_name.text = "4. %-5s"  %(labels[3][1])
		self.score_label4_score.text = str(labels[3][0])
		self.score_label5_name.text = "5. %-5s" %(labels[4][1])
		self.score_label5_score.text = str(labels[4][0])

	def empty_score_labels(self, labels):
		for count in range(5):
			labels.append([0, "N/A"])

class MathRoot(ScreenManager):
	final_score = NumericProperty()
	player_name = StringProperty()
	mode = StringProperty()
	submissions = 0

	def check_answer(self,op):
		self.mode = op
		try:
			if op == "adding":
				if self.adding_screen.check_addition():
					self.adding_screen.update_adding_screen()
					return "adding"
				else:
					self.final_score = self.adding_screen.give_final_score()
					self.adding_screen.restart_adding_screen()
					return "incorrect"
			if op == "substracting":
				if self.substracting_screen.check_substraction():
					self.substracting_screen.update_substracting_screen()
					return "substracting"
				else:
					self.final_score = self.substracting_screen.give_final_score()
					self.substracting_screen.restart_substracting_screen()
					return "incorrect"
			if op == 'multiplying':
				if self.multiplying_screen.check_multiplication():
					self.multiplying_screen.update_multiplying_screen()
					return "multiplying"
				else:
					self.final_score = self.multiplying_screen.give_final_score()
					self.multiplying_screen.restart_multiplying_screen()
					return "incorrect"
		except Exception:
			return op

	def enter_player_name(self):
		if self.submissions < 1:
			popup = ScorePopup(on_dismiss = self.write_player)
			popup.open()
		else:
			error_popup = ErrorPopup()
			error_popup.open()

		self.submissions += 1

	def to_start(self):
		self.submissions = 0
		self.player_name = ""
		return "start"

	def get_player_name(self, popup):
		self.player_name = popup.n.text

	def write_player(self,popup):
		self.get_player_name(popup)
		self.score_screen.modify_high_scores(self.mode,self.player_name,self.final_score)

	def to_high_scores(self):
		self.score_screen.write_addition_scores()
		return "score"

class MathIQApp(App):

	def on_pause(self):
		return False

	def open_settings(self):
		pass

if __name__ == '__main__':
	MathIQApp().run()
