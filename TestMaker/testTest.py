import testMaker
import testTemplate

q1 = testMaker.Question("Sample Text","ANS",1)
q2 = testMaker.TFQuestion("This is {}.",["true","paradox"],[["true", "false"]])
q3 = testMaker.MCQuestion("A {} is a type of what?", 
	["Cat","Dog"],[["fluff","pupper"]], 
	["Lizard", "Sandwich", "Video Game", "Sports Team"], True)
q4 = testMaker.SAQuestion("How many {} are in a {}?", [3,5280],[['feet','feet'],['yard','mile']])

s = testMaker.Section(3, "Questions", "Do the questions", "Q", 
	[[q1,q2],[q3,q4]])
t = testMaker.Test("Final Exam","Math 281","Summer '18","110 minutes",[s,s],False)

keyCodes = ["swift rabbit", "crystal ball"]
t.makeRun(keyCodes)
