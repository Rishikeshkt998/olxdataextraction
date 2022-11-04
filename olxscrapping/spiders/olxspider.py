import scrapy

class olxspider(scrapy.Spider):
    name ='olx'
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

    def parse(self,response):
        for product in response.css("li._1DNjI"):
            yield{
                'name': product.css("span.YBbhy::text").get(),
                'price':product.css("span._2Ks63::text").get().replace('₹',''),
            }