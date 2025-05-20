FROM node:20-alpine

RUN npm install -g vsce

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run compile

RUN vsce package

CMD cp *.vsix /out/
