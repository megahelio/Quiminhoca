FROM node:22 AS builder

WORKDIR /app

ARG VITE_FRONTEND_BASE_URL
ARG VITE_API_URL

ENV VITE_FRONTEND_BASE_URL=$VITE_FRONTEND_BASE_URL
ENV VITE_API_URL=$VITE_API_URL


COPY quiminhoca-frontend/package.json .
RUN npm install
COPY quiminhoca-frontend/ .

RUN npm run build

FROM nginx:stable-alpine
WORKDIR /

ARG VITE_FRONTEND_BASE_URL
ENV VITE_API_URL=$VITE_API_URL

COPY --from=builder /app/dist /usr/share/nginx/html/${VITE_FRONTEND_BASE_URL}

COPY nginx/default.conf /etc/nginx/conf.d/default.conf

RUN sed -i "s|/__BASE_PATH__/|${VITE_FRONTEND_BASE_URL}|g" /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
