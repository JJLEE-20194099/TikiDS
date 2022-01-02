import requests
import json
import csv
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from src.crawler_by_call_api.exception_utils import get_text, get_href, get_value_by_idx_list, get_a_children_by_find, get_a_children_by_find_class, get_childrens_by_find, get_childrens_by_find_class, get_len

def get_header():
    headers = dict()
    headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    headers['Accept-Encoding'] = 'gzip, deflate, sdch'
    headers['Accept-Language'] = 'en-US,en;q=0.8,vi;q=0.6'
    headers['Connection'] = 'keep-alive'
    headers['Upgrade-Insecure-Requests'] = '1'
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    return headers

# Số trang cần lấy với từng category
def crawl_item_ids(id_list_by_category_api):
    item_ids = []
    pages = 22
    for i in range(pages):
        payload = {}
        params = {
            'page': i + 1
        }
        
        response = requests.request("GET", id_list_by_category_api, headers=get_header(), data=payload, params=params)
        if response.status_code == 200: 
            response_json = response.json()
            if "data" in response_json:
                for item in response_json["data"]:
                    item_ids.append([get_value_by_idx_list(item, 'id')])
            i = i + 1
        else:
            break
       
    return item_ids

# Những item mình cần crawl về
def crawl_item_detail_by_id(detail_by_item_id_api, item_id):
    name = -1
    category = -1
    brand = -1
    price = -1
    discount = -1
    discount_rate = -1
    mota = -1
    image_url = -1
    n_sold = -1
    rank = -1

    item_detail = [item_id[0], name, price, category, brand, discount, discount_rate, image_url, mota, n_sold, rank]
    item_detail_util = [item_id[0], name, price, category, brand, discount, discount_rate, image_url, mota, n_sold, rank]
    payload = {}
    try:
        response = requests.get(detail_by_item_id_api.format(item_id[0]), headers=get_header(), data=payload)
    except Exception:
        return item_detail
    try:
        response_json = response.json()
    except Exception:
        return item_detail    
    
    try:
        if response.status_code == 200:
            name = get_value_by_idx_list(response_json, 'name')
            price = get_value_by_idx_list(response_json, 'price')
            category = get_value_by_idx_list(response_json, 'productset_group_name')
            discount = get_value_by_idx_list(response_json, 'discount')
            discount_rate = get_value_by_idx_list(response_json, 'discount_rate')
            image_url = get_value_by_idx_list(response_json, 'thumbnail_url')
            try:
                mota = get_text(BeautifulSoup(get_value_by_idx_list(response_json, 'description'), 'html.parser'))
            except Exception:
                mota = -1
            
            brand_dict = get_value_by_idx_list(response_json, 'brand')
            brand = get_value_by_idx_list(brand_dict, 'name')
            sold_dict = get_value_by_idx_list(response_json, 'quantity_sold')
            n_sold =  get_value_by_idx_list(sold_dict, 'value')
            rank = get_value_by_idx_list(get_value_by_idx_list(get_value_by_idx_list(response_json, 'ranks'), 0), 'rank')
                            
                        
            item_detail = [item_id[0], name, category, brand, price, discount, discount_rate, mota, image_url, n_sold, rank]
            return item_detail
    except Exception:
        return item_detail_util
        

# Thông tin tổng quan về rating
def crawl_overall_rating_by_id(detail_by_item_id_api, item_id):
    id = item_id[0]
    avg_rating = -1
    n_reviews = -1
    n_rate_5 = -1
    n_rate_4 = -1
    n_rate_3 = -1
    n_rate_2 = -1
    n_rate_1 = -1
    rate_with_img = -1

    payload = {}
    item_overrall = [item_id[0], avg_rating, n_reviews, n_rate_5, n_rate_4, n_rate_3, n_rate_2, n_rate_1, rate_with_img]
    item_overrall_util = [item_id[0], avg_rating, n_reviews, n_rate_5, n_rate_4, n_rate_3, n_rate_2, n_rate_1, rate_with_img]
    try:
        response = requests.get(detail_by_item_id_api.format(item_id[0]), headers=get_header(), data=payload)
        response_json = response.json()
        cnt = 0
        if response.status_code == 200:
        
            avg_rating = get_value_by_idx_list(response_json, 'rating_average')
            n_reviews = get_value_by_idx_list(response_json, 'reviews_count')

            n_rate_5 = get_value_by_idx_list(get_value_by_idx_list(get_value_by_idx_list(response_json, 'stars'), "5"), "count")
            n_rate_4 = get_value_by_idx_list(get_value_by_idx_list(get_value_by_idx_list(response_json, 'stars'), "4"), "count")
            n_rate_3 = get_value_by_idx_list(get_value_by_idx_list(get_value_by_idx_list(response_json, 'stars'), "3"), "count")
            n_rate_2 = get_value_by_idx_list(get_value_by_idx_list(get_value_by_idx_list(response_json, 'stars'), "2"), "count")
            n_rate_1 = get_value_by_idx_list(get_value_by_idx_list(get_value_by_idx_list(response_json, 'stars'), "1"), "count")
            
            
            ratings = get_value_by_idx_list(response_json, "data")
            if ratings:
                for rating in ratings:
                    try:
                        if len(get_value_by_idx_list(rating, "images")) > 0:
                            cnt += 1
                    except Exception:
                        continue
                rate_with_img = cnt
                        
            item_overrall = [item_id[0], avg_rating, n_reviews, n_rate_5, n_rate_4, n_rate_3, n_rate_2, n_rate_1, rate_with_img]
        return item_overrall
    except Exception:
        return item_overrall_util



def crawl_rating_list_by_item_id(rating_list_api, id):
    user_id = -1
    item_id = -1
    rating = -1
    timestamp = -1
    comment = -1
    payload = {}
    response = requests.get(rating_list_api.format(id), headers=get_header(), data=payload)
    response_json = response.json()
    rating_list = []
    
    if response.status_code == 200:
        if 'data' in response_json:    
            try:
                for review in response_json['data']:
                    try:
                        user_id = get_value_by_idx_list(review, 'customer_id')
                        item_id = id
                        rating = get_value_by_idx_list(review, 'rating')
                        timestamp = get_value_by_idx_list(review, 'created_at')
                        comment = get_value_by_idx_list(review, 'content')
                        rating = [user_id, item_id, rating, timestamp, comment]
                        rating_list.append(rating)

                        user_id = -1
                        item_id = -1
                        rating = -1
                        timestamp = -1
                        comment = -1
                    except Exception:
                        continue
            except Exception:
                return rating_list

    
    return rating_list

