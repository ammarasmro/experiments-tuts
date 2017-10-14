var http = require('http');
var mF = require('./myfirstmodule');

http.createServer(function(req,res){
	res.writeHead(200, {'Content-Type': 'Text/html'});
	res.write("The result from my module" + mF.myFunc() )
	res.end('Hello World!');
}).listen(8080);