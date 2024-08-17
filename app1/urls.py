from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('student_registration/',views.student_registration,name='student_registration'),
    path('teacher_registration/',views.teacher_registration,name='teacher_registration'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('student_profile',views.student_profile,name='student_profile'),
    path('teacher_profile',views.teacher_profile,name='teacher_profile'),
    path('view_teacher_list',views.view_teacher_list,name='view_teacher_list'),
    path('student_view_reply/<int:id>',views.student_view_reply,name ='student_view_reply'),

    path('complaint_registration/<int:id>',views.complaint_registration,name='complaint_registration'),
    path('complaint_registration/complaintreg/<int:id>',views.complaintreg,name='complaintreg'),

    path('regeditstd',views.regeditstd,name='regeditstd'),
    path('editstd/<int:id>',views.editstd,name='editstd'),
    path('editstd/stdupdateext/<int:id>',views.stdupdateext,name='stdupdateext'),
    path('stddlt/<int:id>/', views.stddlt, name='stddlt'),

    path('regedittchr',views.regedittchr,name='regedittchr'),
    path('edittchr/<int:id>',views.edittchr,name='edittchr'),
    path('edittchr/tchrupdateext/<int:id>',views.tchrupdateext,name='tchrupdateext'),
    path('tchrdlt/<int:id>/', views.tchrdlt, name='tchrdlt'),  

    path('teacher_view_complaint_list/',views.teacher_view_complaint_list,name='teacher_view_complaint_list') ,
    
    path('complaint_reply/<int:id>', views.complaint_reply, name='complaint_reply'),
    path('replyreg/<int:id>', views.replyreg, name='replyreg'),
    path('student_view_reply/',views.student_view_reply,name='student_view_reply')
]
