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
Head over to the "Address" and "Port" you specified and add a langauge you want to translate and the content (example: localhost:8080/german/Hello Friend)
