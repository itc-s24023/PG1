with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)

with open("sample.txt", "r") as f:
     for line in f:
         print(line.strip())

