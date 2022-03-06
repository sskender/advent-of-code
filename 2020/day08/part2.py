import sys
import copy

program = sys.stdin.read().strip().split("\n")

# [ operation, argument, executed ]
instructions = list()
for i in program:
    operation = i.split(" ")[0]
    argument = int(i.split(" ")[1])
    executed = False
    instructions.append([ operation, argument, executed ])

NOP = "nop"
ACC = "acc"
JMP = "jmp"

accumulator = 0

def computer(pc, instruction):
    global accumulator
    print(f"Executing: {instruction[0]} {instruction[1]}")

    if instruction[2]:
        print(f"Inf loop detected")
        return -1
    else:
        instruction[2] = True

    if instruction[0] == NOP:
        return pc + 1
    if instruction[0] == ACC:
        accumulator += instruction[1]
        return pc + 1
    if instruction[0] == JMP:
        return pc + instruction[1]

def run(instructions_list):
    global accumulator
    pc = 0
    while True:
        print(f"Before instruction: PC={pc} ACCUMULATOR={accumulator}")
        pc = computer(pc, instructions_list[pc])
        print(f"After instruction: PC={pc} ACCUMULATOR={accumulator}")
        if pc == -1:
            return -1
        if pc >= len(instructions):
            print("Exiting gracefully")
            return 0


for i in range(len(instructions)):
    accumulator = 0
    instructions_modified = copy.deepcopy(instructions)
    instruction = instructions_modified[i]
    if instruction[0] == JMP or instruction[0] == NOP:
        if instruction[0] == NOP:
            instruction[0] = JMP
        elif instruction[0] == JMP:
            instruction[0] = NOP
    exit_code = run(instructions_modified)
    if exit_code == 0:
        break
