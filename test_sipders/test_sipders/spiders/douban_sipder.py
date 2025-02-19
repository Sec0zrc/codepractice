import scrapy


class DoubanSipderSpider(scrapy.Spider):
    name = "douban_sipder"
    allowed_domains = ["movie.douban.com"]
    #豆瓣排行榜
    start_urls = ["https://movie.douban.com"]


    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Referer': 'https://movie.douban.com/',
        }
        for url in self.start_urls:
            yield scrapy.Request(url,headers=headers,callback=self.parse)

        


    def parse(self, response):
        print("================start scrapy ====================")
        #print(response.text)
        for movie in response.css('div.item'):
            print(movie)
            yield{
                'title': movie.css('item.p::text').get(),
                'rating': movie.css('item.rating_num::text').get(),
                'quote': movie.css('item.inq::text').get(),
            }

        #处理分页
        next_page = response.css('span.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        pass
