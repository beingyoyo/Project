from django import forms
from dr_ui.models import ImageUpload


class PhotoUploadModelForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ('imageField',)
        labels = {'imageField': ('Image'), }
