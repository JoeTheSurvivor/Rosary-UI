# Good example: https://www.adorare.ch/rosenkranz.html
def which_mystery()->str:
    return "Welches Geheimnis?\n1 = freudenreichen, 2 = lichtreichen, 3 = schmerzhaften, 4 = glorreichen"
def recommended()->str:
    try:
        from datetime import datetime as dt
        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        mysteries = ["freundenreiche", "schmerzhafte", "glorreiche", "lichtreiche", "schmerzhafte", "freudenreiche", "glorreiche"]
        weekday = dt.weekday(dt.now())
        return "Für " + days[weekday] + " ist der " + mysteries[weekday] + " Rosenkranz empfohlen."
    except Exception:
        return ""
def mystery_contains()->str:
    return "Geheimnis enthält folgende Versen:"

def invalid_mystery()->str:
    return "Geheimnis gibt es nicht, bitte auswählen zwischen 1 2 3 und 4"

def only_press_enter()->str:
    return "Von nun an nur noch Enter drücken. Schreibe z um zurückzuspringen.\nEs kann andere Versionen des Rosenkranz geben."

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
    if not secret == 0:
        return mysteries[mystery - 1](secret)
    else:
        full_mystery_text = ""
        for i in range(1,6):
            full_mystery_text = full_mystery_text + "Jesus, " + mysteries[mystery - 1](i) + "\n"
        return full_mystery_text
def fatima_prayer()->str:
    return "O mein Jesus, verzeih uns unsere Sünden, bewahre uns vor dem Feuer der Hölle,\nführe alle Seelen in den Himmel, besonders jene, die deiner Barmherzigkeit am meisten bedürfen.\nAmen."
def crucifix()->str:
    return "Im Namen des Vaters und des Sohnes und des Heiligen Geistes.\nAmen."

def apostles_creed()->str:
    return "Ich glaube an Gott, den Vater, den Allmächtigen, den Schöpfer des Himmels\nund der Erde, und an Jesus Christus, seinen eingeborenen Sohn, unsern\nHerrn, empfangen durch den Heiligen Geist, geboren von der Jungfrau\nMaria, gelitten unter Pontius Pilatus, gekreuzigt gestorben und begraben,\nhinabgestiegen in das Reich des Todes, am dritten Tage auferstanden von\nden Toten, aufgefahren in den Himmel; er sitzt zur Rechten Gottes, des\nallmächtigen Vaters; von dort wird er kommen, zu richten die Lebenden und\ndie Toten. Ich glaube an den Heiligen Geist, die heilige katholische Kirche,\nGemeinschaft der Heiligen, Vergebung der Sünden, Auferstehung der Toten\nund das ewige Leben.\nAmen."

def glory_be()->str:
    return "Ehre sei dem Vater und dem Sohn und dem Heiligen Geist, wie im Anfang, so auch jetzt und alle Zeit und in Ewigkeit.\nAmen."

def our_father()->str:
    return "Vater unser im Himmel, Geheiligt werde dein Name.\nDein Reich komme. Dein Wille geschehe, wie im Himmel so auf Erden.\nUnser tägliches Brot gib uns heute. Und vergib uns unsere Schuld, wie auch wir vergeben unsern Schuldigern.\nUnd führe uns nicht in Versuchung, sondern erlöse uns von dem Bösen.\nDenn dein ist das Reich und die Kraft und die Herrlichkeit in Ewigkeit.\nAmen."
def ave_maria_start(num)->str:
    secrets = ["der in uns den Glauben vermehre",
               "der in uns die Hoffnung stärke",
               "der in uns die Liebe entzünde"]
    return secrets[num - 1]

def ave_maria(secret:str, amount:str = "")->str:
    return f"{amount}Gegrüßet seist du, Maria, voll der Gnade, der Herr ist mit dir. Du bist\ngebenedeit unter den Frauen, und gebenedeit ist die Frucht deines Leibes,\nJesus, {secret}.\nHeilige Maria, Mutter Gottes, bitte für uns Sünder jetzt und in der Stunde\nunseres Todes.\nAmen."

def cant_go_back()->str:
    return "(Bereits am Anfang)"