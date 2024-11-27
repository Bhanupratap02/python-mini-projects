print("Welcome To The Quiz")
playing = input("Do you Want to Play?")

if playing.lower() != "yes":
    quit()
print("Okay! Let's Play :)")
score = 0
answer = input("What Does CPU Stand For? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("What Does GPU Stand For? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 


answer = input("What language does computer understand? ")
if answer.lower() == "binary":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 


answer = input("React is a framework or library ? ")
if answer.lower() == "library":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

print("You got " + str(score) + " questions correct!")
percent = (score / 4)*100
print(f"You got {percent} %")