import testMaker as m
import final281Text as x

keyCodes = ["crystal ball", "swift rabbit"]

"""
    TEMPLATES
	tf01 = m.TFQuestion(x.tf01q, x.tf01a, x.tf01v)
	mc1  = m.MCQuestion(x.mc1q, x.mc1a, x.mc1v, x.mc1c, x.mc1e)
	sa1  = m.SAQuestion(x.sa1q, x.sa1a, x.sa1v)
"""

q = m.MCQuestion(x.mc3q, x.mc3a, x.mc3v, x.mc3c, x.mc3e)

s = m.Section(7, "TEST", "DO TEST", "ts", [[q,q,q,q,q,q]])

t = m.Test("QTester", "TEST", "TEST", "0 minutes", [s], False)
t.makeRun(keyCodes)