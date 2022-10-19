# in python open function is useď for opening the file in different mode


# syntax:-
# open(filename,modes)

# There are four methods for opening file
# "r" - Read - Defalt value  opens a file for reading , error if the file does not exist
# "a" - append - opens a file appending mode , creates the file iƒ it does not exist
# "w" - write - opens a file for writing, creates the file if it does not exist or if already exist it overwrite the content
# "x" - create - creates the specificied file, returns an error if the file exists

# We can also specify that file should be handled as binary or text mode
# "t" - Text - Default value.Text mode
# "b" - Binary - Binary mode(e.g images)

# fp = open("read_mode.txt", "r")
fp = open("write_mode.txt", "w")
fp = open("append_mode.txt", "a")
fp = open("create_mode.txt", "x")
fp.close()
