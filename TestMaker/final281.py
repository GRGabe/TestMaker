import testMaker as m
import final281Text as x

keyCodes =     ["apple pastry", "blue trumpet", "chicken legs", "crystal ball", 
		"danger zones", "driven sleet", "egg scramble", "eight pizzas", 
		"free dessert", "green lights", "happy pixels", "icy driveway",
		"jungle party", "kickball gal", "light purple", "maze walkers", 
		"new sneakers", "orange juice", "pretty stone", "psychic boss",
		"quick tailor", "relaxed dogs", "shuffle foot", "swift rabbit", 
		"taco tuesday", "through ways", "umpire union", "vampire gala",
		"working dude", "xray wizards", "yellow camel", "zebra escape" ]

tf01 = m.TFQuestion(x.tf01q, x.tf01a, x.tf01v)
tf02 = m.TFQuestion(x.tf02q, x.tf02a, x.tf02v)
tf03 = m.TFQuestion(x.tf03q, x.tf03a, x.tf03v)
tf04 = m.TFQuestion(x.tf04q, x.tf04a, x.tf04v)
tf05 = m.TFQuestion(x.tf05q, x.tf05a, x.tf05v)
tf06 = m.TFQuestion(x.tf06q, x.tf06a, x.tf06v)
tf07 = m.TFQuestion(x.tf07q, x.tf07a, x.tf07v)
tf08 = m.TFQuestion(x.tf08q, x.tf08a, x.tf08v)
tf09 = m.TFQuestion(x.tf09q, x.tf09a, x.tf09v)
tf10 = m.TFQuestion(x.tf10q, x.tf10a, x.tf10v)
tf11 = m.TFQuestion(x.tf11q, x.tf11a, x.tf11v)
tf12 = m.TFQuestion(x.tf12q, x.tf12a, x.tf12v)
tf13 = m.TFQuestion(x.tf13q, x.tf13a, x.tf13v)
tf14 = m.TFQuestion(x.tf14q, x.tf14a, x.tf14v)
tf15 = m.TFQuestion(x.tf15q, x.tf15a, x.tf15v)
tf16 = m.TFQuestion(x.tf16q, x.tf16a, x.tf16v)
tf17 = m.TFQuestion(x.tf17q, x.tf17a, x.tf17v)
tf18 = m.TFQuestion(x.tf18q, x.tf18a, x.tf18v)

mc1  = m.MCQuestion(x.mc1q, x.mc1a, x.mc1v, x.mc1c, x.mc1e)
mc2  = m.MCQuestion(x.mc2q, x.mc2a, x.mc2v, x.mc2c, x.mc2e)
mc3  = m.MCQuestion(x.mc3q, x.mc3a, x.mc3v, x.mc3c, x.mc3e)
mc4  = m.MCQuestion(x.mc4q, x.mc4a, x.mc4v, x.mc4c, x.mc4e)
mc5  = m.MCQuestion(x.mc5q, x.mc5a, x.mc5v, x.mc5c, x.mc5e)
mc6  = m.MCQuestion(x.mc6q, x.mc6a, x.mc6v, x.mc6c, x.mc6e)

sa1  = m.SAQuestion(x.sa1q, x.sa1a, x.sa1v)
sa2  = m.SAQuestion(x.sa2q, x.sa2a, x.sa2v)
sa3  = m.SAQuestion(x.sa3q, x.sa3a, x.sa3v)
sa4  = m.SAQuestion(x.sa4q, x.sa4a, x.sa4v)
sa5  = m.SAQuestion(x.sa5q, x.sa5a, x.sa5v)
sa6  = m.SAQuestion(x.sa6q, x.sa6a, x.sa6v)
sa7  = m.SAQuestion(x.sa7q, x.sa7a, x.sa7v)
sa8  = m.SAQuestion(x.sa8q, x.sa8a, x.sa8v)

tf = m.Section(2, x.tfTitle, x.tfInst, "tf", 
	[[tf01, tf02, tf03, tf04, tf05, tf06, tf07, tf08, tf09],
	 [tf10, tf11, tf12, tf13, tf14, tf15, tf16, tf17, tf18]])
mc = m.Section(4, x.mcTitle, x.mcInst, "mc",
	[[mc1, mc2, mc3],
	 [mc4, mc5, mc6]])
sa = m.Section(5, x.saTitle, x.saInst, "sa",
	[[sa1, sa2, sa3],
	 [sa4, sa5],
	 [sa6, sa7, sa8]])


t = m.Test("Final Exam", "Math 281", "Summer '18", "110 minutes", [tf, mc, sa], False)

t.makeRun(keyCodes)
