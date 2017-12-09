## Attributes

- limit - request limit (optional)
- page - initial page (optional)
- top - number of news per page (optional)

## How to use

Search using one attribute:

`scrapy runspider spider.py -a top=10`

Search using two attributes:

`scrapy runspider spider.py -a top=10 -a limit=2`

Export items:

`scrapy runspider spider.py -a top=10 -a limit=2 -t csv -o output.csv`

## References

- [Scrapy 1.4 documentation](https://doc.scrapy.org/en/1.4/)
- [Scrapy pipeline to export csv file in the right format](https://stackoverflow.com/questions/29943075)
