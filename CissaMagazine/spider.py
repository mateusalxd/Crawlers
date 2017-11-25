# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from item import Product

protocol = 'https'

def clean_up(text):
    return ''.join(text.split('\n')).strip() if text is not None else ''

def fix_quantity(quantity):
    return quantity.replace('(', '').replace(')', '')

def fix_url(url):
    return protocol + ':' + url if url is not None else ''

class CissaMagazineSpider(Spider):
    name = 'cissamagazine'
    allowed_domains = ['www.cissamagazine.com.br']

    def start_requests(self):
        url = 'https://www.cissamagazine.com.br/'
        brand = getattr(self, 'brand', None)
        category = getattr(self, 'category', None)
        search = getattr(self, 'search', None)
        start = getattr(self, 'start', None)

        if search is not None:
            url = url + 'busca?q=' + search
            if brand is not None:
                url = url + '&marca=' + brand
            if category is not None:
                url = url + '&categoria=' + category
            if start is not None:
                url = url + '&p=' + start

        yield Request(url, self.item_parse)

    def item_parse(self, response):
        products = response.xpath('//div[contains(@class, "pesquisa-produtos")]//ul[@class = "product-list clearfix product-list-loading-images"]')
        for product in products.xpath('.//li'):
            pdt = Product()
            pdt['id'] = product.xpath('.//meta[@itemprop = "productId"]/@content').extract_first()
            pdt['url_image'] = product.xpath('.//figure/img/@src').extract_first()
            pdt['url_product'] = fix_url(product.xpath('.//a[@itemprop = "url"]/@href').extract_first())
            pdt['name'] = clean_up(product.xpath('.//span[@class = "product-name"]/text()').extract_first())
            pdt['brand'] = product.xpath('.//div[@itemprop = "brand"]/meta/@content').extract_first()
            pdt['rating'] = product.xpath('.//span[@class = "rating"]/span[@class = "star-back big"]/@title').extract_first()
            pdt['rating_quantity'] = fix_quantity(clean_up(product.xpath('.//span[@class = "rating"]/span[@class = "qtd-aval"]/text()').extract_first()))
            pdt['availability'] = product.xpath('.//div[@itemprop = "offers"]/meta[@itemprop = "availability"]/@content').extract_first()
            pdt['price'] = product.xpath('.//div[@itemprop = "offers"]/meta[@itemprop = "price"]/@content').extract_first()
            pdt['price_currency'] = product.xpath('.//div[@itemprop = "offers"]/meta[@itemprop = "priceCurrency"]/@content').extract_first()
            pdt['type_payment'] = clean_up(product.xpath('.//div[@itemprop = "offers"]//span[@class = "type-payment-condiction"]/text()').extract_first())
            pdt['extra'] = product.xpath('./@data-variant').extract_first()
            yield pdt

        last_button = response.xpath('//div[@class = "pesquisa-paginacao"]//ul/li[last()]')
        is_next_button = bool(last_button.xpath('./@class = "nav"'))
        next_page = last_button.xpath('./a/@href').extract_first()

        if is_next_button and next_page is not None:
            yield Request(protocol + ':' + next_page, callback=self.item_parse)
