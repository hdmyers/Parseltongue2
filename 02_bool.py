import random

list1 = ["False","True","True","None","True","None","None","False","False","None","True","False"]
list2 = ["or","or","or","==","!=","==","and","==","!=","and","==","or"]
list3 = ["False","False","None","None","True","True","False","True","None","False","True","None"]

def do_the_eval_thing(item1, item2, item3):
    print(item1 + " " + item2 + " " + item3 + " => " + str(eval(item1 + " " + item2 + " " + item3)))
            
def do_the_iterative_thing():
    for x in range(0, len(list1)-1):
        do_the_eval_thing(list1[x], list2[x], list3[x])

def do_the_random_thing():
    for x in range(0, len(list1)-1):
        triple = (random.randint(0, len(list1)-1), random.randint(0, len(list2)-1), random.randint(0, len(list3)-1))
        do_the_eval_thing(list1[triple[0]], list2[triple[1]], list3[triple[2]])

do_the_iterative_thing()
print("")
do_the_random_thing()

