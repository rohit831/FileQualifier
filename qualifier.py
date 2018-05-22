import re


def file_parse(src_file,delimiter, target_true_file, doubt_file):
    pass

pattern = r'(?!(([^"]*"){2})*[^"]*$)~'

with open("TextQualifier.txt","r", encoding="utf-8") as f:
    for line in f:
        if line.count('"') % 2 != 0:
            # data = line.rstrip("\n")
            data = line.replace('"', '')
            print(data, end="")
        else:
            data = re.sub(pattern, "", line)
            data = data.replace('"', '')
            print(data, end="")


