import scrapy
from urllib.parse import urljoin
import json

class olxspider(scrapy.Spider):
    name ='olx'
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']
    
    
    
    def parse(self,response):
        urls= response.css("li._1DNjI a").xpath("@href").extract()
        for url in urls:
            url=response.urljoin(url)
            yield scrapy.Request(url=url,callback=self.parse_details)
    def parse_details(self,response):
        
        yield{
            'property_name':response.xpath("//h1[@class='_1hJph']/text()").extract(),
            'property_id':response.xpath("//div[contains(@class, '_1-oS0')]/strong/text()").extract()[2],
            'breadcrumbs':response.xpath('//ol[@class="rui-10Yqz"]/li/a/text()').extract(),
            'price':{
                'amount':response.xpath("//span[@class='T8y-z']/text()").extract()[0][2:],
                'currency':response.xpath("//span[@class='T8y-z']/text()").extract()[0][0]
            },
            'image_url':response.xpath("//div[@class='_23Jeb']/figure/img/@src").extract_first(),
            'description':response.xpath("//div[@data-aut-id='itemDescriptionContent']/p/text()").extract(),
            'seller_name':response.css('div.eHFQs::text').extract(),
            'location':response.css('span._1RkZP::text').extract(),
            'property_type':response.xpath("//span[@class='B6X7c']/text()").extract()[0],
            'bathrooms':response.xpath("//span[@class='B6X7c']/text()").extract()[2],
            'bedrooms':response.xpath("//span[@class='B6X7c']/text()").extract()[1],


        }
    
        


