#QUIZ SIMULATOR (using python)
import time
from datetime import datetime
today=datetime.now()
date=today.strftime("%d/%m/%Y")
print("QUIZ TEST")
print("\n")
print(date)

print("\nlet's play start")
start_time=time.time()
print(start_time)
quiz=[

   {
       "question":" If a train travels 60 km in 1 hour, how much distance will it cover in 3 hours?",
       "options":[ "A. 120 km ","B. 180 km" ,"C. 200 km" ,"D. 240 km"],
       "correct_answer":'B'
   },
   {
       "question":"What is 25%percentage of 200?",
       "options":["A. 25","B. 40","C. 50","D. 75"],
       "correct_answer":'C'
   },
   {
       "question":"Find the next number: 2, 4, 8, 16, ?",
       "options":["A. 20","B. 24","C. 30","D. 32"],
       "correct_answer":'D'
   },
   {
       "question":"A shopkeeper buys an item for ₹500 and sells it for ₹600. What is the profit?",
       "options":["A. ₹50","B. ₹75","C. ₹100","D. ₹150"],
       "correct_answer":'C'
   },
   {
       "question":"If 5 workers complete a task in 10 days, how many days will 10 workers take (same efficiency)?",
       "options":["A. 2","B. 4","C. 5","D.8"],
       "correct_answer":"C"
   }
]


total_question=len(quiz)
score=0
for index,i in enumerate(quiz,start=1):
    print(f'question{index}:{i["question"]}')
    for option in i['options']:
        print(option)

    user_answer=input("enter options(A/B/C/D): ").strip().upper()
    if user_answer == i['correct_answer']:
        print("correct_answer\n")
        score+=1
    else:
        print(f"wrong answer. correct_answer was {i['correct_answer']}.\n")


for j in quiz:
        if time.time()-start_time>=60:
              print("game over")
              break       
remaining =60-(time.time()-start_time)
print(remaining)
percentage=(score/total_question)*100
print("end quiz")
print(f"final result: {score}/{total_question}")
print(percentage,"%")


