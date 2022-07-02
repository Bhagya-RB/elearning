"""elearningproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as main_views
from instructorapp import views as instructor_views
from studentapp import views as student_views
from adminapp import views as admin_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_views.home, name='home'),
    path('about',main_views.about, name='about'),
    path('courses',main_views.courses, name='courses'),
    path('contact',main_views.contact, name='contact'),

    # Instructor URL's
    path('instructor-dashboard',instructor_views.instructor_dashboard,name='instructor-dashboard'),
    path('instructor-registration',instructor_views.instructor_registration,name='instructor-registration'),
    path('instructor-login',instructor_views.instructor_login, name='instructor-login'),
    path('instructor-addcourses',instructor_views.instructor_addcourses,name='instructor-addcourses'),

    path('instructor-managecourses',instructor_views.instructor_managecourses, name='instructor-managecourses'),

    path('instructor-editcourses',instructor_views.instructor_edit_courses, name='instructor-editcourses'),

    path('instructor-editcourses/<int:id>/',instructor_views.instructor_edit_courses, name='instructor-editcourses'),
    
    path('instructor-managecourses/<int:id>/',instructor_views.instructor_deletecourses, name='instructor-managecourses'),

    path('instructor-addtest',instructor_views.instructor_addtest, name='instructor-addtest'),
    path('instructor-view-courses',instructor_views.instructor_view_courses, name='instructor-view-courses'),
    path('instructor-view-students',instructor_views.instructor_view_students, name='instructor-view-students'),
    path('instructor-view-feedback',instructor_views.instructor_view_feedback, name='instructor-view-feedback'),
    path('instructor-profile',instructor_views.instructor_profile,name='instructor-profile'),

    # Students URL's
    path('student-dashboard',student_views.student_dashboard, name='student-dashboard'),
    path('student-registration',student_views.student_registration, name='student-registration'),
    path('student-login',student_views.student_login, name='student-login'),
    path('student-profile',student_views.student_profile, name='student-profile'),
    path('student-viewcourses',student_views.student_browsecourses,name='student-viewcourses'),
    path('student-enrollcourses',student_views.student_enrollcourses,name='student-enrollcourses'),
    path('student-mycourses',student_views.student_mycourses,name='student-mycourses'),
    path('student-quiz',student_views.student_quiz, name='student-quiz'),


    path('student-accessquiz',student_views.student_accessquiz, name='student-accessquiz'),

    path('student-accessquiz/<str:name>/',student_views.student_accessquiz,name='student-accessquiz'),

    path('student-result',student_views.student_result,name='student-result'),



    path('student-feedback',student_views.student_feedback, name='student-feedback'),

    #Admin URL's
    path('admin-index',admin_views.admin_index, name='admin-index'),
    path('admin-view-instructor',admin_views.admin_view_instructor, name='admin-view-instructor'),

    # accept reject provider urls
     path('accepts_instructor/<int:id>/',admin_views.accepts_instructor, name='accepts_instructor'),
     path('reject_instructor/<int:id>/',admin_views.reject_instructor, name='reject_instructor'),



    path('admin-view-students',admin_views.admin_view_students, name='admin-view-students'),
    path('admin-view-marks',admin_views.admin_view_marks, name='admin-view-marks'),

    path('admin-view-courses',admin_views.admin_view_courses, name="admin-view-courses"),
    path('admin-view-feedback',admin_views.admin_view_feedback, name="admin-view-feedback"),
    path('admin-login',admin_views.admin_login, name='admin-login')

    
    ]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
