import scrapy
from urllib.parse import urljoin

class olxspider(scrapy.Spider):
    name ='olx'
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']
    # headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}
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
            'price':response.xpath("//span[@class='T8y-z']/text()").extract(),
            'image_url':response.xpath("//div[@class='_23Jeb']/figure/img/@src").extract_first(),
            'description':response.xpath("//div[@data-aut-id='itemDescriptionContent']/p/text()").extract(),
            'seller_name':response.css('div.eHFQs::text').extract(),
            'location':response.css('span._1RkZP::text').extract(),
            'property_type':response.xpath("//span[@class='B6X7c']/text()").extract()[0],
            'bathrooms':response.xpath("//span[@class='B6X7c']/text()").extract()[2],
            'bedrooms':response.xpath("//span[@class='B6X7c']/text()").extract()[1],


        }
    # def start_requests(self):
    #     for page in range(0,3):
    #       next_page=self.start_urls+str(page)
    #     yield scrapy.Request(url=next_page,headers=self.headers,callback=self.parse)


