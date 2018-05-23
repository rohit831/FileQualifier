import qualifier as q

src_path = "/media/rohit/New Volume/PROJECTS/FileQualifier/TextQualifier.txt"
delimiter = '~'

# This will remove all the unwanted symbols in the file
#  And will also store the output in two different files
q.tag_file(src_path, delimiter, no_of_columns=3)
