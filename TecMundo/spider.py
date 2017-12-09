# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from item import New
import json

class TecMundoSpider(Spider):
    name = 'tecmundo'
    allowed_domains = ['www.tecmundo.com.br']
    limit = 1
    counter = 0
    protocol = 'https'

    def start_requests(self):
        top = getattr(self, 'top', '20')
        page = getattr(self, 'page', '1')
        limit = getattr(self, 'limit', 1)
        self.limit = int(limit) if int(limit) > 0 else 1

        url = 'https://www.tecmundo.com.br/api/v2/news/latest-news/noticias?top=' + top + '&noHighlights=False&idReference=0&older=True&os=&page=' + page

        yield Request(url, self.item_parse)

    def item_parse(self, response):
        data = json.loads(response.text)

        for new in data['data']:
            nw = New()
            nw['image'] = new['Image']
            nw['author'] = new['NomeAutor']
            nw['title'] = new['Title']
            nw['summary'] = new['Chamada']
            nw['date'] = new['DateISO']
            nw['tag'] = new['Tag']['Title']
            nw['url'] = new['Social']['Url']

            yield nw

        self.counter += 1

        if self.counter < self.limit:
            next_page = data['next']
            if next_page != "":
                yield Request(self.protocol + '://' + self.allowed_domains[0] + next_page, callback=self.item_parse)
