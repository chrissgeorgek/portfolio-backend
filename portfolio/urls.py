from django.urls import path

from .views import (CertificateDetailAPIView, CertificateAPIView, ContactMessageAPIView, ContactMessageDetailAPIView, HeroAPIView,SkillAPIView,

SkillDetailAPIView,DashboardAPIView,
ProjectAPIView,
ProjectDetailAPIView,
ExperienceAPIView,
ExperienceDetailAPIView,
EducationAPIView,
EducationDetailAPIView,
)

urlpatterns = [

    path("hero/",HeroAPIView.as_view(),name="hero",),

    path("skills/",SkillAPIView.as_view(),name="skills",),

    path("skills/<int:pk>/",SkillDetailAPIView.as_view(),name="skill-detail",),

    path("dashboard/",DashboardAPIView,name="dashboard",),
    path("projects/",ProjectAPIView.as_view(),name="projects",),

    path("projects/<int:pk>/",ProjectDetailAPIView.as_view(),name="project-detail",),
    path("experience/",ExperienceAPIView.as_view(),name="experience",),

    path("experience/<int:pk>/",ExperienceDetailAPIView.as_view(),name="experience-detail",),
    path("education/",EducationAPIView.as_view(),name="education",),

    path("education/<int:pk>/",EducationDetailAPIView.as_view(),name="education-detail",),
    
    path(
    "certificates/",
    CertificateAPIView.as_view(),
    name="certificates",
),

path(
    "certificates/<int:pk>/",
    CertificateDetailAPIView.as_view(),
    name="certificate-detail",
),

path(
    "messages/",
    ContactMessageAPIView.as_view(),
    name="messages",
),

path(
    "messages/<int:pk>/",
    ContactMessageDetailAPIView.as_view(),
    name="message-detail",
),

]