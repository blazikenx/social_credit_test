import time
score = 0
print("Welcome to the Chinese Government's Official 2021 Social Credit Exam!")
time.sleep (2)
print("Today I will be assessing you on important knowledge that you should already know, so if you're stressed you shouldn't be.")
time.sleep (1)
person1 = input("Question 1: Who is this person? (Please open this link in a separate browser DO NOT CHEAT https://i.redd.it/a1zcxisgjls71.png) (Grammer and spelling will be judged!)\n")
if person1 == ('John Xina'):
    print('Well done! You have gotten this question correct. Your social credit score has increased by 15!')
    score = score +15
else:
    print('Yikes, you got that wrong! Shame on you! -15 social credit!')
    score = score -15
time.sleep (2)
person2 = input("Question 2: Who is this person? (Same rules as last time, here's your link: https://i.kym-cdn.com/photos/images/newsfeed/002/229/102/5c5.jpg)\n")
if person2 == ('The Wok'):
    print('Excellent job! You have correctly answered thje quiestion! Your social credit score has increased by 30!')
    score = score +30
else:
    print('Shame on you! Your social credit score has decreased! Be weary that if your score becomes too low there will be some issues!')
    score = score -30
time.sleep (2)
Tiananmen = input("Did something happen in Tiananmen Square in 1989? Please type 'Yes' or 'No'\n")
if Tiananmen == ('No'):
    print("Well done! +100 social credit")
    score = score +100
else:
    print("Shame on you! Please review your history class materials! -100 social credit")
    score = score -100
time.sleep (2)
taiwan = input("Is Taiwan a country? Please input 'Yes' or 'No'\n")
if taiwan == ("No"):
    print("Well done! +50000000 social credit")
    score = score +50000000
else: 
    print("Yikes! Shame on you!")
    score = score -50000000
time.sleep (2)
print("Your final score was:"); print(score)
if score == 50000145:
    print("Congratulations, you have passed the 2021 Chinese Social Credit Exam!")
else: print("Shame on you! Your execution date will be determined soon. Please expect a letter or package in the mail that will give more details, DO NOT DISCARD THE MAIL!")
time.sleep (3)
exit