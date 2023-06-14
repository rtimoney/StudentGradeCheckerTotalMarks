#from crypt import methods
from email import header
from http.client import HTTPResponse
import mimetypes
from textwrap import indent
import time
import json
from urllib import response
#import redis
from flask import Flask, render_template
from flask import request
#from flask import request
from functions import getTotal



app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)





@app.route('/', methods=['GET'])   #@app.route('/', methods=['GET','POST']) 
  


def hello():
    
    
    #input_text_rec = 'placeholder'
    output = {'error':'false','string':'','answer':''}
    
    
    
    if request.method == "GET":

        
        header = 'input_text'
        
        
        input_text_rec = request.headers.get('input_text')
        
        

       




        #input_text_rec = request.headers.get('input_text')


        output = {'error':'false','string':input_text_rec,'answer':''}

        #input_text_rec = request.headers.post('input_text')
        


        

        #input_text_rec = "software engineering,999newlinedatabases,55newlineweb development,1newlinecomputing foundations,1newlinecloud computing,1"
        #input_text_rec = "software%20engineering,99newlinedatabases,55newlineweb%20development,1newlinecomputing%20foundations,1newlinecloud%20computing,1"
        
        answer = getTotal(input_text_rec)

        #answer=500

        #answer = stored

        print('line 1')
        output['answer']= answer
        #print(json.dumps(output),end="")

        jsonString = json.dumps(output, indent=4)



        
        print(jsonString)
        return (output)



        #exit
        #app.run()
        
        
        
        
        
        
    print(json.dumps(output))
        #return 'success'
    return (output)
    return (json.dumps(output))
    return (json.dumps(input_text_rec))


if __name__ == "__main__":
    app.run()
    
    
@app.after_request
def after_request(response):
  response.headers.set('Access-Control-Allow-Origin', '*')
  response.headers.set('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.set('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response 
    
    
    
    #return 'Hello World! I am now updated to version 1.1.3 and I have been seen {} times.\n'.format(count)









