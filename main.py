import python_stuff.api as api

if api.draw("Activate german language? If so, type d").lower() == "d":
    import language.german as l
else:
    import language.english as l

mysteries = [1, 2, 3, 4]
mystery = api.askNum(l.which_mystery())

if mystery not in mysteries:
    api.draw(l.invalid_mystery())
    mystery = 1
def o(text): # For easier to read code below
    api.draw(text)
    
o(l.only_press_enter())
    
o(l.crucifix())
o(l.i_believe())
o(l.glory_be())
o(l.our_father())

o(l.ave_maria(l.ave_maria_start(1)))
o(l.ave_maria(l.ave_maria_start(2)))
o(l.ave_maria(l.ave_maria_start(3)))

for i in range(1,6):
    o(l.glory_be())
    o(l.our_father())
    o(l.ave_maria(l.get_mysteries(mystery, i), "10x\n"))

o(l.glory_be())