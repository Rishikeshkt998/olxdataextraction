import scrapy
from urllib.parse import urljoin

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
            'property_name':response.css('h1._1hJph::text').extract(),
            # 'property_id':response.css('div._1-oS0 strong::text').extract(),
            # 'breadcrumbs':response.xpath('//ol/li/text()').extract(),
            'price':response.css('span.T8y-z::text').extract(),
            # 'image_url':response.css("img::attr(src)")[1].extract(),
            # 'description':'null',
            'seller_name':response.css('div.eHFQs::text').extract(),
            'location':response.css('span._1RkZP::text').extract(),
            # 'property_type':response.css('span.B6X7c::text').extract(),
            # 'bathrooms':response.css('span.B6X7c::text')[1].extract(),
            # 'bedrooms':response.css('span.B6X7c::text')[2].extract(),

        }

    #     # next_page = response.css('button.rui-39-wj.rui-3evoE.rui-1JPTg')
    #     # if next_page is not None:
    #     #     yield response.follow(next_page,callback=self.parse)
        # has_next = response.css('.rui-39-wj.rui-3evoE.rui-1JPTg').extract()
        # if has_next:
        #     next_page = response.meta.get('next_page', 1) + 1
        #     url = response.urljoin(response.css('script').re_first("'(\?searchId.*page=)'") + str(next_page))
        #     yield Request(url , meta={'next_page': next_page})
        
