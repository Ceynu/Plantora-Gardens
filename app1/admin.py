from django.contrib import admin

# Register your models here.
from . models import student
from . models import teacher
from . models import complaint
from . models import complaints
from . models import reply

class studentadmin(admin.ModelAdmin):
    list_display = ('name','course','year','department','phone','address','email','password','image')

class teacheradmin(admin.ModelAdmin):
    list_display = ('name','department','phone','email','password','image')
    
class complaintadmin(admin.ModelAdmin):
    list_display = ('s_name','t_name','description','submitted_date')

class complaintsadmin(admin.ModelAdmin):
    list_display = ('s_name','t_name','description','submitted_date')

class replyadmin(admin.ModelAdmin):
    list_display = ('s_name','t_name','message')








admin.site.register(student,studentadmin)
admin.site.register(teacher,teacheradmin)
admin.site.register(complaint,complaintadmin)
admin.site.register(complaints,complaintsadmin)
admin.site.register(reply,replyadmin)