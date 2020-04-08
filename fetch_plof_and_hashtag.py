# -*- coding: utf-8 -*-

import json
import re
import csv
import os
import requests
import collections
from typing import Dict
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

requests.packages.urllib3.disable_warnings() 

class PlofileCollecter:
    
    def __init__(self):
        self.file_pass = "plof_img/{}.png"
        self.plofile_data = {'username': "", 'url': "", 'icon_src': "", 'biography': "", 'country': "",
                             'post': 0, 'follow': 0, 'follower': 0, 'hashtag': []}
        self.instagram_plofile_url = "https://www.instagram.com/{}/"
        self.len_can_fetch_post = 12 #インスタの仕様上ログインせずに取得可能な投稿数
        self.num_return_hashtag = 30

    def download_img(self, url, user_name):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            save_file_name = self.file_pass.format(user_name)
            with open(save_file_name, 'wb') as f:
                f.write(r.content)

    def fetch_jsondata_from_username(self, user_name_i):
        url = self.instagram_plofile_url.format(user_name_i)
        self.plofile_data['url'] = url
        response = requests.get(url, verify=False)

        soup = BeautifulSoup(response.content, 'html.parser') # 'lxml'  -> 'html.parser' 
        js = soup.find("script", text=re.compile("window._sharedData")).text
        json_data = json.loads(js[js.find("{"):js.rfind("}")+1]);
        #pprint.pprint(json_data)
        return json_data
    
    def fetch_plofile_data_from_jsondata(self, json_data):
        user_data = json_data['entry_data']['ProfilePage'][0]['graphql']['user']
        timeline_media = user_data['edge_owner_to_timeline_media'][ 'edges']
        self.plofile_data['icon_src'] = user_data['profile_pic_url']
        self.plofile_data['biography'] = user_data['biography']        
        self.plofile_data['country'] = json_data['country_code']
        self.plofile_data['post'] = user_data['edge_owner_to_timeline_media']['count']
        self.plofile_data['follow'] = user_data['edge_follow']['count']
        self.plofile_data['follower'] = user_data['edge_followed_by']['count']
        
        hashtag = []
#         for i in range(min(self.post_num_hashtag, int(self.plofile_data['post']))):
        for i in range(min(int(self.plofile_data['post']), self.len_can_fetch_post)):
            text = timeline_media[i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
            hashtag.append(self.text2hashtag(text))
        self.plofile_data['hashtag'] = self.return_top_hashtag(self.flatten(hashtag))
        
    def text2hashtag(self, text):
        pattern = "\#[^(\ ¥\#¥\n)]*"
        return re.findall(pattern, text)
    
    def flatten(self, nested_list):
        """2重のリストをフラットにする関数"""
        return [e for inner_list in nested_list for e in inner_list]
    
    def return_top_hashtag(self, hashtag_list):
        c = collections.Counter(hashtag_list)
        values, counts = zip(*c.most_common())
        return values[:self.num_return_hashtag]

    def main_loop(self, user_name):
        self.plofile_data['username'] = user_name
        try:
            json_data = self.fetch_jsondata_from_username(user_name)
            self.fetch_plofile_data_from_jsondata(json_data)
            self.download_img(self.plofile_data['icon_src'], user_name)   
            return self.plofile_data
        except:
            return self.plofile_data
            
if __name__ == '__main__':
    pc = PlofileCollecter()
    user_name = "ekkkkkkkkkkkkkkkyu"
    plofile_data = pc.main_loop(user_name)