FROM node:19.6-bullseye-slim As base

WORKDIR /usr/scr/app

COPY package*.json ./

FROM base as prduction

ENV NODE_ENV production

RUN --mount=type=cache,target=/usr/src/app/.npm \
  npm set cache /usr/src/app/.npm && \
  npm install

USER node

COPY --chown=node:node ./healthcheck/ .
COPY --chown=node:node ./src . 
COPY --chown=node:node ./test . 

EXPOSE 3000

CMD ["node", "./index.js"]