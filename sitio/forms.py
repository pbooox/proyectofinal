from django import forms
from .models import Cliente, Bebida, Ingrediente

class FormCli(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'email',)


class FormIng(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = ('nombre',)

class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ('cliente', 'ingredientes',)

    def __init__ (self, *args, **kwargs):
        super(BebidaForm, self).__init__(*args, **kwargs)
        self.fields["ingredientes"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["ingredientes"].help_text = "Seleccione los ingredientes que desea en su bebida"
        self.fields["ingredientes"].queryset = Ingrediente.objects.all()