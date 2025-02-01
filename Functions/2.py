#Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(score):
    if score > 1.0 or score < 0.0:
        return "enter the score between 0 and 1"
    
    if score >= 0.9:
        return "your grade is: A"
    elif score >= 0.8:
        return "your grade is: B"
    elif score >= 0.7:
        return "your grade is: C"
    elif score >= 0.6:
        return "your grade is: D"
    else:
        return "fail"
try: 
    score = float(input("Enter the score: "))
    result = computegrade(score)
    print(result)

except ValueError:
    print("enter the valide numaric value")
