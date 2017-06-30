file= open("raw_data/washington.txt", "r").readlines()
content_set=set(file)
data = open("final_data/washington.txt","w")
for line in content_set:
    data.write(line)