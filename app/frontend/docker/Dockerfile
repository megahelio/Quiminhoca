FROM node:22 AS builder
WORKDIR /app
COPY ../package.json .
RUN npm install
RUN npm i -g serve
COPY ../. .
RUN npm run build

FROM nginx:stable-alpine
WORKDIR /
COPY --from=builder /app/dist /usr/share/nginx/html
COPY ./docker/nginx/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
