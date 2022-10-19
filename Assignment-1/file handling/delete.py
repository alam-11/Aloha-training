import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("the file does not exist")