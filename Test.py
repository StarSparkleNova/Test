import os

folder = input("What folder should I check?")
#folder = "input"

print("Contents of folder "+ folder)
files = os.listdir(folder)
for f in files:
  print("  " + f)
print()

for filename in files:
  print("contents of "+filename)
  f = open(folder+"/"+filename)
  contents = ""
  for line in f:
    contents += line

  f.close()
  # search and replace HERE!!
  # https://www.w3schools.com/python/ref_string_replace.asp
  contents += "!!!!"
  print(contents)

  f = open("output/" + filename, "w")
  f.write(contents)
  f.close()





