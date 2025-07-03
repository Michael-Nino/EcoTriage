from django import forms
from .models import SimulacionAmbiental

class SimulacionForm(forms.ModelForm):
    # Opciones para el campo medio_transporte
    TRANSPORTE_CHOICES = [
        ("", "Seleccione un medio de transporte"),
        ("A pie", "A pie"),
        ("Bicicleta", "Bicicleta"),
        ("Transporte público", "Transporte público"),
        ("Auto particular", "Auto particular"),
        ("Moto", "Moto"),
        ("Otro", "Otro")
    ]

    medio_transporte = forms.ChoiceField(
        choices=TRANSPORTE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label="Medio de transporte principal"
    )
    """
    Formulario para crear simulaciones ambientales
    """
    
    class Meta:
        model = SimulacionAmbiental
        fields = [
            'edad',
            'ciudad',
            'medio_transporte',
            'km_por_dia',
            'carne_por_semana',
            'vegetales_por_semana',
            'horas_luz_dia',
            'separa_residuos',
        ]
        
        widgets = {
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu edad',
                'min': '1',
                'max': '120'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Lima, Arequipa, Cusco'
            }),
            'medio_transporte': forms.Select(attrs={
                'class': 'form-control'
            }),
            'km_por_dia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kilómetros que recorres diariamente',
                'min': '0',
                'step': '0.1'
            }),
            'carne_por_semana': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Veces que comes carne por semana',
                'min': '0',
                'max': '21'
            }),
            'vegetales_por_semana': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Veces que comes vegetales por semana',
                'min': '0',
                'max': '21'
            }),
            'horas_luz_dia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Horas de luz artificial que usas',
                'min': '0',
                'max': '24',
                'step': '0.5'
            }),
            'separa_residuos': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        
        labels = {
            'edad': 'Edad (años)',
            'ciudad': 'Ciudad donde vives',
            'medio_transporte': 'Medio de transporte principal',
            'km_por_dia': 'Kilómetros recorridos por día',
            'carne_por_semana': 'Veces que comes carne por semana',
            'vegetales_por_semana': 'Veces que comes vegetales por semana',
            'horas_luz_dia': 'Horas de luz artificial por día',
            'separa_residuos': '¿Separas tus residuos?',
        }
        
        help_texts = {
            'edad': 'Ingresa tu edad en años',
            'ciudad': 'Ciudad principal donde vives',
            'medio_transporte': 'Selecciona tu medio de transporte más usado',
            'km_por_dia': 'Aproximadamente cuántos kilómetros recorres diariamente',
            'carne_por_semana': 'Incluye pollo, res, cerdo, pescado, etc.',
            'vegetales_por_semana': 'Incluye frutas, verduras, legumbres',
            'horas_luz_dia': 'Promedio de horas de luz eléctrica que usas',
            'separa_residuos': 'Marca si separas residuos orgánicos de inorgánicos',
        }

    def clean_edad(self):
        """Validación personalizada para edad"""
        edad = self.cleaned_data.get('edad')
        if edad is not None and (edad < 1 or edad > 120):
            raise forms.ValidationError('La edad debe estar entre 1 y 120 años.')
        return edad

    def clean_km_por_dia(self):
        """Validación personalizada para kilómetros por día"""
        km_por_dia = self.cleaned_data.get('km_por_dia')
        if km_por_dia is not None and km_por_dia < 0:
            raise forms.ValidationError('Los kilómetros no pueden ser negativos.')
        if km_por_dia is not None and km_por_dia > 500:
            raise forms.ValidationError('Los kilómetros por día parecen demasiado altos.')
        return km_por_dia

    def clean_carne_por_semana(self):
        """Validación personalizada para consumo de carne"""
        carne_por_semana = self.cleaned_data.get('carne_por_semana')
        if carne_por_semana is not None and carne_por_semana < 0:
            raise forms.ValidationError('El consumo de carne no puede ser negativo.')
        if carne_por_semana is not None and carne_por_semana > 21:
            raise forms.ValidationError('No puedes comer carne más de 21 veces por semana.')
        return carne_por_semana

    def clean_vegetales_por_semana(self):
        """Validación personalizada para consumo de vegetales"""
        vegetales_por_semana = self.cleaned_data.get('vegetales_por_semana')
        if vegetales_por_semana is not None and vegetales_por_semana < 0:
            raise forms.ValidationError('El consumo de vegetales no puede ser negativo.')
        if vegetales_por_semana is not None and vegetales_por_semana > 21:
            raise forms.ValidationError('No puedes comer vegetales más de 21 veces por semana.')
        return vegetales_por_semana

    def clean_horas_luz_dia(self):
        """Validación personalizada para horas de luz"""
        horas_luz_dia = self.cleaned_data.get('horas_luz_dia')
        if horas_luz_dia is not None and horas_luz_dia < 0:
            raise forms.ValidationError('Las horas de luz no pueden ser negativas.')
        if horas_luz_dia is not None and horas_luz_dia > 24:
            raise forms.ValidationError('No puedes usar más de 24 horas de luz por día.')
        return horas_luz_dia

    def clean(self):
        """Validación general del formulario"""
        cleaned_data = super().clean()
        carne_por_semana = cleaned_data.get('carne_por_semana')
        vegetales_por_semana = cleaned_data.get('vegetales_por_semana')
        # Validar que tenga al menos algo de alimentación
        if (
            carne_por_semana is not None and vegetales_por_semana is not None and
            carne_por_semana == 0 and vegetales_por_semana == 0
        ):
            raise forms.ValidationError(
                'Debes consumir al menos algo de carne o vegetales por semana.'
            )
        return cleaned_data