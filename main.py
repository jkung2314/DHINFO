import re
import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=College+Nine+%26+Ten&sName=&naFlag=')
soup = BeautifulSoup(html, "html.parser")
data = soup.findAll(text=True)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

result = filter(visible, data)

raw_code = list(result)
length = len(raw_code)

end_array=[]
breakfastIndex=-1
lunchIndex=-1
dinnerIndex=-1
lateNightIndex=-1
breakfastArray=[]
lunchArray=[]
dinnerArray=[]
lateNightArray=[]
for x in raw_code:
    if "\n" in x:
        continue
    else:
        if "Recipe Name Is Displayed Here" in x:
            continue
        elif "Nutrition Info" in x:
            continue
        elif "\xa0" in x:
            continue
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


breakfastArray=end_array[breakfastIndex:lunchIndex]
lunchArray=end_array[lunchIndex+1:dinnerIndex]
dinnerArray=end_array[dinnerIndex+1:lateNightIndex]
lateNightArray=end_array[lateNightIndex+1:-9]

print(breakfastArray)
#print(breakfastIndex)
print('\n')
print(lunchArray)
#print(lunchIndex)
print('\n')
print(dinnerArray)
print('\n')
print(lateNightArray)


end_array=end_array[1:-9]


#print(raw_code)
