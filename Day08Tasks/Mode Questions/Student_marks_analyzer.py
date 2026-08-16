# Student Marks File Analyer

file=open("marks.txt","r")
total=0
count=0
print("Student Records:")
for line in file:
    line=line.strip()
    if line =="":
        continue
    print(line)
    data=line.split()
    marks=int(data[-1])
    total=total+marks
    count=count+1
average=total/count
print("Average Marks:",average)
file.close()
