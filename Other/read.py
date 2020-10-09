filepath = "Input_files/file.txt"
with open(filepath) as fp:
	line = fp.readline()
	while line:
		line = line.strip()
		print(line)
		line = fp.readline()
fp.close()
