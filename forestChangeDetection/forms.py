from django import forms

class ImportGeojsonfileForm(forms.Form):
    import_file = forms.FileField(label="Select a geojson file")