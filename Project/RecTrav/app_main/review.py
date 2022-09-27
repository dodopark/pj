import requests
import re 

def GetReviews(url):
    req = requests.get(url)
    str_reviews_summary = re.findall(r'"//lh3.goog?.*?].*?]', req.text)
    reviews = []
    for i in range(len(str_reviews_summary)):
        text = str_reviews_summary[i]
        text = text.split(',')
        rev = text[2]
        rev = re.sub(r'\\', '', rev)
        rev = re.sub(r'""', '', rev) 
        reviews.append(rev)
        print(rev)
    return reviews



url = 'https://www.google.com/maps?cid=13109049706329246808&hl=th'
re = GetReviews(url)  
print(re[0])  