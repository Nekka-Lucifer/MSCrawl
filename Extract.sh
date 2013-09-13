#!/bin/bash
export http_proxy='127.0.0.1:8118'
> Addresses.csv
scrapy crawl Extract -o Addresses.csv -t csv
