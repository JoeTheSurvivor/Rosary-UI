def joyful_mystery(num)->str:
    secrets = ["den du, o Jungfrau, vom Heiligen Geist empfangen hast",
               "den du, o Jungfrau, zu Elisabeth getragen hast",
               "den du, o Jungfrau, geboren hast",
               "den du, o Jungfrau, im Tempel aufgeopfert hast",
               "den du, o Jungfrau, im Tempel wiedergefunden hast"]
    return secrets[num - 1]

def luminous_mystery(num)->str:
    secrets = ["der von Johannes getauft worden ist",
               "der sich bei der Hochzeit in Kana offenbart hat",
               "der uns das Reich Gottes verkündet hat",
               "der auf dem Berg verklärt worden ist",
               "der uns die Eucharistie geschenkt hat"]
    return secrets[num - 1]

def sorrowful_mystery(num)->str:
    secrets = ["der für uns Blut geschwitzt hat",
               "der für uns gegeißelt worden ist",
               "der für uns mit Dornen gekrönt worden ist",
               "der für uns das schwere Kreuz getragen hat",
               "der für uns gekreuzigt worden ist"]
    return secrets[num - 1]

def glorious_mystery(num)->str:
    secrets = ["der von den Toten auferstanden ist",
               "der in den Himmel aufgefahren ist",
               "der uns den Heiligen Geist gesandt hat",
               "der dich, o Jungfrau, in den Himmel aufgenommen hat",
               "der dich, o Jungfrau, im Himmel gekrönt hat"]
    return secrets[num - 1]

def get_mysteries(mystery, secret):
    mysteries = [joyful_mystery, luminous_mystery, sorrowful_mystery, glorious_mystery]
    return mysteries[mystery - 1](secret)

def crucifix()->str:
    return "Im Namen des Vaters und des Sohnes und des Heiligen Geistes. \nAmen."

def in_the_name()->str:
    return "Im Namen des Vaters und des Sohnes und des Heiligen Geistes. \nAmen."

def i_believe()->str:
    return "Ich glaube an Gott, den Vater, den Allmächtigen, den Schöpfer des Himmels\nund der Erde, und an Jesus Christus, seinen eingeborenen Sohn, unsern\nHerrn, empfangen durch den Heiligen Geist, geboren von der Jungfrau\nMaria, gelitten unter Pontius Pilatus, gekreuzigt gestorben und begraben,\nhinabgestiegen in das Reich des Todes, am dritten Tage auferstanden von\nden Toten, aufgefahren in den Himmel; er sitzt zur Rechten Gottes, des\nallmächtigen Vaters; von dort wird er kommen, zu richten die Lebenden und\ndie Toten. Ich glaube an den Heiligen Geist, die heilige katholische Kirche,\nGemeinschaft der Heiligen, Vergebung der Sünden, Auferstehung der Toten\nund das ewige Leben. \nAmen."

def glory_be()->str:
    return "Ehre sei dem Vater und dem Sohn und dem Heiligen Geist, wie im Anfang, so auch jetzt und alle Zeit und in Ewigkeit. \nAmen."

def our_father()->str:
    return "Vater unser im Himmel, geheiligt werde dein Name. Dein Reich komme.\nDein Wille geschehe, wie im Himmel so auf Erden. Unser tägliches Brot gib\nuns heute. Und vergib uns unsere Schuld, wie auch wir vergeben unseren\nSchuldigern. Und führe uns nicht in Versuchung, sondern erlöse uns von\ndem Bösen. \nAmen."

def ave_maria_start(num)->str:
    secrets = ["der in uns den Glauben vermehre",
               "der in uns die Hoffnung stärke",
               "der in uns die Liebe entzünde"]
    return secrets[num - 1]

def ave_maria(secret:str, amount:str = "")->str:
    return f"{amount}Gegrüßet seist du, Maria, voll der Gnade, der Herr ist mit dir. Du bist\ngebenedeit unter den Frauen, und gebenedeit ist die Frucht deines Leibes,\nJesus {secret}.\nHeilige Maria, Mutter Gottes, bitte für uns Sünder jetzt und in der Stunde\nunseres Todes. \nAmen."

