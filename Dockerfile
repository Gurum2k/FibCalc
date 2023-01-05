# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster
ADD main.py .
CMD [ "python3", "./main.py"]