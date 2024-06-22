from django import forms
from cars.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value < 10000:
            self.add_error('value', 'O valor mínimo é R$10.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year is not None and factory_year < 1886:
            self.add_error('factory_year', 'Não existem carros antes de 1886')
        return factory_year
    
    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        factory_year = self.cleaned_data.get('factory_year')

        if model_year is not None and model_year < 1886:
            self.add_error('model_year', 'Não existem carros antes de 1886')
        if factory_year is not None and model_year < factory_year:
            self.add_error('model_year', 'O ano do modelo do carro não pode ser menor que o ano de fabricação')
        return model_year
    
        