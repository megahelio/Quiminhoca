FROM node:22 AS builder
WORKDIR /app
COPY quiminhoca-frontend/package.json .
RUN npm install
COPY  quiminhoca-frontend/ .
RUN npm run build

FROM nginx:stable-alpine
WORKDIR /
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
