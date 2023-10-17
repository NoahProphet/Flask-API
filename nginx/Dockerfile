FROM nginx:1.23-alpine

RUN rm /etc/nginx/nginx.conf
COPY config /etc/nginx/nginx.conf

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx /etc/nginx/conf.d/default.conf
EXPOSE 80
