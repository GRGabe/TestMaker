"""
Commenting: TODO

Sketch: This is going to be the base class for the different types of questions that will be produced
Types of questions will also be included as subclasses below. 

Classes:
	Question
		Subclasses:
			TFQuestion: True/False Questions
			MCQuestion: Multiple Choice Question
			SAQuestion: Short Answer Question
			SMQuestion: Select Multiple Question
			MAQuestion: Match Answers Question
			
		Attributes:
			question : String
			answer : String
			spaceWeight : Int
		
		Methods:
			MakePreamble : () -> String
			MakeInstance : () -> QuestionInstance
			MakePostamble : () -> String
		
	QuestionInstance:
		Attributes:
			question : String
			answer : String
			
		Methods:
			GetQuestion: () -> String
			GetAnswer: () -> String
		
	Section:
		Attributes:
			pointsPerQuestion: Int
			name: String
			instructions: String
			sectionCode : String
			questions : [[Question]]
			
		Methods:
			makeInstance() -> (String, String) [Latex, Key]
		
	Test:
		Attributes:
			name: string (eg. "Final Exam")
			subj: string (eg. "Math 281")
			term: string (eg. "Fall '18")
			time: string (eg. "50 minutes")
			sections : [Section]
			endBlankPage : boolean
			
		Methods:
			makeInstance : String (Name) -> String (Key) //Printed to output
			makeRun : [String] (keycodes) -> None //Printed to output
			makePreamble() : None -> None //Printed to output
			makePostamble() : None -> None //Printed to output
			makeGrid() : None -> String


"""
import testTemplate
import random
import numpy as np



class Question:
	def __init__(self, question, answer,spaceWeight):
		self.question = question
		self.answer = answer
		self.spaceWeight = spaceWeight

	def makeInstance(self):
		return QuestionInstance(self.question + "\\vfill\n"*self.spaceWeight, self.answer )

class TFQuestion(Question):
	def __init__(self, question, answer, variations):
		Question.__init__(self,question, answer, 1)
		self.variations = variations

	def makeInstance(self):
		for var in self.variations:
			assert(len(self.answer) == len(var))
		form = []	
		i = random.randint(0,len(self.answer)-1)
		for var in self.variations:
			instance = var[i]
			form.append(instance)
		return QuestionInstance("\\tf " + self.question.format(*form) + "\\vfill\n", self.answer[i] )

class MCQuestion(Question):
	def __init__(self, question, answer, variations, choices, hasNOTA = True):
		Question.__init__(self, question, answer, 1)
		self.variations = variations
		self.choices = choices
		self.hasNOTA = hasNOTA

	def makeInstance(self):
		for var in self.variations:
			assert(len(self.answer) == len(var))
		form = []	
		i = random.randint(0,len(self.answer)-1)
		for var in self.variations:
			instance = var[i]
			form.append(instance)
		text = self.question.format(*form) + "\n\\begin{enumerate}[\\bf (a)]\n"
		n = len(self.choices)
		if self.hasNOTA:
			j=3
		else:
			j=4
		indices = list(np.random.choice(n,j,False))
		k = random.randint(0,j)
		indices.insert(k,-1)
		for index in indices:
			if index >= 0:
				text += "\\item " + self.choices[index] + "\n"
			else:
				text += "\\item " + self.answer[i] + "\n"
		if self.hasNOTA:
			text += "\\item None of the Above.\n"
		text += "\\end{enumerate}"
		ans = ['A', 'B', 'C', 'D', 'E']
		return QuestionInstance(text + "\\vfill\n", ans[k])

class SAQuestion(Question):
	def __init__(self, question, answer, variations):
		Question.__init__(self, question, answer, 1)
		self.variations = variations

	def makeInstance(self):
		for var in self.variations:
			assert(len(self.answer) == len(var))
		form = []	
		i = random.randint(0,len(self.answer)-1)
		for var in self.variations:
			instance = var[i]
			form.append(instance)
		ending = """\\vfill

\\hfill \\fbox{ \\begin{minipage}{2in} \\hfill\\vspace{.5in} \\end{minipage} } """
		return QuestionInstance(self.question.format(*form) + ending, str(self.answer[i]))


class QuestionInstance:
	def __init__(self, question, answer):
		self.question = question
		self.answer = answer


	def getQuestion(self):
		return "\\item " + self.question 

	def getAnswer(self):
		return self.answer



class Section:
	def __init__(self, pointsPerQuestion, name, instructions, sectionCode, questions):
		self.pointsPerQuestion = pointsPerQuestion
		self.name = name
		self.instructions = instructions
		self.sectionCode = sectionCode
		self.questions = questions

	def makeInstance(self):
		key = "\n\n\\qquad\qquad " + self.sectionCode + ": "
		#i = 1
		output = testTemplate.section1 + self.name + testTemplate.section2 + self.instructions + testTemplate.section3
		print(output)
		n = len(self.questions)
		for j in range(n):
			for question in self.questions[j]:
				q = question.makeInstance()
				print(q.getQuestion())
				key += q.getAnswer() + ", "
				#key += "("+ str(i) + "," + q.getAnswer() +") "
				#i += 1
			if j < n-1:
				print(testTemplate.sectionA)
		print(testTemplate.section4)
		return key



class Test:
	def __init__(self, name, subj, term, time, sections, blankEndPage):
		self.name = name
		self.subj = subj
		self.term = term
		self.time = time
		self.sections = sections
		self.blankEndPage = blankEndPage
	
	def makeRun(self, keyCodes):
		keys = []
		self.makePreamble()
		for keyCode in keyCodes:
			key = self.makeInstance(keyCode)
			keys.append((keyCode,key))
		self.makePostamble(keys)
		
	def makePreamble(self):
		output = testTemplate.latexHeader1 + self.name + testTemplate.latexHeader2 + self.subj + ", " + self.term + testTemplate.latexHeader3
		print(output)
		
	def makePostamble(self, keys):
		print("\\setcounter{page}{1}")
		for key in keys:
			out = key[0] + key[1] + "\n\n"
			print(out)
		print("\\end{document}")
		
	def makeInstance(self, keyCode):
		key = ""
		output = testTemplate.coverPage1 + self.name + testTemplate.coverPage2 + self.time + testTemplate.coverPage3 + keyCode + testTemplate.coverPage4 + self.makeGrid() + testTemplate.coverPage5
		print(output)
		for section in self.sections:
			key += section.makeInstance()
		if self.blankEndPage:
			print("\\newpage\n\n")
		return key
	
	def makeGrid(self):
		i = 2
		out = testTemplate.grid1
		for section in self.sections:
			for page in section.questions:
				p = section.pointsPerQuestion * len(page)
				out += testTemplate.gridLine1 + str(i) + testTemplate.gridLine2 + str(p) + testTemplate.gridLine3 + "\n"
				i += 1
		out += testTemplate.grid2
		return out
	