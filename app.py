from sanic import Sanic, request
from googletrans import Translator
import json
from multiprocessing import cpu_count
from sanic_cors import CORS

app = Sanic(__name__)

def translate(text):
	"""
	This function wraps the google translate service.
	It requires a connection to the internet.  If the
	internet doesn't end up working, this translation service
	will not work.  Also, I make no guarantees for how long this service
	will work.  If google changes it api, depricates something, or changes
	it's web page, this service might break.

	Parameter:
	@text - this function assumes you are passing dutch.
	Notice the `src` parameter in translator.translate.
	This parameter specifies the source language.
	If dealing with another language, feel free to update this parameter
	and relaunch the service.  Or add other translators.
	You can also specific the target with:
	  
	"""
	translator = Translator()
	return translator.translate(text, src="nl").text

@app.route("/", methods=["GET", "POST"])
async def index():
	json_data = request.get_json()
	data = json.loads(json_data)
	dutch = data["text"]
	result = {
		"dutch": dutch,
		"english": translate(data["text"])
	}
	return json.dumps(result) 

if __name__ == '__main__':
        app.run(workers=cpu_count())
