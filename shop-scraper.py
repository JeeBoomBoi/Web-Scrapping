import requests
from bs4 import BeautifulSoup 
import smtplib 
 
URL = 'Your Link' //Any product link from amazon 
headers = {"User-Agents": 'Your user agent'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = price[2:7] // For Indian rupee representation in online stores, varies from site to site


    print(converted_price)
    print(title.strip())
    
    if(converted_price<x):  //The x here is the price you want a paticular product to be.
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Your Email', 'Your password') 

    subject = 'Downfall of Price'
    body = 'Check amazon link Your link'

    msg = "Subject: {}\n\n{}".format(subject, body)
    
    server.sendmail(
        'Your Email',
        'To Another mail id',
        msg
    )
    print("Hey, Email has been sent")

    server.quit()

check_price()