from scrapy.cmdline import execute

def run():
    execute(["scrapy", "crawl", "stock", "-o", "items.json"])



if __name__ == "__main__":
    run()
