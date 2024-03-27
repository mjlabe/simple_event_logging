import logging
from typing import List

from django.conf import settings
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja.pagination import paginate, LimitOffsetPagination

from device_logging.models import DeviceLogOut, DeviceLog, DeviceLogPost

api = NinjaAPI()

fmt = getattr(settings, "LOG_FORMAT", None)
lvl = getattr(settings, "LOG_LEVEL", logging.DEBUG)

logging.basicConfig(format=fmt, level=lvl)
logging.debug("Logging started on %s for %s" % (logging.root.name, logging.getLevelName(lvl)))


@api.get("/log", response=List[DeviceLogOut])
@paginate(LimitOffsetPagination)
def get_log(request, device: str = None):
    return (
        DeviceLog.objects.filter(device=device).order_by("-id") if device else DeviceLog.objects.all().order_by("-id")
    )


@api.post("/log", response=DeviceLogOut)
def post_log(request, payload: DeviceLogPost):
    device_log = DeviceLog.objects.create(**payload.dict())
    logging.debug(device_log)
    return device_log


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
