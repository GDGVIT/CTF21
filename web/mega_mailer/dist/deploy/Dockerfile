FROM python:3.8-alpine
ADD app /app
ADD flag /app/
WORKDIR /app
RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev 
RUN pip install --no-cache-dir flask
RUN chmod -R 755 .
RUN adduser --disabled-password user
USER user
EXPOSE 5000/tcp
CMD [ "python3" ,"-m","flask","run","--host=0.0.0.0"]
