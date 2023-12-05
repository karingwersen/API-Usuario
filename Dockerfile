FROM mongo:7.0.4

RUN apt update && apt install -y python3.11 && apt install -y python3-pip && mkdir /app && mkdir /app/api

COPY api /app/api

COPY requirements.txt /app/requirements.txt

COPY container-startup-script.sh /app/container-startup-script.sh

WORKDIR /app

RUN python3.11 -m pip install -r requirements.txt && chmod +x /app/container-startup-script.sh

WORKDIR /app

EXPOSE 5000

CMD [ "/app/container-startup-script.sh" ]