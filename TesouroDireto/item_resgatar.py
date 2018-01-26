# -*- coding: utf-8 -*-
from scrapy import Item, Field

class TituloResgatar(Item):
    titulo = Field()
    categoria = Field()
    vencimento = Field()
    taxa_rendimento = Field()
    preco_unitario = Field()
    atualizacao = Field()