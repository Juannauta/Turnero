FROM node:11.1.0-alpine

RUN apk add g++ make python

WORKDIR /usr/app


ADD package.json package.json
RUN npm install nodemon -g &&\
	npm install --quiet && \
	npm audit fix --force && \
	npm update

COPY . .


EXPOSE 3000

CMD npm start