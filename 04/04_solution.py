FILE = "input"

#Takes a line from file; converts elf ranges to a list of two sets
def convert_ranges(line):
    elfs = line[:-1].split(",") #splitting into list with: [elf1, elf2]
    elfs = [set(range(int(elf.split("-")[0]), int(elf.split("-")[1])+1)) for elf in elfs]  #converting that list into two ranges
    return elfs

#Iterates through the lines of a file, using convert_ranges; then counts overlap depending on what task conditions are & returns count
def count_overlaps(file, task):
    counter = 0
    for line in file:
        elfs = convert_ranges(line)
        counter += task(elfs)
        
    return counter 


#TASK ONE: takes intersection, and if it's equal to either of the elf sets it returns 1 to add to count
def task_one(elfs):
    intersection = elfs[0].intersection(elfs[1])  
    return 1 if intersection == elfs[0] or intersection == elfs[1] else 0 

#TASK TWO: takes intersection; if it's nonzero, it returns 1 to add to count
def task_two(elfs):
    intersection = elfs[0].intersection(elfs[1])
    return 1 if len(intersection) > 0 else 0 


#PRINTING SOLUTIONS
def do_task(task, file_name = FILE):
    file = open(file_name, "r")
    answer = count_overlaps(file, task)
    file.close()
    return answer 

def print_solutions():
    print("TASK 1:", do_task(task_one))
    print("TASK 2:", do_task(task_two))
    return
    
print_solutions()