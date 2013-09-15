#!/bin/bash
export http_proxy='localhost:8118'
> Addresses.csv
scrapy crawl Extract -o Addresses.csv -t csv
