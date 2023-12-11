import sys

def prepare(inputs):
	outputs = ""
	cursor = 0
	for i in inputs:
		cursor += 1
		outputs += str(i)
		if (cursor != len(inputs)):
			outputs += ","
	return outputs

def tokenize(input):
	output = []
	current = ""

	for i in input:
		if ((i == " ") or (i == "	")):
			output.append(current)
			current = ""
			continue
		current += i
	
	return output

def extract_order(input):
	file = open(input, "r", encoding = 'utf-8')
	treebank = file.readlines()

	oCount = 0
	ovCount = 0
	voCount = 0

	lineCount = 0

	for l in treebank:
		lineCount += 1
		text = l.strip()
		tokens = tokenize(text)

		if (len(tokens) == 0):
			continue

		if (tokens[0] == "#"):
			continue

		cursor = 0

		for t in tokens:
			if (t == "obj"):
				oCount += 1
				if (int(tokens[0]) < int(tokens[cursor - 1])):
					ovCount += 1
				else:
					voCount += 1
			cursor += 1

	# Now we've finished going through all our
	# trees, we can spit out our findings.

	return oCount, (ovCount / oCount), (voCount / oCount)

labels = []
ovs = []
vos = []

argCount = 0
for arg in sys.argv:

	argCount += 1
	if (argCount == 1):
		continue

	langCode = ""

	for c in arg:
		if (c == "_"):
			break
		langCode += c
		
	o, ov, vo = extract_order(arg)

	labels.append(langCode)
	ovs.append(ov)
	vos.append(vo)
	
	print(langCode + " // O: " + str(o) + " // OV:" + str(ov) + " // VO: " + str(vo))

# I'm thoroughly ready for the semester to be over.

label_outputs = prepare(labels)
ov_outputs = prepare(ovs)
vo_outputs = prepare(vos)

output = label_outputs + "\n" + ov_outputs + "\n" + vo_outputs
outfile = open("outputs.csv", "a")
outfile.write(output)
outfile.close()