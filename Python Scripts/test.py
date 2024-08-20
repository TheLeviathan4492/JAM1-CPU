import sys

def get_file():
  if len(sys.argv) != 2:
    print("add file")
    sys.exit(1)
  file_name = r'C:\JAM-1 Files\Assembly Code\\' + sys.argv[1]
  file_name = file_name[:28] + file_name[29:]
  print(file_name)

print("greetings")