## Setup

Withing "data.json" you will find this, change all the data to be correct
```json
{
    "Address": "192.168.56.1",
    "Port": "8080",
    "Debug": true,
    "MaxLength": 2
}
```
Install dependencies with this command
```console
$ pip install -r requirements.txt
```
Start the api with the following command
```console
$ python Translate.py
```
Head over to the "Address" and "Port" you specified and add a langauge you want to translate and the content 
(example: localhost:8080/german/Hello Friend)
```json
{
  "Input": "Hello Friend", 
  "Langauge": "german", 
  "Output": "Hallo, Freund", 
  "Status": "Success"
}
```

## Use and output

`localhost:8080/<string:Language>/<string:Content>`

* Success 
```json
{
  "Input": "Hello Friend", 
  "Langauge": "german", 
  "Output": "Hallo, Freund", 
  "Status": "Success"
}
```
* Incorrect Translation Name
```json
{
  "Input": "He", 
  "Langauge": "examplename", 
  "Output": "'EXAMPLENAME' IS AN INVALID TARGET LANGUAGE . EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT", 
  "Status": "Fail"
}
```
* Content too long
```json
{
  "Code": "Content is too long (Max 2)", 
  "Status": "Fail"
}
```
