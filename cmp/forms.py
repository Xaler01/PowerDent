from django import forms

from .models import Proveedor, ComprasEnc


class ProveedorForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    class Meta:
        model = Proveedor
        exclude = ['um', 'fm', 'uc', 'fc']
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ComprasEncForm(forms.ModelForm):
    fecha_compra = forms.DateInput()
    fecha_factura = forms.DateInput()

    class Mega:
        model=ComprasEnc
        fields=['proveedor', 'fecha_compra', 'observacion',
                'no_factura', 'fecha_factura', 'subtotal',
                'descuento', 'total']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-comtrol'
                })
            self.fields['fecha_compra'].widget.attrs['reasonly'] = True
            self.fields['fecha_factura'].widget.attrs['reasonly'] = True
            self.fields['sub_total'].widget.attrs['reasonly'] = True
            self.fields['descuento'].widget.attrs['reasonly'] = True
            self.fields['total'].widget.attrs['reasonly'] = True