# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
ADD main.py .
CMD [ "python3", "./main.py"]