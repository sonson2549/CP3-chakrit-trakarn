
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from tkinter.ttk import Notebook
from tkinter import *
from tkinter import ttk


def goldsell():
    url = 'https://www.goldtraders.or.th/'
    webopen = req(url)
    page_html = webopen.read()
    webopen.close()
    page_soup = soup(page_html, "html.parser")
    data = page_soup.findAll(id='DetailPlace_uc_goldprices1_lblBLSell')
    sell = data[0].text
    selltext.set(sell)


def goldbuy():
    url = 'https://www.goldtraders.or.th/'
    webopen = req(url)
    page_html = webopen.read()
    webopen.close()
    page_soup = soup(page_html, "html.parser")
    data = page_soup.findAll(id="DetailPlace_uc_goldprices1_lblBLBuy")
    buy = data[0].text
    buytext.set(buy)


def timeupdate():
    url = 'https://www.goldtraders.or.th/'
    webopen = req(url)
    page_html = webopen.read()
    webopen.close()
    page_soup = soup(page_html, "html.parser")
    data = page_soup.findAll(id="DetailPlace_uc_goldprices1_lblAsTime")
    time = data[0].text
    timetext.set(time)


GUI = Tk()
GUI.title('son gold shop')
GUI.geometry('700x500')
Tab = Notebook(GUI)

F1 = Canvas(Tab, width=1800, height=1560)


F1.configure(background='firebrick3')
Tab.add(F1, text='gold price')


Tab.pack(fill=BOTH, expand=1)
F1.create_line(0, 70, 1800, 70, fill="white", width=4)
F1.create_line(0, 380, 1800, 380, fill="white",width=4)


selltext = StringVar()
buytext = StringVar()
timetext = StringVar()


L1 = ttk.Label(F1, textvariable=selltext, foreground='yellow2',
                background='firebrick3', font=('Arial Black', 40), command=goldsell())
L1.place(x=350, y=120)
L2 = ttk.Label(F1, textvariable=buytext, foreground='yellow2',
                background='firebrick3', font=('Arial Black', 40), command=goldbuy())
L2.place(x=350, y=230)
L3 = ttk.Label(F1, textvariable=timetext, foreground='yellow2',
                background='firebrick3', font=('Arial Black', 22), command=timeupdate())
L3.place(x=140, y=410)
L4 = ttk.Label(F1, text='รับซื้อ', foreground='white',
                background='firebrick3', font=('Arial Black', 22))
L4.place(x=250, y=253)
L5 = ttk.Label(F1, text='ขายออก', foreground='white',
                background='firebrick3', font=('Arial Black', 22))
L5.place(x=230, y=140)
L6 = ttk.Label(F1, text='อัพเดตเมื่อ', foreground='black',
                background='firebrick3', font=('Arial Black', 18))
L6.place(x=20, y=415)
L7 = ttk.Label(F1, text='ร้านทองt9เยาวราช สาขาหนองหาน', foreground='yellow2',
                background='firebrick3', font=('Arial Black', 28))
L7.place(x=90, y=10)


GUI.mainloop()
