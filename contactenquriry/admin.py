from django.contrib import admin
from .models import contactEnquiry,singlepost
from .models import Post,Services,SubPlan,SubPlanFeature,Posts

class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','message')  # Correct 'emp-id' to 'emp_id'


class EmAdmin(admin.ModelAdmin):
    list_display=('name','email','message')


class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')

admin.site.register(contactEnquiry, EmpAdmin)
admin.site.register(singlepost,EmAdmin)
admin.site.register(Post)
admin.site.register(Services,ServiceAdmin)

# Register your models here.



class SubPlanFeatureInline(admin.TabularInline):
    model = SubPlanFeature
    extra = 1




class SubPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'highlight_status')
    list_editable = ('highlight_status',)  # You can edit 'highlight_status' directly from the list display
    inlines = [SubPlanFeatureInline]

admin.site.register(SubPlan, SubPlanAdmin)
class SubPlanFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'subplan')
    list_filter = ('subplan',)  # Add filter by subplan
    search_fields = ['title']  # Add search field for title

admin.site.register(SubPlanFeature, SubPlanFeatureAdmin)



admin.site.register(Posts)