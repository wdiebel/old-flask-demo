import speech_recognition as sr
import sys
import time
import os

r = sr.Recognizer()


#print(sys.argv)

#strFileToSave = sys.argv[0]
#strFileToSave = strFileToSave + '.txt'

print("Input Command")

#os.system('pause')

with sr.Microphone() as source:
	audio_data = r.record(source, duration=5)
	print("Recognizing...")

	# convert speech to text
	text = r.recognize_google(audio_data)
	print(text)







	#writeFile = open(strFileToSave, "x")
	#writeFile.write(text)
	#writeFile.close()