# Stage 0, for downloading project’s npm dependencies, building and compiling the app.
FROM node:12-alpine3.11 as build

# set working directory
RUN mkdir /usr/local/app/
WORKDIR /usr/local/app/
COPY news-site/ /usr/local/app/

# install package.json (o sea las dependencies)
RUN npm install
RUN npm run build

# Stage 1, for copying the compiled app from the previous step and making it ready for production with Nginx
FROM nginx:alpine

#copy html files to nginx server
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /usr/local/app/dist/news /usr/share/nginx/html

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
# COPY nginx/nginx.conf /etc/nginx/

# COPY certificates
# COPY nginx/certs/cert.pem /etc/letsencrypt/
# COPY nginx/certs/key.pem /etc/letsencrypt/
# COPY nginx/certs/localhost.crt /etc/letsencrypt/
# COPY nginx/certs/localhost.key /etc/letsencrypt/
COPY nginx/certs/localhost+2-key.pem /etc/letsencrypt/
COPY nginx/certs/localhost+2.pem /etc/letsencrypt/
