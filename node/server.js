var redis_host = process.env.REDIS_SERVER_HOST;
var redis_port = process.env.REDIS_PORT;
var port = 3000;
//import http
var http = require("http");
//import express
var app = require('express')();
//import http
var config_http = require('http').Server(app);
//import socket.io
var io = require('socket.io')(config_http);
//import redis to conection with redis
var RedisNotifier = require('redis-notifier');
//redis library
var redis = require("redis");

var eventNotifier = new RedisNotifier(redis, {
    redis : { host : redis_host, port : redis_port },
    expired : true,
    evicted : true,
    logLevel : 'DEBUG'
})


subscriberClient = redis.createClient({host: redis_host, port: redis_port,}), schedQueueClient = redis.createClient({host: redis_host, port: redis_port,});

subscriberClient.subscribe('nuevo_turno');

subscriberClient.on('message', function(channel, message) {
    try {
        message = eval('(' + message + ')')
    } catch (error) {
        console.log(error)
    }
    
    switch(channel)
    {
        case "nuevo_turno":
            io.sockets.emit('nuevo_turno', message);
        break;
    }
});

config_http.listen(port, function(){
    console.log('listening on *:' + port);
});