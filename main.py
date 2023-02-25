import python.api as api

if api.draw("Activate german language? If so, type d").lower() == "d":
    import language.german as l
else:
    import language.english as l

mysteries = [1, 2, 3, 4]
mystery = api.askNum(l.which_mystery() + "\n\n" + l.recommended())

while mystery not in mysteries:
    api.draw(l.invalid_mystery())
    mystery = api.askNum(l.which_mystery() + "\n\n" + l.recommended())
def o(text, title = " ")->str: # For easier to read code below
    return api.draw(text, title)

o(l.only_press_enter() + "\n\n" + l.mystery_contains() + "\n" + l.get_mysteries(mystery, 0), "Version 1.3.1")

instructions = [l.crucifix(), l.apostles_creed(), l.our_father(), l.ave_maria(l.ave_maria_start(1)), l.ave_maria(l.ave_maria_start(2)), l.ave_maria(l.ave_maria_start(3)), l.glory_be()]

for i in range(1,6):
    instructions.append(l.our_father())
    instructions.append(l.ave_maria(l.get_mysteries(mystery, i), "10x\n"))
    instructions.append(l.glory_be() + "\n\n" + l.fatima_prayer())

x = 0
while x < len(instructions):
    feedback = o(instructions[x])
    if (feedback.lower() == "b" or feedback.lower() == "z") and x > 0:
        x = x - 1
    elif feedback.lower() == "b" or feedback.lower() == "z": # We are at the last point and cannot go back any further.
        o(l.cant_go_back())
    else:
        x = x + 1