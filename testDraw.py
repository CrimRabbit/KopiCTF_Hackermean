import matplotlib.pyplot as plt
import numpy as np
import sys

# Solution produces tiny image, but no border -- OLD PRINT METHOD
# fig = plt.imshow(g, cmap='Greys')
# plt.axis('off')
# plt.imsave('blkwht.png',g,format="png",cmap="Greys")

#currently expects inputs in binary
def draw(text, key, outputFile):
	#print("Draw function received:",text,key,outputFile)
	with open(text) as input:
		inputText = input.readline()
		if(len(inputText) < key*key):
			raise ValueError("Text not at least key^2 length!")

		if(len(inputText) % key != 0):
			#padding with 0's
			n = len(inputText) % key
			inputText += '0'*(key - n)
		g = []
		for i in range(int(len(inputText)/key)):
			g.append([int(x) for x in inputText[i*key:(i+1)*key]])
			
		#print(g)
		#Solution has a 2px border
		fig = plt.imshow(g, cmap='Greys')
		plt.axis('off')
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)
		plt.savefig('outputFile', bbox_inches='tight', pad_inches = 0)

		plt.show()


if __name__ == "__main__":
	#print('Given arguments: ',str(sys.argv))
	try:
		draw(sys.argv[2],int(sys.argv[4]),sys.argv[6])
	except ValueError as e:
		print(e)
		sys.exit(1)
	except Exception as e:
		print(e)
		print("Usage: draw.py -i <inputFile> -k <keylength, int> -o <outputFile>")
		print("Note that contents expected of inputFile is a single line of binary input; 1 for black 0 for white")
		sys.exit(1)