FROM node:11.1.0-alpine

RUN apk add g++ make python

WORKDIR /usr/app

COPY node .
RUN npm install nodemon -g &&\
	npm install --quiet && \
	npm audit fix --force && \
	npm update



EXPOSE 3000

CMD ls && pwd && npm start