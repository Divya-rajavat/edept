from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse, HttpResponseNotAllowed

def my_notification_view(request):
    if request.method == "GET":
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "notify",
                "content": {
                    "message": "Hello...I'm your new notification",
                }
            }
        )
        return JsonResponse({"status": "Notification sent"})
    else:
        return HttpResponseNotAllowed(['GET'])
