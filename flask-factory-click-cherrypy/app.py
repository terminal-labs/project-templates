import cherrypy

from app import create_app

application = create_app()

cherrypy.tree.graft(application, '/')
cherrypy.config.update({'server.socket_host': '127.0.0.1',
                        'server.socket_port': 5000,
                        'engine.autoreload.on': False,
                        })

if __name__ == '__main__':
    cherrypy.engine.start()
