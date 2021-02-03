FROM python:3.9.1-buster
RUN mkdir /twitter
WORKDIR /twitter
COPY . /twitter
RUN pip3 install flask
RUN pip install mysql-connector-python
RUN pip3 install datetime
CMD ['python','main.py']