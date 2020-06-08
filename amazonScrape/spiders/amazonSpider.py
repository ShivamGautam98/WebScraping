# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
class amazonscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_price1 = scrapy.Field()
    product_imagelink = scrapy.Field()
    pass
class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonSpider'
    start_urls = ['https://www.amazon.in/s?k=sanitizer&ref=nb_sb_noss_2']
    
    def parse(self, response):
        items=amazonscrapeItem()
        product_name=response.css('.a-color-base.a-text-normal::text').extract()
        product_price=response.css('.a-price-whole').css('::text').extract()
        product_imagelink=response.css('.s-image-square-aspect::attr(src)').extract()
        items['product_name']=product_name
        items['product_price']=product_price
        items['product_imagelink']=product_imagelink
        file = open("amazon.txt","w")
        file.writelines(items['product_name'])
        file.writelines(items['product_price'])
        file.writelines(items['product_imagelink'])
        file.close()
        yield items


        
##class AmazonspiderSpider(scrapy.Spider):
##    name = 'amazonSpider'
##    start_urls = ['https://www.flipkart.com/search?q=sanitizer&sid=g9b%2Cema%2Crhm%2Cjrn&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=sanitizer%7CHand+Sanitizer&requestId=06e87ddb-5e0a-43bb-bd5a-b970396b05a4&as-searchtext=sani']
##    
##    
##    def parse(self, response):
##        items=amazonscrapeItem()
##        product_name=response.css('._2cLu-l::text').extract()
##        product_price=response.css('._1Vfi6u ._1vC4OE').css('::text').extract()
##        product_imagelink=response.css('.Zhf2z- ._30XEf0::attr(src)').extract()
##        items['product_name']=product_name
##        items['product_price']=product_price
##        items['product_imagelink']=product_imagelink
##        file = open("flipkart.txt","w")
##        file.writelines(items['product_name'])
##        file.writelines(items['product_price'])
##        file.writelines(items['product_imagelink'])
##        file.close()
##        print(product_name)
##        yield items
        


        
##class AmazonspiderSpider(scrapy.Spider):
##    name = 'amazonSpider'
##    start_urls = ['https://paytmmall.com/shop/search?from=autosuggest&userQuery=sanitiser&autosuggest_index_type=autosuggestions&meta_autosuggest_query=sanitiser&meta_autosuggest_keyword=sanitiser&meta_autosuggest_version=3.0&meta_autosuggest_position=1&meta_autosuggest_query_size=9&meta_autosuggest_fetch_size=3&meta_autosuggest_config_size=10&meta_autosuggest_experiment_name=ctr_suggest&meta_src=ctr_suggest&page=1&latitude=27.2030360000001&longitude=78.0426420000001']
##    
##    def parse(self, response):
##        items=amazonscrapeItem()
##        product_name=response.css('.UGUy::text').extract()
##        product_price=response.css('._1kMS span').css('::text').extract()
##        product_imagelink=response.css('img::attr(src)').extract()
##        items['product_name']=product_name
##        items['product_price']=product_price
##        items['product_imagelink']=product_imagelink
##        file = open("paytmmall.txt","w")
##        file.writelines(items['product_name'])
##        file.writelines(items['product_price'])
##        file.writelines(items['product_imagelink'])
##        file.close()
##        yield items



        
##class AmazonspiderSpider(scrapy.Spider):
##    name = 'amazonSpider'
##    start_urls = ['https://www.1mg.com/categories/coronavirus-prevention/sanitizers-handwash-products-296']
##    def parse(self, response):
##        items=amazonscrapeItem()
##        product_name=response.css('.style__pro-title___2QwJy::text').extract()
##        product_author=response.css('.style__pack-size___2JQG7').css('::text').extract()
##        product_price=response.css('.CardRatingDetail__weight-700___27w9q').css('::text').extract()
##        product_price1=response.css('.style__product-pricing___38PRR div .style__price-tag___cOxYc span , .style__large___ubU44+ span').css('::text').extract()
##        product_imagelink=response.css('.style__product-image___1F9l3::attr(src)').extract()
##        items['product_name']=product_name
##        items['product_price1']=product_price1
##        items['product_price']=product_price
##        items['product_price1']=product_price1
##        items['product_imagelink']=product_imagelink
##        file = open("1mg.txt","w")
##        file.writelines(items['product_name'])
##        file.writelines(items['product_price'])
##        file.writelines(items['product_price1'])
##        file.writelines('items['product_imagelink']')
##        file.close()
##        print(product_name)
##        yield items



        
##class AmazonspiderSpider(scrapy.Spider):
##    name = 'amazonSpider'
##    start_urls = ['https://www.shopclues.com/search?q=Sanitizers&z=0&trend=1']
##
##    def parse(self, response):
##        items=amazonscrapeItem()
##        product_name=response.css('h2::text').extract()
##        product_author=response.css('.p_price').css('::text').extract()
##        product_price=response.css('.p_price').css('::text').extract()
##        product_imagelink=response.css('#product_list img::attr(src)').extract()
##        items['product_name']=product_name
##        items['product_price1']=product_price1
##        items['product_price']=product_price
##        items['product_imagelink']=product_imagelink
##        file = open("ShopClues.txt","w")
##        file.writelines(items['product_name'])
##        file.writelines(items['product_price'])
##        file.writelines(items['product_price1'])
##        file.writelines('items['product_imagelink']')
##        file.close()
##        yield items   





##class AmazonspiderSpider(scrapy.Spider):
##    name = 'amazonSpider'
##    start_urls = ['https://www.gofresh-anupam-enterprises.com/']
##
##    def parse(self, response):
##        items=amazonscrapeItem()
##        product_name=response.css('._2BULo::text').extract()
##        product_price1=response.css('._23IPr').css('::text').extract()
##        product_price=response.css('._23ArP').css('::text').extract()
##        product_imagelink=response.css('._2PNEb , li:nth-child(15) ._23ArP::attr(src)').extract()
##        items['product_name']=product_name
##        items['product_price']=product_price1
##        items['product_price1']=product_price
##        items['product_imagelink']=product_imagelink
##        file = open("ScrapeGoFresh.txt","w")
##        file.writelines(items['product_name'])
##        file.writelines(items['product_price'])
##        file.writelines(items['product_price1'])
##        file.close()
##        yield items
##    
##        
