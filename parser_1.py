# For each file
import re
import os

for dir in ["r9k/", "out/"]:
#filename = "r9k_72938968.txt"
    for filename in os.listdir(dir):

        if not os.path.isfile(dir+filename):
            continue

        f = open(dir+filename, "r", encoding="utf-8", errors="ignore")

        all_lines = f.readlines()
        f.close() 
        new_lines = []
        all_lines = all_lines[1:]
        citations = []
        plain_text = []
        used = False
        for line in all_lines:
            line = line.lstrip()
            new_comm = re.match(r"--- [0-9]+", line)
            refs = re.match(r">>[0-9]+", line)
            if refs:
                continue
            if new_comm:
                used = False
                res = "\2"
                if plain_text:
                    new_lines.append("\2")

                    citations = []                  
                    new_lines.append("".join(plain_text))
                    plain_text = []
                        #new_lines.append(res)
                #elif line[0] == ">":
                #    res = line[1:]
                #    last_comment += res
            else:
                    
                if line:
                    if line[0] == ">":
                        if not used:
                            if plain_text:
                                if citations:
                                    for cit in citations:
                                        new_lines.append("\2")
                                        new_lines.append(cit)
                                        new_lines.append("\2")
                                        new_lines.append("".join(plain_text))
                                else:
                                    new_lines.append("\2")
                                    new_lines.append("".join(plain_text))

                                plain_text = []
                                citations = []
                        used = True
                        while line[0] == ">":
                            line = line[1:]
                        citations.append(line)

                    else:
                        plain_text.append(line)
                        used = False
                    

        if plain_text:
            new_lines.append("\2")
            new_lines.append("".join(plain_text))
            

        out = open(dir+"res/"+filename, "w", encoding="utf-8")
        out.writelines(new_lines)
        out.close()
    
#print(all_lines)