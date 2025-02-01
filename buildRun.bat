@echo off
docker build -t python-parser .
docker run --rm -it python-parser
