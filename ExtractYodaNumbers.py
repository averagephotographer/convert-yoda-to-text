
file = open('yoda.txt', 'rt')
charts = []
titles:str = []


file_list = []
for line in file:
  file_list.append(line)

# for i, _ in enumerate(file_list):
i = 0
while i < len(file_list):
  # get title
  if file_list[i].startswith("BEGIN YODA_HISTO1D"):
    # splitting each beginning line at the slash
    line_split = file_list[i].split("/")
    long_title = line_split[-1]
    # if you need the bracket text, you would get it from long_title
    short_title = long_title[:3]
    titles.append(long_title)


  # get chart headings
  if file_list[i].startswith("# xlow"):
    heading = file_list[i][2:].split()
    reached_end = False
    table = []

    # gets each line from and individual chart
    while True:
      i += 1
      if file_list[i].startswith("END"): 
        table.append(["END"])
        charts.append(table)
        break
      # remove the last item in the list (a newline), where there are tabs split the spring into a list, and append that list to the table
      table.append(file_list[i][:-1].split("\t"))

  i+=1

with open("text.txt", "w") as file:
  for i in range(len(charts)):
    # skip all charts with a [ in the title 
    if "[" in titles[i]:
      continue # starts the loop over from the next 'i", skipping the code below
               # kinda like a "go directly to GO and collect $200" but without the money
    file.write(titles[i])
    file.write(" ".join(heading))
    file.write("\n")
    # write each
    for line in charts[i]:
      file.write(" ".join(line))
      file.write("\n")
    file.write("\n")
