###Learning material
* [Learning JavaScript Design Pattern](http://addyosmani.com/resources/essentialjsdesignpatterns/book/)
* [Javascript fundation](http://www.javascriptkit.com/domref/)
* [JSON2](http://www.json.org/js.html)
* [HTML5 Up and Running](http://shop.oreilly.com/product/9780596806033.do) 
* [JQueryMobile](http://jquerymobile.com/) ->A unified, HTML5-based user interface system for all popular mobile device platforms
* [JQuery.tmpl.js](https://github.com/jquery/jquery-tmpl)
* [PhoneGap](http://phonegap.com/)
AutoBahn -> android browser supports websocket   
* [modernizr](http://modernizr.com/) uses [yepnopejs](http://yepnopejs.com/)   
* [Sizzle](http://sizzlejs.com/) - A pure-JavaScript CSS selector engine
designed to be easily dropped in to a host library.   
* [CouchDB](http://couchdb.apache.org/)   
	that uses JSON for documents   
	JavaScript for MapReduce queries   
	and regular HTTP for an API   
* [DOM Level 3 Events Specification](http://www.w3.org/TR/DOM-Level-3-Events/)
* [QUnit](http://qunitjs.com/)
* [Node.js](http://nodejs.org/)
* [npm](https://npmjs.org/)


##Notes

* HTML5 云端应用架构   
  Client-Server => Device Server(need long connection)   
  Pull Data => Push Data   
  WebSocket   
  NodeJS   
  _Platform shifting_  
	* Assemble     
	* DLL   
	* JVM   
	* Browser 
  
 HTML5/Javascript困境:不能调用platform API => PhoneGap   
 Javacript Debug
	* firebug

* Data Push基本架构   
	* WebSocket   
	* Event driven   


* To do   
	Install NodeJS - done   
	Setup Android or iOS development env  
	Install PhoneGap  
	Put the exercises into phone project and make it work with server   
	Understand the 4 patterns of JavaScript:   
	* Module   
	* Contructor   
	* Facotry   
	* JQuery plugin   

* Javascript development tips
	* Module to isolate code   
	* No blocking code - like sleep(..) - should setTimeOut(func, timeout)   
	* Javascript in Browser is single thread mode, so NO use sleep() which will block UI.   
	* Server side receive JSON object, don't dump it and keep/save it in DB/memory as string. This is because when the data is pushed back to client, it still needs the format of string. If it is saved as object, when the data is returned to client, it still need to Stringify the object to string, which decrease the performance.  
	* if the server side push an object back to client, on the client side, it could be some problem. So the skill is that save the data from client in an array(which is not object in JavaScript), then when server pushes data to client, just SendUTF(array) (array will be sent as string), then client side could use JSON.parse(string) to an object   
	* when call JSON.parse(string), please use   
		>var msg = '[' + message.data + ']';  
		>var data = JSON.parse(msg);
* Source code  
	* https://github.com/moko365/html5-game-bubble-training -> please see the commits which is saved step by step  
	* https://github.com/jollen/html5-game-bubble
	* https://github.com/jollen/html5-websocket-nodejs
	* https://github.com/jollen/node-websocket-server	