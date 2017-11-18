# -*- coding: utf-8 -*-
from scrapy import Item, Field

class Product(Item):
    id = Field()
    url_image = Field()
    url_product = Field()
    name = Field()
    brand = Field()
    rating = Field()
    rating_quantity = Field()
    availability = Field()
    price = Field()
    price_currency = Field()
    type_payment = Field()
    extra = Field()
