from googletrans import Translator

def translator(text):
	translator = Translator()
	return translator.translate(text, src="nl").text

