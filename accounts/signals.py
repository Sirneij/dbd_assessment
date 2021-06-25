from django.db.models.signals import  pre_save
from django.dispatch import receiver
from django.core.files.base import ContentFile


from io import BytesIO
from PIL import Image
from .models import User
THUMBNAIL_SIZE = (300, 300)

@receiver(pre_save, sender=User)
def generate_thumbnail(sender, instance, **kwargs):
    image = Image.open(instance.avatar)
    image = image.convert("RGB")
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    temp_thumb = BytesIO()
    image.save(temp_thumb, "JPEG")
    temp_thumb.seek(0)
    # set save=False, otherwise it will run in an infinite loop
    instance.avatar.save(
        instance.avatar.name,
        ContentFile(temp_thumb.read()),
        save=False,
    )
    temp_thumb.close()