#!/bin/bash
export http_proxy='127.0.0.1:8118'
> Links.txt
scrapy crawl Get -o Links.txt -t csv
