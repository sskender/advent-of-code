import sys

question_groups = sys.stdin.read().split("\n\n")
question_groups = [[j for j in i.split("\n") if j] for i in question_groups]

questions_sum = 0
for question in question_groups:
    everyone_yes = set(question[0])
    for person in question[1:]:
        everyone_yes &= set(person)
    questions_sum += len(everyone_yes)

print(questions_sum)
