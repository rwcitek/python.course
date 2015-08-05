# use mbox-short.txt as file name, and search for email addresses
# make a file such that the email address that occurs the most can be accessed
fname = "mbox-short.txt"
fname = raw_input("Enter file name: ")
try:
  fhand=open(fname, 'r')
except:
  print 'File cannot be opened:',fname
  exit()

alladd=dict()
email=""
#this section should produce a dictionary with ...
# the email address as the key and the count as the value
for line in fhand:
  if line.startswith("From "):
    email=line.split()[1]
    if email in alladd:
      alladd[email] += 1
    else:
      alladd[email] = 1

#now we will count occurances of each email address from the 
#alladd dictionary and save the largest count and the corresponding email
bigemail=None
bigcount=None
for email,count in alladd.items():
  if bigcount is None or count>bigcount:	
    bigemail=email
    bigcount=count

print bigemail, bigcount

