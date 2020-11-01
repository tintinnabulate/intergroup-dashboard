# -*- coding: utf-8 -*-
import scrapy
import os
import pandas as pd
from bs4 import BeautifulSoup
import re
import csv
#from scraper.items import ScraperItem # Model
from scrapy import Spider
from scrapy.http import FormRequest,Request
from scrapy.utils.response import open_in_browser
import datetime


zoom_pattern = r"https://[\w+?\.]*zoom\.us/j/.+?[\?pwd=\w+?]+\b"
ZOOM_RE = re.compile(zoom_pattern, re.IGNORECASE | re.MULTILINE)


intergroups = {11: "Wiltshire",}

class AlcoholicsAnonymousSpider(scrapy.Spider):
    name = 'alcoholics-anonymous'
    intergroup_urls = {x[0]:f'https://www.alcoholics-anonymous.org.uk/markers.do?ig={x[0]}'  for x  in intergroups.items()}

    def start_requests(self):
        for intergroup_id,url in self.intergroup_urls.items():
            yield Request(url,callback=self.parse,meta={'intergroup_id':intergroup_id})

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser') 
        meetings=soup.find_all('marker')
        for meeting in meetings:
      
            marker_address = meeting.get('address')
            marker_code = meeting.get('code')
            marker_title = meeting.get('title')
            marker_day = meeting.get('day')
            hearing = meeting.get('hearing')
            marker_lat = meeting.get('lat') or None
            marker_lng = meeting.get('lng') or None
            marker_postcode = meeting.get('postcode')
            slat = meeting.get('slat')
            slng = meeting.get('slng')
            marker_time = meeting.get('time')
            marker_wheelchair = meeting.get('wheelchair')
            marker_hearing = meeting.get('hearing')
            marker_time = marker_time.replace(".",":")
            marker_url = response.url
            marker_open_again = meeting.get('oa')
            covid_open_status = False
            if marker_open_again == 'True':
                covid_open_status = True
                
            hour = int(marker_time[:2])
            minute = int(marker_time[3:5]) 
            meeting_time = datetime.time(hour,minute)
            
            meeting_data = {'code':marker_code,'day':marker_day,'hearing':marker_hearing,'lat':marker_lat,'lng':marker_lng,'postcode':marker_postcode,'time':meeting_time,\
               'duration':'','title':marker_title,'wheelchair':marker_wheelchair,'intergroup': intergroups[self.request.meta['intergroup_id']],'covid_open_status':covid_open_status}
          

            url = f'https://www.alcoholics-anonymous.org.uk/detail.do?id={marker_code}'
            
            yield Request(url=url,callback=self.get_meeting_detail,meta={'meeting_data':meeting_data})

    
    def get_meeting_detail(self,response):
        meeting_data = response.meta.get('meeting_data')

        data = response.text
        soup = BeautifulSoup(data, features="lxml")
        dpanel = soup.find('div',{"class": "dpanel"})
        table = soup.find('div',{"class": "dpanel"}).find_parent("table")
        header = soup.find('div',{"class": "dpanel"}).findChild("h3")
        detail_url = response.url
        
                   
        lines =  [line for line in dpanel.strings] 

        detail = "\n".join(lines[3:])
        meeting_data['detail'] = detail

        matches = ZOOM_RE.findall(detail)
        meeting_data['conference_url'] = None
        if matches:
            meeting_data['conference_url'] = matches[0]

        item = meeting_data
        yield item
