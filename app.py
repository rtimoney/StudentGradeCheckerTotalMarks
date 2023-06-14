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
#from flask_cors import CORS



app = Flask(__name__)
app.run()














@app.route('/', methods=['GET'])  
def hello():
 
    output = {'error':'false','string':'','answer':'blank'}
    #input_text_rec = (request.headers)
    
    #input_text_rec = request.headers.get('input_text')
    args = request.args
    input_text_rec = args.get('input_text')   
        
        #print(request.headers)
        #input_text_rec = request.headers.get('ronan')
        

       




        #input_text_rec = request.headers.get('input_text')


    output = {'error':'false','string':'','answer':input_text_rec}

        #input_text_rec = request.headers.post('input_text')
        


        

        #input_text_rec = "software engineering,999newlinedatabases,55newlineweb development,1newlinecomputing foundations,1newlinecloud computing,1"
        #input_text_rec = "software%20engineering,99newlinedatabases,55newlineweb%20development,1newlinecomputing%20foundations,1newlinecloud%20computing,1"
        
    answer = getTotal(input_text_rec)
    output = {'error':'false','string':'','answer':answer}

        #answer=500

        #answer = stored
        #output['answer']= answer
        #print(json.dumps(output),end="")

        #jsonString = json.dumps(output, indent=4)



        
        #print(jsonString)
        #return (output)

    print (input_text_rec)



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
    
    
    










