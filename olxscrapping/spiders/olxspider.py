import scrapy

class olxspider(scrapy.Spider):
    name ='olx'
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

    def parse(self,response):
        for products in response.css("li._1DNjI"):
            try:
                yield{
                    'name': products.css('span.YBbhy::text').get(),
                    'price':products.css('span._2Ks63::text').get().replace('₹',''),
                }
            except:
                yield{
                    'name': products.css('span.YBbhy::text').get(),
                    'price':'sold out',

                 
                }
        next_page = response.css('button.rui-39-wj.rui-3evoE.rui-1JPTg')
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
        
