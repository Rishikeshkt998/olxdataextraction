import scrapy
# from urllib.parse import urljoin

class olxspider(scrapy.Spider):
    name ='olx'
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

    def parse(self,response):
        
        for products in response.css("li._1DNjI"):
            try:
                yield{
                    'link':products.css("li._1DNjI a").xpath("@href").extract()
                }
            except:
                yield{
                    'link': 'sold out',
                }
        # for p in products:
        #     url=urljoin(response.url,p)
        #     yield scrapy.request(url,callback=self.parse_product)

        # next_page = response.css('button.rui-39-wj.rui-3evoE.rui-1JPTg')
        # if next_page is not None:
        #     yield response.follow(next_page,callback=self.parse)
        
