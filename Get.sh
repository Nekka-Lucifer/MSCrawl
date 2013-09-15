#!/bin/bash
export http_proxy='localhost:8118'
> Links.txt
scrapy crawl Get -o Links.txt -t csv
