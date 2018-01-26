# -*- coding: utf-8 -*-
from scrapy import Item, Field

class TituloInvestir(Item):
    titulo = Field()
    categoria = Field()
    vencimento = Field()
    taxa_rendimento = Field()
    valor_minimo = Field()
    preco_unitario = Field()
    atualizacao = Field()