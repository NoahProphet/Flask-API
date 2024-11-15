FROM postgres:13-alpine

COPY db.sql /docker-entrypoint-initdb.d/

RUN chmod 755 /docker-entrypoint-initdb.d/db.sql