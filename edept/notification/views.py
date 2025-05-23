import uuid
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def my_notification_view(request):
    message_id = str(uuid.uuid4())  
    channel_layer = get_channel_layer()

    try:
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "notify",
                "content": {
                    "message": "Hey...I'm your new notification!",
                    "message_id": message_id,
                }
            }
        )
        return JsonResponse({"status": "Sent", "message_id": message_id})
    except Exception as e:
        return JsonResponse({"status": "Failed", "error": str(e)}, status=500)
