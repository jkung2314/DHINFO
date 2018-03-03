from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
import requests
import re
import urllib.request
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms():

    message_body = request.form['Body'].lower()

    cowell = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell&sName=&naFlag=', 'Cowell/Stevenson Dining Hall'
    ten = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=College+Nine+%26+Ten&sName=&naFlag=', 'Colleges Nine & Ten Dining Hall'
    merill = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill&sName=&naFlag=', 'Merill Cowell'
    porter = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=25&locationName=Porter&sName=&naFlag=', 'Porter College'
    rcc = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag=', 'Rachel Carson College'

    #cowell
    end_array=[]
    breakfastIndex=-1
    lunchIndex=-1
    dinnerIndex=-1
    lateNightIndex=-1

    html = urllib.request.urlopen(cowell)
    soup = BeautifulSoup(html, "html.parser")
    data = soup.findAll(text=True)
    result = filter(visible, data)
    raw_code = list(result)
    length = len(raw_code)

    breakfastArray_cowell=[]
    lunchArray_cowell=[]
    dinnerArray_cowell=[]
    lateNightArray_cowell=[]

    wordbank=["\n","Recipe Name Is Displayed Here","Nutrition Info","\xa0"]

    for x in raw_code:
        for y in wordbank:
            if y in x:
                break
        else:
            end_array.append(x)
    for x in end_array:
        if "Breakfast" in x:
            breakfastIndex=end_array.index(x)
        elif "Lunch" in x:
            lunchIndex=end_array.index(x)
        elif "Dinner" in x:
            dinnerIndex=end_array.index(x)
        elif "Late Night" in x:
            lateNightIndex=end_array.index(x)


    breakfastArray_cowell=end_array[breakfastIndex:lunchIndex]
    lunchArray_cowell=end_array[lunchIndex+1:dinnerIndex]
    dinnerArray_cowell=end_array[dinnerIndex+1:lateNightIndex]
    lateNightArray_cowell=end_array[lateNightIndex+1:-9]



    #ten
    end_array=[]
    breakfastIndex=-1
    lunchIndex=-1
    dinnerIndex=-1
    lateNightIndex=-1

    html = urllib.request.urlopen(ten)
    soup = BeautifulSoup(html, "html.parser")
    data = soup.findAll(text=True)
    result = filter(visible, data)
    raw_code = list(result)
    length = len(raw_code)

    breakfastArray_ten=[]
    lunchArray_ten=[]
    dinnerArray_ten=[]
    lateNightArray_ten=[]

    wordbank=["\n","Recipe Name Is Displayed Here","Nutrition Info","\xa0"]

    for x in raw_code:
        for y in wordbank:
            if y in x:
                break
        else:
            end_array.append(x)
    for x in end_array:
        if "Breakfast" in x:
            breakfastIndex=end_array.index(x)
        elif "Lunch" in x:
            lunchIndex=end_array.index(x)
        elif "Dinner" in x:
            dinnerIndex=end_array.index(x)
        elif "Late Night" in x:
            lateNightIndex=end_array.index(x)


    breakfastArray_ten=end_array[breakfastIndex:lunchIndex]
    lunchArray_ten=end_array[lunchIndex+1:dinnerIndex]
    dinnerArray_ten=end_array[dinnerIndex+1:lateNightIndex]
    lateNightArray_ten=end_array[lateNightIndex+1:-9]




    #merill
    end_array=[]
    breakfastIndex=-1
    lunchIndex=-1
    dinnerIndex=-1
    lateNightIndex=-1

    html = urllib.request.urlopen(merrill)
    soup = BeautifulSoup(html, "html.parser")
    data = soup.findAll(text=True)
    result = filter(visible, data)
    raw_code = list(result)
    length = len(raw_code)

    breakfastArray_merrill=[]
    lunchArray_merrill=[]
    dinnerArray_merrill=[]
    lateNightArray_merrill=[]

    wordbank=["\n","Recipe Name Is Displayed Here","Nutrition Info","\xa0"]

    for x in raw_code:
        for y in wordbank:
            if y in x:
                break
        else:
            end_array.append(x)
    for x in end_array:
        if "Breakfast" in x:
            breakfastIndex=end_array.index(x)
        elif "Lunch" in x:
            lunchIndex=end_array.index(x)
        elif "Dinner" in x:
            dinnerIndex=end_array.index(x)
        elif "Late Night" in x:
            lateNightIndex=end_array.index(x)


    breakfastArray_merrill=end_array[breakfastIndex:lunchIndex]
    lunchArray_merrill=end_array[lunchIndex+1:dinnerIndex]
    dinnerArray_merrill=end_array[dinnerIndex+1:lateNightIndex]
    lateNightArray_merrill=end_array[lateNightIndex+1:-9]




    #porter
    end_array=[]
    breakfastIndex=-1
    lunchIndex=-1
    dinnerIndex=-1
    lateNightIndex=-1

    html = urllib.request.urlopen(porter)
    soup = BeautifulSoup(html, "html.parser")
    data = soup.findAll(text=True)
    result = filter(visible, data)
    raw_code = list(result)
    length = len(raw_code)

    breakfastArray_porter=[]
    lunchArray_porter=[]
    dinnerArray_porter=[]
    lateNightArray_porter=[]

    wordbank=["\n","Recipe Name Is Displayed Here","Nutrition Info","\xa0"]

    for x in raw_code:
        for y in wordbank:
            if y in x:
                break
        else:
            end_array.append(x)
    for x in end_array:
        if "Breakfast" in x:
            breakfastIndex=end_array.index(x)
        elif "Lunch" in x:
            lunchIndex=end_array.index(x)
        elif "Dinner" in x:
            dinnerIndex=end_array.index(x)
        elif "Late Night" in x:
            lateNightIndex=end_array.index(x)


    breakfastArray_porter=end_array[breakfastIndex:lunchIndex]
    lunchArray_porter=end_array[lunchIndex+1:dinnerIndex]
    dinnerArray_porter=end_array[dinnerIndex+1:lateNightIndex]
    lateNightArray_porter=end_array[lateNightIndex+1:-9]


    #rcc
    end_array=[]
    breakfastIndex=-1
    lunchIndex=-1
    dinnerIndex=-1
    lateNightIndex=-1

    html = urllib.request.urlopen(rcc)
    soup = BeautifulSoup(html, "html.parser")
    data = soup.findAll(text=True)
    result = filter(visible, data)
    raw_code = list(result)
    length = len(raw_code)

    breakfastArray_rcc=[]
    lunchArray_rcc=[]
    dinnerArray_rcc=[]
    lateNightArray_rcc=[]

    wordbank=["\n","Recipe Name Is Displayed Here","Nutrition Info","\xa0"]

    for x in raw_code:
        for y in wordbank:
            if y in x:
                break
        else:
            end_array.append(x)
    for x in end_array:
        if "Breakfast" in x:
            breakfastIndex=end_array.index(x)
        elif "Lunch" in x:
            lunchIndex=end_array.index(x)
        elif "Dinner" in x:
            dinnerIndex=end_array.index(x)
        elif "Late Night" in x:
            lateNightIndex=end_array.index(x)


    breakfastArray_rrc=end_array[breakfastIndex:lunchIndex]
    lunchArray_rrc=end_array[lunchIndex+1:dinnerIndex]
    dinnerArray_rrc=end_array[dinnerIndex+1:lateNightIndex]
    lateNightArray_rrc=end_array[lateNightIndex+1:-9]







    breakfastArray
    lunchArray
    dinnerArray
    lateNightArray

    found = 'Found in '
    array = [cowell,ten,merill,porter,rcc]
    page = requests.get(cowell[0])
    foundFlag = False
    for college in array:

        if message_body in breakfastArray_cowell:
            message = ("Cowell for breakfast,\n")
            found = found + message
            foundFlag = True
        if message_body in breakfastArray_ten:
            message = ("College Ten for breakfast,\n")
            found = found + message
            foundFlag = True
        if message_body in breakfastArray_merrill:
            message = ("Merill for breakfast,\n")
            found = found + message
            foundFlag = True
        if message_body in breakfastArray_porter:
            message = ("Porter for breakfast,\n")
            found = found + message
            foundFlag = True
        if message_body in breakfastArray_rcc:
            message = ("Rachel Carson College for breakfast,\n")
            found = found + message
            foundFlag = True

        if message_body in lunchArray_cowell:
            message = ("Cowell for lunch,\n")
            found = found + message
            foundFlag = True
        if message_body in lunchArray_ten:
            message = ("College Ten for lunch,\n")
            found = found + message
            foundFlag = True
        if message_body in lunchArray_merrill:
            message = ("Merill for lunch,\n")
            found = found + message
            foundFlag = True
        if message_body in lunchArray_porter:
            message = ("Porter for lunch,\n")
            found = found + message
            foundFlag = True
        if message_body in lunchArray_rcc:
            message = ("Rachel Carson College for lunch,\n")
            found = found + message
            foundFlag = True


        if message_body in dinnerArray_cowell:
            message = ("Cowell for dinner,\n")
            found = found + message
            foundFlag = True
        if message_body in dinnerArray_ten:
            message = ("College Ten for dinner,\n")
            found = found + message
            foundFlag = True
        if message_body in dinnerArray_merrill:
            message = ("Merill for dinner,\n")
            found = found + message
            foundFlag = True
        if message_body in dinnerArray_porter:
            message = ("Porter for dinner,\n")
            found = found + message
            foundFlag = True
        if message_body in dinnerArray_rcc:
            message = ("Rachel Carson College for dinner,\n")
            found = found + message
            foundFlag = True


        if message_body in lateNightArray_cowell:
            message = ("Cowell for late night,\n")
            found = found + message
            foundFlag = True
        if message_body in lateNightArray_ten:
            message = ("College Ten for late night,\n")
            found = found + message
            foundFlag = True
        if message_body in lateNightArray_merrill:
            message = ("Merill for late night,\n")
            found = found + message
            foundFlag = True
        if message_body in lateNightArray_porter:
            message = ("Porter for late night,\n")
            found = found + message
            foundFlag = True
        if message_body in lateNightArray_rcc:
            message = ("Rachel Carson College for late night,\n")
            found = found + message
            foundFlag = True


    if foundFlag == False:
        found = "Item not found."

    resp = MessagingResponse()
    resp.message(found)
    return str(resp)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

if __name__ == "__main__":
    app.run(debug=True)
