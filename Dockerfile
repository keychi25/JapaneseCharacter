FROM python:3.7


RUN pip install pipenv

RUN mkdir /hiragana
WORKDIR /hiragana

ADD Pipfile /hiragana/Pipfile
ADD Pipfile.lock /hiragana/Pipfile.lock
RUN pipenv install --system

ADD . /hiragana
