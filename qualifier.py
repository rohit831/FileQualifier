import re
import os


# This function parses a file and will remove unwanted characters from
# it as well as tag the lines and store the output in two files
def tag_file(src_file, delimiter, no_of_columns):
    accept_data = []
    reject_data = []

    def add_to_list(data, no_of_cols):
        if len(data.split(delimiter)) == no_of_cols:
            accept_data.append(data)

        elif len(data.split(delimiter)) > no_of_cols:
            data = data.rstrip("\n")
            data += "  --too many columns\n"
            reject_data.append(data)

        else:
            data = data.rstrip("\n")
            data += "  -- very less columns\n"
            reject_data.append(data)

    pattern = r'(?!(([^"]*"){2})*[^"]*$)' + delimiter
    with open(src_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip(" ").strip("\n") in "":
                pass
            elif line.count('"') % 2 != 0:
                tmp = line.replace('"', '')
                add_to_list(tmp, no_of_columns)

            else:
                tmp = re.sub(pattern, " ", line).replace('"', '')
                add_to_list(tmp, no_of_columns)

    with open(os.path.splitext(src_file)[0] + '-accept' + os.path.splitext(src_file)[1], "w") as f:
        [f.write(line) for line in accept_data]

    with open(os.path.splitext(src_file)[0] + '-reject' + os.path.splitext(src_file)[1],"w") as f:
        [f.write(line) for line in reject_data]


# This function parses a file according to a delimiter
# and will remove unwanted characters from it
def file_fix(src_file, delimiter, update_file=False):
    data = []
    pattern = r'(?!(([^"]*"){2})*[^"]*$)' + delimiter
    with open(src_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.count('"') % 2 != 0:
                tmp = line.replace('"', '')
                data.append(tmp)
                # print(data, end="")
            else:
                tmp = re.sub(pattern, " ", line)
                data.append(tmp.replace('"', ''))
                # print(data, end="")

    if update_file:
        with open(src_file,"w") as f:
            [f.write(line) for line in data]

    print("Printing data .. ")
    [print(line, end="") for line in data]
