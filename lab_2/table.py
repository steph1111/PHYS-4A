import sys

try: 
  with open("/Users/stephanie/Documents/_PHYS-4A/r_cubed/lab_2/pencil_data_steph.txt") as file:
    file_contents = file.readlines()
    cols = len(file_contents[0].split("\t"))
    print(f"\\begin{{center}} \n\t \\begin{{tabular}}{{| {' ' + 'c || ' * cols}}} \n\t\t \\hline") 

    for row in file_contents:
      numList = row.split()
      for i in range(len(numList)-1):
        print(f"\t\t\t {numList[i]} & ", end="")
      print(numList[-1], "\\\\ \n \t\t\t \\hline")
  
    print(f"\t\t \n\t \\end{{tabular}} \n \\end{{center}}") 
except Exception as error:
  print(error, file=sys.stderr)