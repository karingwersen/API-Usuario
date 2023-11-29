FROM mongo:nanoserver-1809

EXPOSE 27017

CMD ["mongod", "--bind_ip_all"]