from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import os
import pandas as pd
from lxml import etree
import re
import random

#Prduct name
pdt="neuroscience"
#Number of pages want to scrape
page_no=1
#Excel file name
file_name="neurobook_data"

#type the file type you want you scraped data into
file_type="excel" #excel or csv

driver=webdriver.Chrome()
try:
    for i in range(1,page_no+1):
        print(f"🌀 Preparing Page:{i}/{page_no}...")
        query=f"https://www.amazon.in/s?k={pdt}&page={i}&xpid=kAD_rTWKD3n62&crid=14YJDT70HO7X9&qid=1759825218&sprefix=laptop%2Caps%2C209&ref=sr_pg_2"
        time.sleep(random.uniform(1,3))

        driver.get(query)
    try:
        wait = WebDriverWait(driver,15)
        boxes = wait.until(
            EC.presence_of_all_elements_located(
                ("xpath", "//div[contains(@class, 's-main-slot')]/div[@data-asin]")
            )
        )

        i=1
        for box in boxes:
            d=box.get_attribute("innerHTML")
            os.makedirs("data_book2", exist_ok=True)
            with open(f"data_book2/file0{i}.html","w",encoding="utf=8") as f:
                f.write(d)
            print(f"file0{i}:scraped")
            i+=1
            time.sleep(random.uniform(1,3))
    except Exception as e:
        print(e)

    print(f"Pages Scraped🌀:{page_no}")

    d={'Title':[],'Author':[],'Price':[],'Link':[]}

    def clean_text(text):
        text = text.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
        text = text.replace('â‚¹', 'Rs.') \
                .replace('Â', '') \
                .replace('â€™', "'") \
                .replace('â€œ', '"') \
                .replace('â€�', '"') \
                .replace('â€“', '-') \
                .replace('â€”', '-') \
                .replace('â€¦', '...')
        return text.strip()
    os.makedirs("data_book2", exist_ok=True)
    for file in os.listdir("data_book2"):

        try:
            with open(f"data_book2/{file}") as f:
                doc=f.read()
            soup=BeautifulSoup(doc,"html.parser")
            dom = etree.HTML(str(soup)) 

            t=dom.xpath("//h2/span/text()")
            joined = " ".join(t)
            title= re.sub(r'\s+', ' ', joined).strip()


            text1=soup.find("a",attrs={'class':"a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style"})
            text2=None
            if text1:
                # Extract text properly
                a = text1.get_text()
                author= re.sub(r'\s+', ' ', a).strip()
                if "by " in author:
                    author=author.replace("by ","")
            else:
                text2 = dom.xpath("//div[@class='a-row']//span[@class='a-size-base']/text()")

                # Join list elements into one string first
                if text2:
                    joined = " ".join(text2)
                    author = re.sub(r'\s+', ' ', joined).strip()
                    if author=="by":
                        text3=dom.xpath("//div[@class='a-row']//span[@class='a-size-base']/following-sibling::span[@class='a-price-whole']/text()")
                        joined = " ".join(text3)
                        author = re.sub(r'\s+', ' ', joined).strip()
                    elif text2:
                        joined = " ".join(text2)
                        author = re.sub(r'\s+', ' ', joined).strip()
                        if "by " in author:
                         author=author.replace("by ","")
                    
                else:
                    author="No text"

                
            price2=None
            price1=dom.xpath("//span[@class='a-price']/following-sibling::span[@class='a-offscreen']/text()")
            if price1:
                p1=price1[0]
                j=" ".join(p1)
                clean=re.sub(r'\s+','',j).strip()
            else:
                price2=dom.xpath("//span[@class='a-price-symbol']/following-sibling::span[@class='a-price-whole']/text()")
                if price2:
                    p2=price2[0]
                    j=" ".join(p2)
                    clean=re.sub(r'\s+','',j).strip()

                else:
                   clean="M.R.P:?"


            link1 =dom.xpath("//h2[contains(@class,'a-size-medium')]/parent::a/@href")
            if link1:
                l=f"https://www.amazon.in{link1[0]}"
            else:
                l="No link found"


            title = clean_text(title)
            author = clean_text(author)
            price = clean_text(clean)   

        except Exception as e:
            print(e)

        d['Title'].append(title)
        d['Author'].append(author)
        d['Price'].append(price)
        d['Link'].append(l)

    df=pd.DataFrame(data=d)
    df = df.applymap(lambda x: clean_text(str(x)))

    if file_type.upper()=="EXCEL":
        df.to_excel(f"{file_name}.xlsx",index=False)
    elif file_type.upper()=="CSV":
       df.to_csv(f"{file_name}.csv")
    else:
        df.to_excel(f"{file_name}.xlsx",index=False)
    
except Exception as e:
    print(f"Error:{e}")

finally:
    #closing the driver
    driver.quit()
    print("Browser closed")


    

    
