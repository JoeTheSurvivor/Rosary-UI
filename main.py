import python.api as api

if api.draw("Activate german language? If so, type d").lower() == "d":
    import language.german as l
else:
    import language.english as l

mysteries = [1, 2, 3, 4]
mystery = api.askNum(l.which_mystery())

if mystery not in mysteries:
    api.draw(l.invalid_mystery())
    mystery = 1
def o(text)->str: # For easier to read code below
    return api.draw(text)

o(l.only_press_enter())

instructions = [l.crucifix(), l.i_believe(), l.glory_be(), l.our_father(), l.ave_maria(l.ave_maria_start(1)), l.ave_maria(l.ave_maria_start(1)), l.ave_maria(l.ave_maria_start(3))]

for i in range(1,6):
    instructions.append(l.glory_be())
    instructions.append(l.our_father())
    instructions.append(l.ave_maria(l.get_mysteries(mystery, i), "10x\n"))

instructions.append(l.glory_be())

x = 0
while x < len(instructions):
    feedback = o(instructions[x])
    if (feedback.lower() == "b" or feedback.lower() == "z") and x > 0:
        x = x - 1
    elif feedback.lower() == "b" or feedback.lower() == "z": # We are at the last point and cannot go back any further.
        o(l.cant_go_back())
    else:
        x = x + 1