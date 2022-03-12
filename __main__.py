from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()

sio.attach(app)

@sio.on('msg')
async def print_message(sid, message):
    print(message["sender"] + " said " + message["text"] + " in " + message["chat"])
    await sio.emit("newmsg", {"text": message["text"], "chat": message["chat"], "sender": message["sender"]})

if __name__ == '__main__':
    web.run_app(app)