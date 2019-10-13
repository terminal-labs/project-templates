import cherrypy

html_header = \
    """
    <html>
        <head>
            <title>CherryPy Simple Demo</title>
        </head>
        <body>
    """

html_footer = \
    """
        <p><strong><a href='http://cherrypy.org/'>CherryPy</a></strong>: A Minimalist Python Web Framework</p>
    </body>
    </html>
    """

class HelloWorld(object):    
    @cherrypy.expose
    def index(self):
        html_body = \
            """
            <strong><em>Hello, World!</em><strong></br>
            <br>

            <form method="POST" action="post_method">
            <input type="text" value="" name="text_input"/>
            <button type="submit">submit</button>
            </form>
            """
        return html_header + html_body + html_footer

    @cherrypy.expose
    def post_method(self, text_input):
        if cherrypy.request.method == 'POST':
            html_body =  \
                """
                <h3><em>Hello, %s!</em></h3>
                <p>This is an example of POST method in CherryPy. <a href="/">Back to home</a></p>
                """ % text_input
            print("User POST string: "+text_input)
            return html_header + html_body + html_footer


if __name__ == '__main__':
    conf = { '/' : {}}
    cherrypy.quickstart(HelloWorld(), '/', conf)