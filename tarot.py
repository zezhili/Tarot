from msvcrt import kbhit
import random

tarot = { 1: "The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}


def magic():
    user_name = input("Your name is: ")
    past = tarot.pop(random.randint(1, 22))
    present = tarot.pop(random.randint(1, 21))
    future = tarot.pop(random.randint(1, 20))
    if random.randint(0,2) == 1:
        过去顺序 = "正序"
    else:
        过去顺序 = "倒序"
    
    if random.randint(0,2) == 1:
        现在顺序 = "正序"
    else:
        现在顺序 = "倒序"
    
    if random.randint(0,2) == 1:
        未来顺序 = "正序"
    else:
        未来顺序 = "倒序"

    print("你好 " + user_name)
    print("你的过去是 " + str(过去顺序) + past)
    print("你的现在是 " + str(现在顺序)+ present)
    print("你的未来是 " + str(未来顺序)+ future)
    


magic()

