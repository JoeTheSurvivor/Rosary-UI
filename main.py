import german as g
import api

mysteries = [1, 2, 3, 4]
mystery = api.askNum("Welches Geheimnis?\n1 = freudenreichen, 2 = lichtreichen, 3 = schmerzhaften, 4 = glorreichen")

if mystery not in mysteries:
    api.draw("Gehemnis gibt es nicht, wechsel zu freudenreichen (1)")
    mystery = 1
def o(text):
    api.draw(text)
o("Von nun an nur noch Enter drücken.")
    
o(g.crucifix())
o(g.i_believe())
o(g.glory_be())
o(g.our_father())

o(g.ave_maria(g.ave_maria_start(1)))
o(g.ave_maria(g.ave_maria_start(2)))
o(g.ave_maria(g.ave_maria_start(3)))

for i in range(1,6):
    o(g.glory_be())
    o(g.our_father())
    o(g.ave_maria(g.get_mysteries(mystery, i), "10x\n"))

o(g.glory_be())