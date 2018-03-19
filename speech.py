import speech_recognition as sr
 
def voice_querry():
 	r = sr.Recognizer()
 	with sr.Microphone() as source:
     		print "\n\n\t\tSay what to play!"
     		audio = r.listen(source)
 	try:
    		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    		# instead of `r.recognize_google(audio)`
   	    return r.recognize_google(audio)
	except:
		pass


