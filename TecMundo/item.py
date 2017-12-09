# -*- coding: utf-8 -*-
from scrapy import Item, Field

class New(Item):
    image = Field()
    author = Field()
    title = Field()
    summary = Field()
    date = Field()
    tag = Field()
    url = Field()

