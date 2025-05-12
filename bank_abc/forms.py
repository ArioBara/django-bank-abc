from dataclasses import field, fields
from django import forms
from .models import Transaksi, Nasabah, Rekening, Cabangbank

class Transferform(forms.ModelForm):
   class Meta:
       model = Transaksi
       fields = "__all__"

class Nasabahform(forms.ModelForm):
    class Meta:
        model = Nasabah
        fields = "__all__"

class Rekeningform(forms.ModelForm):
    class Meta:
        model = Rekening
        fields = "__all__"

class Cabangbankform(forms.ModelForm):
    class Meta:
        model = Cabangbank
        fields = "__all__"