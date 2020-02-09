import re
 
log_file_path = r"SampleLog.log"
regex = '/t'
read_line = True
 
with open(log_file_path, "r") as file:
    match_list = []
    if read_line == True:
        for line in file:
            for match in re.finditer(regex, line):
                match_text = match.group()
                match_list.append(match_text)
                print(match_text)
    else:
        data = f.read()
        for match in re.finditer(regex, data):
            match_text = match.group()
            match_list.append(match_text)
file.close()