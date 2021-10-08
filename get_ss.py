from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from git_issue import create_issue
import datetime


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('–lang=ko-KR')


driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

def get_ss(url, out):
    driver.get(url) 

    sleep(2)

    #the element with longest height on page
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    print(S('Width'), S('Height'))
    driver.set_window_size(S('Width'), S('Height'))

    sleep(2)
    driver.save_screenshot(out)
    
if __name__ == '__main__':
    urls = ['https://www.amazon.com/gp/bestsellers/books',
            'http://www.yes24.com/24/Category/BestSeller',
            'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf'
    ]

    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d")

    body = "" 

    for i, url in enumerate(urls):
        print("Getting: " + url)
        out_file = now_str + "_out_" + str(i) + ".png"
        get_ss(url, out_file)
        body += url +  "\n![" + out_file +"]" + \
                "(https://raw.githubusercontent.com/DeepSE/bestbooks/main/" + \
                out_file + ")\n\n"
    

    create_issue('DeepSE/bestbooks', "Best Books on " + now_str, body)



    driver.quit()


