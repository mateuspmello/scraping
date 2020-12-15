FROM python

COPY first.py .

RUN apt update && apt-get install -y python-bs4

RUN pip3 install beautifulsoup4

RUN pip3 install lxml

RUN python3 first.py

ENTRYPOINT [ "python", "first.py" ]

