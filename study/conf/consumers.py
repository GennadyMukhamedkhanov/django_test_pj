import json
from pprint import pprint

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("🟢 ===== CONNECT =====")
        try:
            self.room_name = self.scope["url_route"]["kwargs"]["room_name"]

        except KeyError:
            self.room_name = "test"
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        print(f"✅ Клиент в {self.room_group_name}")

    async def disconnect(self, close_code):
        print(f"🔴 Отключен: {close_code}")

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            print(f"📨 RAW: '{text_data}'")

            # ФИКС: поддержка текста И JSON
            try:
                data = json.loads(text_data)
                message = data.get("message", text_data)
            except json.JSONDecodeError:
                message = text_data  # сырой текст

            print(f"📨 MESSAGE: '{message}'")
            pprint(self.__dict__)

            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "message": message, "username": "Anonymous"}
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"username": event["username"], "message": event["message"]}))
