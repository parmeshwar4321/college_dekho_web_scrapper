from bs4 import BeautifulSoup
import requests,json,pprint
def college_dekho():
    link='https://www.collegedekho.com/btech-computer_engineering-colleges-in-india/'
    res=requests.get(link)
    soip=BeautifulSoup(res.text,'html.parser').find('div',class_="row collegeBlock")
    pri=soip.find_all(class_="box")
    li=[]
    for i in pri:
        names=i.find('a').get('title')
        te=i.find(class_="info").find_all('li')[1].text[6:]#####type
        try:
            b=int(i.find(class_="rating-per").find( class_="star-ratings-sprite-rating").get('style')[6:8])##ratings
            rate=(b)//20
        except :
            rate='No Ratings'
        url2='https://www.collegedekho.com'+i.find('a').get('href')    #https://www.collegedekho.com/colleges/iit-delhi
        res2=requests.get(url2)
        soip2=BeautifulSoup(res2.text,'html.parser')
        main=soip2.find(class_="collegeContacts")
        contact=main.find(class_="data").text.split(',')[0].strip()
        mail=main.find(class_="data").find_next(class_="data").text.strip()#Email
        add=main.find(class_="data").find_next(class_="data").find_next(class_="data").find_next(class_="data").text.strip()  ##address
        facil=soip2.find(class_="block facilitiesBlock").find(class_="box").find_all(class_="title")
        facilities=[]
        for i in facil:
            facilities.append(i.string)
        dic={'name':names,'type':te,'rating':rate,'contact':contact,'E_mail':mail,'address':add,'Facilities':facilities}
        f=open('college.json','w')
        json.dump(li,f,indent=4)
        f.close()
        li.append(dic)
    return li
pprint.pprint(college_dekho())