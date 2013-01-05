import web
        
urls = (
    #'/(hello)', 'hello'    #test for notfound
     '/hello', 'hello'      #test for internalerror
)
class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'
    
def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")

    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))

def internalerror():
    return web.internalerror("Bad, bad server. No donut for you.")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.notfound = notfound
    app.internalerror = internalerror
    app.run()
        

