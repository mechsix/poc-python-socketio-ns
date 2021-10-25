"""
Entrypoint of poc module
"""
import socketio
import torando


sio = socketio.AsyncServer(async_mode='tornado')
app = torando.web.Application([
    (r"/socket.io/", socketio.get_tornado_handler(sio))
])

app = tg
if __name__ == '__main__':
    print('in')
