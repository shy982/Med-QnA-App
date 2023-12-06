FROM python:3.8-slim

WORKDIR /usr/src/app

COPY ./backend /usr/src/app

RUN pip install --no-cache-dir -r ./requirements.txt

COPY . ./

EXPOSE 5000

CMD ["python", "./marshaler/chat_io_service.py"]