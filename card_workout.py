from random import random, randint #imports random

number_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "15"] #card name list
card_type_list = ["clubs", "dimonds", "hearts", "spades", "joker"] #card type list

workout_clubs = ["crunches", "laying leg raises", "russian twist"] #ab exersizes
workout_dimonds = ["squats", "forward lunges", "jump squats", "side lunges", "calf raises"] #leg exersizes
workout_hearts = ["pushups", "dips"] #chest exersizes
workout_spades = ["jumping jacks"] #cardio exersizes
workout_joker = ["1 min wall sit", "1 min plank"] #endurance exersizes


x = randint(0,12)
y = randint(0,3)


w = randint(0,2)
i = randint(0,4)
u = randint(0,1)
z = 0
joker = randint(0,1)


if card_type_list[y] == "clubs":
    print(number_list[x], workout_clubs[w])
elif card_type_list[y] == "dimonds":
    print(number_list[x], workout_dimonds[i])
elif card_type_list[y] == "hearts":
    print(number_list[x], workout_hearts[u])
elif card_type_list[y] == "spades":
    print(number_list[x], workout_spades[z])
else:
    print(workout_joker[joker])





