FROM node:20-alpine AS build
WORKDIR /app

# Добавьте ARG для build-time переменных (они подхватятся в process.env во времяビルда)
ARG YANDEX_TOKEN
ARG API_BASE_URL=http://localhost:8000  # Fallback, если не передан

# Сделайте их ENV для доступности в build process
ENV YANDEX_TOKEN=${YANDEX_TOKEN}
ENV API_BASE_URL=${API_BASE_URL}

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM node:20-alpine AS production
WORKDIR /app

# Для runtime (если нужно, например, для Nitro в runtime, но в вашем случае - build time)
ENV YANDEX_TOKEN=${YANDEX_TOKEN}
ENV API_BASE_URL=${API_BASE_URL:http://backend:8000}

COPY --from=build /app/.output ./.output
COPY package*.json ./

RUN npm ci --omit=dev

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]