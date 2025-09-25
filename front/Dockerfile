FROM node:20-alpine AS build
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM node:20-alpine AS production
WORKDIR /app

COPY --from=build /app/.output ./.output
COPY package*.json ./

RUN npm ci --omit=dev

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]