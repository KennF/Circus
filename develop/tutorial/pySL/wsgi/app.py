def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    content = ''
    for k,v in environ.items():
        content +='%s: %s' % (k, v) + '<br/>'
    return '<div>Hello world!</div> <div>%s</div>' % content