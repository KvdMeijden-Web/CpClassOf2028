# Goal:
# Find the average score of students who passed.
# Rules:
# - Pass mark is 50 or higher
# - Average should be based ONLY on passed students
# Program runs fine but gives the wrong result.

scores = [40, 50, 60, 30, 80]

def average_of_passed(marks):
    total = 0
    count = 0

    for score in marks:
        if score >= 50:
            total += score
        count += 1  

    return total / count

result = average_of_passed(scores)
print("Average of passed students:", result)