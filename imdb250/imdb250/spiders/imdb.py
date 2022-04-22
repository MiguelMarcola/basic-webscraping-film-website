from turtle import title
import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        rate = response.css("strong ::text").getall()
        index = 0

        for films in response.css(".titleColumn"):
            yield{
                "titles": films.css(".titleColumn a::text").get(),
                "year": films.css(".secondaryInfo ::text").get()[1:-1],
                "rate": rate[index],
            }
            index += 1
        pass
