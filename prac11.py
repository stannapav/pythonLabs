#2
file = "monologue of hamlet"
with open(file + ".txt", "r") as f:
    print(file + ':')
    for line in f:
        print(line)

#3
with open(file + ".txt", "r") as f, open("betterTxt.txt", "w") as w:
    for line in f:
        w.write(">" + line)

#4
nums = "nums.txt"
with open(nums, "r") as f, open("betterNums.txt", "w") as w:
    numbers = f.readline()
    numStr = numbers.split()
    numList = [int(x) for x in numStr]
    numStr = " ".join(str(c) for c in sorted(numList))
    w.write(numStr)