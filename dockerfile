FROM nginx:alpine

COPY hello-world.html /usr/share/nginx/html/hello-world.html

EXPOSE 80