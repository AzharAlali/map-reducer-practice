s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0
sum = 0.0

for line in s:
  data = line.strip().split('\t')
  pymentType = data

  if pymentType != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + float(thisValue)+'\n')

    # start over when changing keys
    thisKey = pymentType 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue += float(sum)

# output the final entry when done
r.write(thisKey + '\t' + (thisValue)+'\n')

s.close()
r.close()
