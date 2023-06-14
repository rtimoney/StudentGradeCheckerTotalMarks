from cgitb import text
from collections import OrderedDict
from curses import echo
import json

def getTotal(input_text):

    total = 0

    if input_text is not None:
        
        
        
        #usrinput ='placeholder'
        usrinput = []
        usrinput = input_text.split("newline") # --> ['Line 1', 'Line 2', 'Line 3']

        

        
        
        for i in usrinput:
            line = i.split(",")

            thismodule = int(line[1])
            total = total + thismodule
            
            #total = total + 1
            
            
    return total