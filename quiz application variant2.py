import random
from playsound import playsound
questions={"6+5":["11"],
             "When did India gain independence" :["1947"],
             "When did India win the first world cup in cricket":["1983"],
             "When was the first T20 world cup held":["2007"],
             "Who won the first T20 world cup":["India","india","In","Bharat"],
             "Which cricketer has the most number of centuries in ODI":["Sachin tendulkar","Tendulkar"]}
print("length of questions list ",len(questions))  #print length of the questions dictionary


# random.randint(0,n) takes values from 0 to n-1.create random number using this module and give random questions to the user hence we create 
# random number access random question from the list and after that we can refence the question to the dictionary using dictionary[key]


print("items in the questions are",questions.items()) #prints tuple of list of key,values ([key1,value1],[key2,value2])
print()
print("keys in the questions are",questions.keys()) #prints tuple of list of keys only ([key1,key2,key3])
print()
# print(questions.keys()[0][2]) 
# this will always return dict_subscriptable meaning that the output is iterable but cannot be accessed using indexes
    # hence we cannot de questions.keys()[0] :- cannot access using indices
    # but we can iterate the non subscriptable object using loops:-
    # for i in questions.keys():
        # print(i)


quelist=list(questions.keys()) #as questions.keys() was not subscriptable to make it access using index we type cast it into list
print("List of keys" ,quelist) #prints only the questions in the form of list can be accessed easily using index
# print(quelist[ran])
print(questions.values()) #prints non subscriptable object
# print(questions.values()[0][2]) 
# this will always return dict_subscriptable meaning that the output is iterable but cannot be accessed using indexes
    # hence we cannot de questions.values()[0] :- cannot access using indices
    # but we can iterate the non subscriptable object using loops:-
    # for i in questions.values():
        # print(i)
    # to make it subscriptable type cast it into list

def getrandomnum():
        return random.randint(0,len(questions)-1)

    
ques=list(questions.keys())
chance=0
score=0
visitedquesind=[]
playsound("Training\Kbc - Starting sound.mp3")
for i in range(len(ques)):

    while True:
        randomindex=getrandomnum()
        if(randomindex in visitedquesind):
              randomindex=getrandomnum()
        else:
              visitedquesind.append(randomindex)
            #   print(randomindex)
              break
    question=ques[randomindex]
    playsound("Training\Kbc Question asking - Message Tone.mp3")
    print(ques[randomindex],end="")
    ans=input(": ")
    if ans in questions[question] :
          print("Right answer")
          playsound("Training\Kbc Correct Answer - Sound ! Notification.mp3")
          score=score+1
    else:
          playsound("Training\Kbc - Wrong Answer Sound.mp3")
          print("Wrong answer")

print(f"You correctly answered {score} out of {len(questions)} questions")
