from django import forms


class AddProduct(forms.Form):
    title = forms.CharField(max_length=20, required=True, label="Название товара",
                            widget=forms.TextInput(
                            attrs={ 'class': 'form-control rounded-3', 
                                    'id': 'floatingInput',
                                    'placeholder': 'Название'}))

    description = forms.CharField(max_length=30, required=True, label="Описание товара",
                                  widget=forms.TextInput(
                                  attrs={ 'class': 'form-control rounded-3', 
                                          'id': 'floatingInput',
                                          'placeholder': 'Описание'}))


class AddVendor(forms.Form):
    title = forms.CharField(max_length=20, required=True, label="Название компании",
                            widget=forms.TextInput(
                            attrs={ 'class': 'form-control rounded-3', 
                                    'id': 'floatingInput',
                                    'placeholder': 'Название'}))