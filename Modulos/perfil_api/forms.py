from django import forms


from Modulos.perfil_api.models import *
 


class formulario (forms.ModelForm):

    class Meta: 
        model = productos 
        fields = '__all__'

        widget = {

            'id_descripcion': forms.TextInput(
                attrs= {
                    'id': 'id_descripcion', 'requerid':True, 'placeholder': 'Escribe la descipcion'
                }
            )
        }
        

      

