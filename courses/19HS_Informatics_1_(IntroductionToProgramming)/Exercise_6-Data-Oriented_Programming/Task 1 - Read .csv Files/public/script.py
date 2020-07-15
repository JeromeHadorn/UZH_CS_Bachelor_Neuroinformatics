# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def read_csv(path):
    f = open(path)
    giantArray = []
    for line in f.readlines():
        line = line.strip()
       # print(line)
       # print(line.split(","))
        rowData = line.split(',')
        if line == "":
            continue
        #print(tuple(rowData))
        giantArray.append((tuple(rowData)))
    f.close()
    return giantArray

# You can play around with your solution from within this block.
if __name__ == '__main__':
    print(read_csv("public/example.csv"))
