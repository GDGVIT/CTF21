FROM python:3.8-alpine
ADD app /app
ADD flag /flag
WORKDIR /app
RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev 
RUN pip install --no-cache-dir flask
EXPOSE 5000/tcp
CMD [ "python3" ,"-m","flask","run","--host=0.0.0.0"]
