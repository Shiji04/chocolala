from django import forms

from .models import Order, Branch


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
            'address': forms.Textarea(attrs={'class': 'form-control','placeholder':'Address'}),
            'district': forms.Select(attrs={'class': 'form-control','placeholder':'---Select District---'}),
            'branch': forms.Select(attrs={'class': 'form-control','placeholder':'---Select Your City---'}),
            'chocolet': forms.Select(attrs={'class': 'form-control','placeholder':'---Select Chocolate---'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Quantity'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset=Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')