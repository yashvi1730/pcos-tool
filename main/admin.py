from django.contrib import admin
from main.models import Patient,Medical_History,Schedule,Pcos_History,Purpose_of_visit,Test,Mensis

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=['name','age','city','number','email','weight','height_feet','height_inches']

class Medical_HistoryAdmin(admin.ModelAdmin):
    list_display=[ 'pcos_medication','other_medication','allergies']

class ScheduleAdmin(admin.ModelAdmin):
    list_display=['date','time']

class Pcos_HistoryAdmin(admin.ModelAdmin):
    list_display=['pcos_diagnosed_age','acne','excess_hair_growth','irr_period','weight_gain','hair_loss','diff_conceiving','poly_cystic_ovaries','other','none','lactation','skin_tag_armpit','sleeping_disorder','hypothyroidism','sudden_hunger','headaches','sex_drive','feel_of_guilt']

class Purpose_of_visitAdmin(admin.ModelAdmin):
    list_display=['purpose','add_reason','docfile']



class TestAdmin(admin.ModelAdmin):
    list_display=['t_name','t_age']




class MensisAdmin(admin.ModelAdmin):
    list_display=['m_age_first_period','m_date_last_period','m_cycle_len','m_period_len','m_flow_amount','m_pain_scale','m_bleed']

admin.site.register(
    Patient,
    PatientAdmin,
    )

admin.site.register(
    Medical_History,
    Medical_HistoryAdmin,
    )

admin.site.register(
    Schedule,
    ScheduleAdmin,
)

admin.site.register(
    Pcos_History,
    Pcos_HistoryAdmin,
)

admin.site.register(
    Purpose_of_visit,
    Purpose_of_visitAdmin,
)



admin.site.register(
    Test,
    TestAdmin,
)

admin.site.register(
    Mensis,
    MensisAdmin,
)



