# use mbox-short.txt as file name, and search for email addresses
# make a file such that the email address that occurs the most can be accessed
fname = raw_input("Enter file name: ")
try:
	fhand=open(fname)
except:
	print 'File cannot be opened:',fname
	exit()
emailadd=list()
somestuff=list()
alladd=dict()
#this section should produce a list of email addresses
#somestuff is all the split text in the line, with emailadd being just the email address
for line in fhand:
    if line.startswith("From "):
		somestuff=line.split()
		emailadd.append(somestuff[1])
#now taking the complete email list, the email addresses will be counted per occurance
#and stored in a dictionary called alladd (all addresses) with the number of time each 
#occurred
for email in emailadd:
	alladd[email]=alladd.get(email,0)+1
#now we will count occurances of each email address from the 
#alladd dictionary and save the largest count and the corresponding email
bigcount=None
bigemail=None
for email,count in alladd.items():
	if bigcount is None or count>bigcount:	
		bigcount=count
		bigemail=email
print bigemail, bigcount