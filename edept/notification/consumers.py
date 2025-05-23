# consumers.py
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def notify(self, event):
        content = event["content"]
        content["status"] = "sent"  
        content["message_id"] = content.get("message_id", "default-id")
        await self.send_json(content)

    async def receive_json(self, content, **kwargs):
        if content.get("type") == "delivered":
            print(f"Delivered: {content.get('message_id')}")
