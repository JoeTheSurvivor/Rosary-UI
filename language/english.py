def which_mystery()->str:
    return "Which secret?\n1 = joyful, 2 = luminous, 3 = sorrowful, 4 = glorious"
def recommended()->str:
    try:
        from datetime import datetime as dt
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        mysteries = ["joyful", "sorrowful", "glorious", "luminous", "sorrowful", "joyful", "glorious"]
        weekday = dt.weekday(dt.now())
        return "For " + days[weekday] + ", the " + mysteries[weekday] + " rosary is recommended."
    except Exception:
        return ""
def mystery_contains()->str:
    return "Secret contains following verses:"
def invalid_mystery()->str:
    return "Unknown number, please select between 1 2 3 and 4"

def only_press_enter()->str:
    return "From now on only press enter. Type b to go back.\nNote: There are other versions of the rosary. This is not \"THE\" version."

# See https://www.cs.cmu.edu/~spok/catholic/rosary.html
def joyful_mystery(num)->str:
    secrets = ["whom you conceived by the power of the Holy Spirit",
               "whom you carried in your womb, visiting St. Elizabeth",
               "who was born of you in Bethlehem",
               "whom you presented in the Temple",
               "whom you found in the Temple"]
    return secrets[num - 1]

def luminous_mystery(num)->str: # Didn't have a source (see above) so I translated them
    secrets = ["who was baptised by John",
               "who revealed himself in the wedding at Cana",
               "who proclaimed us the Kingdom of God",
               "who became the light on the mountain",
               "who gifted us the Eucharist"]
    return secrets[num - 1]

def sorrowful_mystery(num)->str:
    secrets = ["who sweated blood for us sinners",
               "who was scourged for us sinners",
               "who was crowned with thorns for us sinners",
               "who carried the cross for us sinners",
               "who was crucified for us sinners"]
    return secrets[num - 1]

def glorious_mystery(num)->str:
    secrets = ["who resurrected from the dead",
               "who ascended into Heaven",
               "who sent us the Holy Spirit",
               "who raised you, Blessed Virgin, up into Heaven",
               "who crowned you, Blessed Virgin, in Heaven"]
    return secrets[num - 1]
def get_mysteries(mystery, secret):
    mysteries = [joyful_mystery, luminous_mystery, sorrowful_mystery, glorious_mystery]
    if not secret == 0:
        return mysteries[mystery - 1](secret)
    else:
        full_mystery_text = ""
        for i in range(1,5):
            full_mystery_text = full_mystery_text + "Jesus, " + mysteries[mystery - 1](i) + "\n"
        return full_mystery_text
def fatima_prayer()->str:
    return "O my Jesus, forgive us our sins, save us from the fires of hell.\nLead all souls to heaven, especially those in most need of thy mercy.\nAmen."
def crucifix()->str:
    return "In the name of the Father, and of the Son, and of the Holy Spirit.\nAmen."

def apostles_creed()->str:
    return "I believe in God, the Father almighty, Creator of Heaven and earth.\nAnd in Jesus Christ, His only Son, our Lord,\nWho was conceived by the Holy Spirit, born of the\nVirgin Mary, suffered under Pontius Pilate;\nwas crucified, died, and was buried.\nHe descended into Hell. The third day He rose again from the dead.\nHe ascended into Heaven, and sits at the right hand of God, the Father almighty.\nHe shall come again to judge the living and the dead.\nI believe in the Holy Spirit, the holy Catholic Church,\nthe communion of saints, the forgiveness of sins,\nthe resurrection of the body, and life everlasting.\nAmen."

def glory_be()->str:
    return "Glory be to the Father, and to the Son, and to the Holy Spirit.\nAs it was in the beginning is now, and ever shall be, world thout end.\nAmen."

def our_father()->str:
    return "Our Father, Who art in Heaven, hallowed be Thy Name.\nThy kingdom come, Thy will be done on earth as it is in Heaven.\nGive us this day our daily bread, and forgive us our trespasses, as we forgive those who trespass against us.\nAnd lead us not into temptation, but deliver us from evil.\nAmen."

def ave_maria_start(num)->str:
    secrets = ["who increases our faith",
               "who strengthens our hope",
               "who perfects our love"]
    return secrets[num - 1]

def ave_maria(secret:str, amount:str = "")->str:
    return f"{amount}Haily Mary, full of grace, the Lord is with thee.\nBlessed art thou among women, and blessed is the fruit of thy womb,\nJesus, {secret}.\nHoly Mary, Mother of God, pray for us sinners,\nnow and at the hour of our death.\nAmen."

def cant_go_back()->str:
    return "(You're already at the start)"