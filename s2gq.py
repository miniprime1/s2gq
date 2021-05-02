import sys

logo = """ ____ ____   ____  ___  
/ ___|___ \ / ___|/ _ \ 
\___ \ __) | |  _| | | |
 ___) / __/| |_| | |_| |
|____/_____|\____|\__\_\\
[Semicolon to Greek Question Mark]
"""

print(logo)

file_list = []
for i in range(1, len(sys.argv)):
    file_list.append(sys.argv[i])

for k in file_list:
    print(f"Converting {k}")
    fread = open(k, "r")
    before = fread.read()
    after = before.replace(";", ";")
    fread.close()
    fwrite = open(k, "w", encoding="utf-8")
    fwrite.write(after)
    fwrite.close()

print("Done!")