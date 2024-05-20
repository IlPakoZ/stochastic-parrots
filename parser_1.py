# For each file
import re
import os

dir = "../r9k/"
#filename = "r9k_72938968.txt"
for filename in os.listdir(dir):
    if not os.path.isfile(dir+filename):
        continue
    f = open(dir+filename, "r")
    all_lines = f.readlines()
    f.close()
    new_lines = []
    all_lines = all_lines[1:]
    last_comment = ""
    for line in all_lines:
        new_comm = re.match(r"--- [0-9]+", line)
        refs = re.match(r">>[0-9]+", line)
        if refs:
            continue
        if new_comm:
            res = "<comment>\n"
            if last_comment:
                new_lines.append(last_comment)
                last_comment = ""
            new_lines.append(res)
        elif line[0] == ">":
            res = line[1:]
            last_comment += res
        else:
            last_comment += line
    new_lines.append(last_comment)
        

    #new_lines.append("<commentsend>")
    

    out = open(dir+"res/"+filename, "w")
    out.writelines(new_lines)
    out.close()

#print(all_lines)