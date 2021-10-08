from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('–lang= ko')


driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

def get_ss(url, out):
    driver.get(url) 

    sleep(2)

    #the element with longest height on page
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    print(S('Width'), S('Height'))
    driver.set_window_size(S('Width'), min(5000, S('Height')))

    sleep(2)
    driver.save_screenshot(out)
    
if __name__ == '__main__':
    urls = ['https://www.amazon.com/gp/bestsellers/books',
            'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?range=0&kind=0&orderClick=DBA&mallGb=KOR&linkClass=0'
    ]

    for i, url in enumerate(urls):
        print("Getting: " + url)
        get_ss(url, "out_" + str(i) + ".png")

    driver.quit()


