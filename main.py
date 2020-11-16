import os
import datetime
import subprocess
import datetime


def start_programm():
	getCuneiformText()


def getCuneiformText():

	os.system('cuneiform -l eng Text_outputs/123.png -o out')
	p = subprocess.Popen('cat out | ispell | grep -v ok', universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	text = p.stdout.read()
	retcode = p.wait()
	writeTextToFile(text)



def writeTextToFile(text):

	filename = datetime.datetime.now()

	with open('RecognizedText/{}'.format(filename), 'w') as file:

		file.write(text)

	parseFile(filename)



def parseFile(filename):

	all_lines = []

	with open('RecognizedText/{}'.format(filename), 'r') as file:
		for line in file.readlines():
			if len(line) != 0 and line != '\n' and 'not found' not in line and len(line) >= 8:
				all_lines.append(line.replace('\n', ''))

	for line in all_lines:
		print(line)



if __name__ == '__main__':
	start_programm()