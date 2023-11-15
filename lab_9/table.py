import sys

try: 
  with open("data.txt") as file:
    file_contents = file.readlines()
    cols = len(file_contents[0].split("\t"))
    print(f"\\begin{{center}} \n\t \\begin{{tabular}}{{| {' ' + 'm{2cm} | ' * cols}}} \n\t\t \\hline") 

    for row in file_contents:
      numList = row.split()
      print("\t\t\t", end="")
      for i in range(len(numList)-1):
        print(f"{numList[i]} & ", end="")
      print(numList[-1], "\\\\ \n \t\t\t \\hline")
  
    print(f"\t\t \n\t \\end{{tabular}} \n \\end{{center}}") 
except Exception as error:
  print(error, file=sys.stderr)