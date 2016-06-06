print("FastaFileReader");

file = open("Boleracea.v1.cds.fasta");

sequenceDict = dict();

for line in file:
	if line.startswith(">"):
		header = line[1:];
		sequenceDict[header] = "";
	else:
			sequenceDict[header] += line;


headerFile = open("BroccoliHeaders.txt", 'w');
for k, v in sequenceDict.iteritems():
	headerFile.write(k);
headerFile.flush();
headerFile.close();
print("done");


