from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import csv

class Crawler:
    def __init__(self, driver):
        self.driver = driver
        
    def get_content_(self, url):

        # get content of a page
        domain = None
        domains = url.split('/')
        if (domains.__len__() >= 3):
            domain = domains[2]
        
        
        headers = dict()
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        headers['Accept-Encoding'] = 'gzip, deflate, sdch'
        headers['Accept-Language'] = 'en-US,en;q=0.8,vi;q=0.6'
        headers['Connection'] = 'keep-alive'
        headers['Host'] = domain
        headers['Referer'] = url
        headers['Upgrade-Insecure-Requests'] = '1'
        headers[
            'User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'

        r = requests.get(url, headers=headers, timeout=10)
        r.encoding = 'utf-8'
        r.close()
        return str(r.text)

    def get_rating_list_per_page(self, reviews):

        # Lay ra danh gia cua moi trang binh luan
        try:
            res = []
            for review in reviews:
                user_container = review.find_elements(By.TAG_NAME, 'div')[0]
                rating_container = user_container.find_element(By.XPATH, './following-sibling::div')
            
                username = user_container.find_element(By.CLASS_NAME, "review-comment__user-name").text
                no_year_participation = user_container.find_element(By.CLASS_NAME, "review-comment__user-date").text
                no_ratings = user_container.find_element(By.CLASS_NAME, "review-comment__user-info").find_element(By.TAG_NAME, "span").text
                comment_title = rating_container.find_element(By.CLASS_NAME, "review-comment__title").text
                comment_content = rating_container.find_element(By.CLASS_NAME, "review-comment__content").text
                rating = {
                    "username": username,
                    "Number of years of participation": no_year_participation,
                    "Number of ratings": no_ratings,
                    "comment": {
                        "comment_title": comment_title,
                        "comment_content": comment_content
                    }
                }
                res.append(rating)
            
            
            return res
        except Exception:
            return None      


    def get_rating_from_item_url(self, url: str, pages=1):
        # Lsy ra tat ca danh gia
        rating_list = []
        try:
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 2500)")
            sleep(3)
            reviews = self.driver.find_elements(By.CLASS_NAME, "review-comment")
            for page in range(0, pages, 1):      
                active_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn.active")
                
                box_btn = active_btn.find_element(By.XPATH, "./..")
                box_next_btn = box_btn.find_element(By.XPATH, "./following-sibling::li")
               
                next_btn = box_next_btn.find_element(By.TAG_NAME, "a")
                
                rating_list_per_page = self.get_rating_list_per_page(reviews)
                rating_list = rating_list + rating_list_per_page
                if (page == pages - 1):
                    break
                if (next_btn == None):
                    break
                next_btn.click()
                sleep(1)
                reviews = self.driver.find_elements(By.CLASS_NAME, "review-comment")
            return rating_list    
        except Exception:
            return None
            



    def get_content_item_from_item_url(self, url: str):
        self.driver.get(url)
        try:
            raw_content = self.get_content_(url)
            soup = BeautifulSoup(raw_content, 'html.parser')

            header = soup.find("div", class_="header")
            brand_detail = header.select_one('a[data-view-id="pdp_details_view_brand"]').text
            title_detail = header.find("h1", class_="title").text
            bestseller_detail = header.select_one('a[data-view-id="pdp_details_view_bestseller"]').text
            no_feedbacks = header.find("a", class_="number").text
            no_orders = header.select_one('div[data-view-id="pdp_quantity_sold"]').text
            price = ""
            try:
                price = self.driver.find_element(By.CLASS_NAME, "product-price__current-price").text
            except Exception:
                pass
            try:
                price = self.driver.find_element(By.CLASS_NAME, "flash-sale-price").find_element(By.TAG_NAME, "span").text
            except Exception:
                pass
            try:
                price = self.driver.find_element(By.CLASS_NAME, "list-price").text
            except Exception:
                pass

            try:
                price = self.driver.find_element(By.CLASS_NAME, "product-price__list-price").text
            except Exception:
                pass

           
            # description_box = soup.find("div", class_="content")
            # item_info = description_box.find("ul").find_all("li")
            # description = ""
            
            # for info in item_info:
            #     description += info.text + " "

            description = ""
            
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
            sleep(1)
            rating_total = self.driver.find_element(By.CLASS_NAME, "review-rating__total").text
            sleep(1)
           
            rating_list = self.get_rating_from_item_url(url, 3)
            print(0)

            return {
                "brand": brand_detail,
                "title": title_detail,
                "price": price,
                "bestseller": bestseller_detail,
                "no_feedbacks": no_feedbacks,
                "no_orders": no_orders,
                "description": description,
                "rating_total": rating_total,
                "rating": rating_list
            }
        except Exception:
            return None

    # Lay ra cac category tu trang chu
    def get_categories_from_home_url(self, url): 
        categories = {}
        try:
            next_btn = True
            slider = self.driver.find_element(By.CLASS_NAME, "slider")
            url_boxes = slider.find_elements(By.TAG_NAME, "a")
            while next_btn:
                for u in url_boxes:    
                    name = u.find_element(By.TAG_NAME, "div").text
                    if name != '':
                        categories.update({name: u.get_attribute("href")})
                next_btn = self.driver.find_element(By.CLASS_NAME, "icon-next")
                if next_btn.is_displayed():
                    next_btn.click() 
                else:
                    break
                
            return categories
        except Exception:
            return None


    # get_items_from_category_url()

    def get_page_urls_from_category_url(self, sub_topic_url, pages=1):
        urls = []
        for page in range(pages):
            urls.append(sub_topic_url + f"?page={page + 1}")
        return urls

    def get_all_page_link_per_category(self, url):
        try:
            categories = self.get_categories_from_home_url(url)
            res = {}

            for keys in categories.keys():
                base_sub_topic_url = categories[keys]
                res.update({keys: self.get_page_urls_from_category_url(base_sub_topic_url, 1)})
            return res
           
        except Exception:
            return None

    def get_items_link_per_page(self, url):
        self.driver.get(url)
        try:
            item_links = []
            item_boxes = self.driver.find_elements(By.CLASS_NAME, "product-item")
        
            for item_box in item_boxes:
                item_links.append(item_box.get_attribute("href"))
            return item_links
        except Exception:
            return None

    def raw_dataset(self, url):
        try:
            overview_dataset = self.get_all_page_link_per_category(url)
           
            sleep(3)
            data = {}
            cnt = 0
            for category in overview_dataset.keys():
                links = overview_dataset[category]
                print(links)
                content = []
                for link in links[:1]:
                    item_links_per_page = self.get_items_link_per_page(link)
                    
                    for item_link in item_links_per_page[:3]:
                        detail = self.get_content_item_from_item_url(item_link)
                        content.append(detail)
                data.update({category: content})
                cnt = cnt + 1
                if cnt == 3:
                    break
            
            return data
        except Exception:
            return None


# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# s = Service("D:\Download Default\chromedriver.exe")
# driver = webdriver.Chrome(options=options, service=s)
# driver.maximize_window()
# crawler = Crawler(driver)
# driver.get("https://tiki.vn/cap-hdmi-2-0-ho-tro-3d-4k-dai-1-5m-ugreen-hd118-40409-hang-chinh-hang-p5986499.html?spid=11405146")
# print(crawler.get_content_item_from_item_url("https://tiki.vn/keo-alpenliebe-huong-dau-kem-phien-ban-cau-chuc-tet-2022--goi-16-thoi--p59599652.html?spid=59599653"))









