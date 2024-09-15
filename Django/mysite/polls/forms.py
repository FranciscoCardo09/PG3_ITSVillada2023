from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'fecha_nacimiento', 'nacionalidad']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }

from .models import Libro

class LibroForm(forms.ModelForm):
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), empty_label="Seleccione un autor")

    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'disponibilidad']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }

from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), empty_label="Seleccione un libro")
    
    class Meta:
        model = Prestamo
        fields = ['libro', 'fecha_devolucion', 'prestado_a']
        widgets = {
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }