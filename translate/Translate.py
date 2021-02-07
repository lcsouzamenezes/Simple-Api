from flask import Flask
import json
from translate import Translator

app = Flask(__name__)

@app.route('/<string:lang>/<string:content>')
def hello_world(lang, content):
    if len(content) > json.load(open("data.json", "r"))["MaxLength"]:
        return {"Status": "Fail","Code": f"Content is too long (Max {json.load(open('data.json', 'r'))['MaxLength']})"}
    if Translator(to_lang=lang).translate(content)[12:].startswith("INVALID"):
        return {"Status": "Fail","Code": Translator(to_lang=lang).translate(content)}

    return {"Status": "Success","Langauge": lang,"Input": content,"Output": Translator(to_lang=lang).translate(content)}

if __name__ == "__main__":
    x = json.load(open("data.json", "r"))
    app.run(host=x["Address"], port=x["Port"], debug=x["Debug"]) 