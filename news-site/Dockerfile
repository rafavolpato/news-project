# Stage 0, for downloading project’s npm dependencies, building and compiling the app.
FROM node:12-alpine3.11 as build

# set working directory
RUN mkdir /usr/local/app/
WORKDIR /usr/local/app/
COPY ./ /usr/local/app/

# add .bin to $PATH
# ENV PATH /usr/local/app/node_modules/.bin:$PATH

# install package.json (o sea las dependencies)
RUN npm install
RUN npm run build

# start app
# CMD npm build-prod

# Stage 1, for copying the compiled app from the previous step and making it ready for production with Nginx
FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /usr/local/app/dist/news /usr/share/nginx/html
