from django import forms
from main.models import Patient,Medical_History,Schedule,Pcos_History,Purpose_of_visit,Test,Mensis

class PatientForm(forms.ModelForm):
    class Meta:
        model =Patient
        fields='__all__'

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model=Medical_History
        fields='__all__'

class ScheduleForm(forms.ModelForm):
    class Meta:
        model=Schedule
        fields='__all__'

class Pcos_HistoryForm(forms.ModelForm):
    class Meta:
        model=Pcos_History
        fields='__all__'

class Purpose_of_visitForm(forms.ModelForm):
    class Meta:
        model=Purpose_of_visit
        fields='__all__'



class TestForm(forms.ModelForm):
    class Meta:
        model=Test
        fields='__all__'

class MensisForm(forms.ModelForm):
    class Meta:
        model=Mensis
        fields='__all__'

class FooterForm(forms.Form):
    f_email=forms.EmailField()

