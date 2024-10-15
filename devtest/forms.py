from django import forms
from devtest.models import Device

class DeviceTestForm(forms.Form):
    device = forms.ModelChoiceField(queryset=Device.objects.all(), label="Select Device")
