from flask import Flask
import json
from translate import Translator

app = Flask(__name__)

@app.route('/<string:lang>/<string:content>')
def hello_world(lang, content):
    if len(content) > json.load(open("data.json", "r"))["MaxLength"]:
        return {"Status": "Fail","Code": f"Content is too long (Max {json.load(open('data.json', 'r'))['MaxLength']})"}
    elif Translator(to_lang=lang).translate(content).endswith("EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT"):
        return {"Status": "Fail","Code": Translator(to_lang=lang).translate(content)}
    else:
        return {"Status": "Success","Langauge": lang,"Input": content,"Output": Translator(to_lang=lang).translate(content)}

if __name__ == "__main__":
    x = json.load(open("data.json", "r"))
    app.run(host=x["Address"], port=x["Port"], debug=x["Debug"]) 
