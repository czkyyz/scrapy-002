# -*- coding: utf-8 -*-
import scrapy


class CoursesSpider(scrapy.Spider):
    name = 'courses'

    def start_urls(self):
        url1 = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url1.format(i) for i in range(1,5))

    def parse(self, response):
        for i in response.css('li.col-12'):

            item = CourseItem({

                "name": i.css('a::text').re_first('\s*(\w*)'),

                "update_time":i.css('relative-time::attr(datetime)').extract_first()
                                                                                    
                })
            yield item
