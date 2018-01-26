# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from item_investir import TituloInvestir
from item_resgatar import TituloResgatar

class TesouroDireto(Spider):
    name = 'tesourodireto'
    allowed_domains = ['www.tesouro.fazenda.gov.br']
    
    def start_requests(self):
        url = 'http://www.tesouro.fazenda.gov.br/tesouro-direto-precos-e-taxas-dos-titulos'
        yield Request(url, self.item_parse)

    def item_parse(self, response):
        linhas = response.xpath("//table[contains(@class, 'tabelaPrecoseTaxas') and not(contains(@class, 'sanfonado'))]/tbody/tr[contains(@class, 'camposTesouroDireto')]")
        atualizacao = response.xpath("//*[@id='p_p_id_precosetaxas_WAR_tesourodiretoportlet_']/div/div/div/b//text()").extract()
        
        for linha in linhas:
            dados_linha = linha.xpath('.//text()').extract()
            titulo = TituloInvestir()
            titulo['titulo'] = dados_linha[1]
            titulo['categoria'] = 'investir'
            titulo['vencimento'] = dados_linha[3]
            titulo['taxa_rendimento'] = dados_linha[5]
            titulo['valor_minimo'] = dados_linha[7].replace('R$', '')
            titulo['preco_unitario'] = dados_linha[9].replace('R$', '')
            titulo['atualizacao'] = atualizacao
            
            yield titulo
            
        linhas = response.xpath("//table[contains(@class, 'tabelaPrecoseTaxas') and contains(@class, 'sanfonado')]/tbody/tr[contains(@class, 'camposTesouroDireto')]")
            
        for linha in linhas:
            dados_linha = linha.xpath('.//text()').extract()
            titulo = TituloResgatar()
            titulo['titulo'] = dados_linha[1]
            titulo['categoria'] = 'resgatar'
            titulo['vencimento'] = dados_linha[3]
            titulo['taxa_rendimento'] = dados_linha[5]
            titulo['preco_unitario'] = dados_linha[7].replace('R$', '')
            titulo['atualizacao'] = atualizacao
            
            yield titulo            