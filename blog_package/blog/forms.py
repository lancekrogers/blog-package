from django import forms
from PIL import Image
from PIL import Image  # this is needed for the models.ImageField to work
from stickyuploads.widgets import StickyUploadWidget


class PhotoForm(forms.Form):
    image = forms.ImageField(label='Please upload a profile image',
                            required=False,
                            widget=StickyUploadWidget,
                            error_messages={'invalid_file': 'Please upload an image'}
                            )