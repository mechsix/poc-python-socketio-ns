"""
Entrypoint of poc module
"""
import socketio
import tornado

class NsHandler(socketio.AsyncNamespace):
    async def on_echo(self, sid, message):
        room = '/{0}'.format(sid)

        self.enter_room(sid, room)
        await self.send(f'>>>', room=room)
        self.leave_room(sid, room)

    async def on_connect(self, sid, message):
        print(">>>", sid, message)

        await self.send('zzz')

def launch():
    sio = socketio.AsyncServer(async_mode='tornado', cors_allowed_origins='*')
    sio.register_namespace(NsHandler('/foo')) 
    app = tornado.web.Application([
        (r"/io/", socketio.get_tornado_handler(sio))
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    print("Launching")
    launch()
    print("Ended")
