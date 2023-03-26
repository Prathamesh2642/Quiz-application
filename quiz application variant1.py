#Quiz type 1 - Normal
# for first type of quiz

questions={"question":"answers"}

score=0
# for getting value from a dictionary we do this:- dictionary[key]
for question in questions:
    print(question,end="")
    ans=input(": ")
    if(questions[question].lower()==ans.lower()):
        score=score+1
        print("Right Answer")
    else:
        print("Wrong Answer")
print(f"You correctly answered {score} out of {len(questions)} questions")
