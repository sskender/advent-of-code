import sys

question_groups = sys.stdin.read().split("\n\n")
print(sum([len(set(i.replace("\n", "").strip())) for i in question_groups]))
