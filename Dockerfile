FROM python:3.9.1-buster
RUN mkdir /twitter
WORKDIR /twitter
COPY . /twitter
RUN pip3 install -r requirements.txt
CMD ["python", "main.py"]