from cloudinary.models import CloudinaryField

class MyCloudinaryField(CloudinaryField):
    """
    A custom Cloudinary field that provides a more explicit upload path.
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('folder', kwargs.pop('upload_to', None))
        super().__init__(*args, **kwargs)