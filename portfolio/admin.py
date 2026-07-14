from django.contrib import admin
from .models import Certificate, ContactMessage, Hero, Skill
from .models import Hero, Skill, Project, Experience, Education
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "updated_at", 
    )
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "display_order",
        "is_active",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "name",
    )
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "featured",
        "display_order",
        "is_active",
    )

    list_filter = (
        "featured",
        "is_active",
    )

    search_fields = (
        "title",
    )

    filter_horizontal = (
        "technologies",
    )
    
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "company",
        "designation",
        "currently_working",
        "display_order",
        "is_active",
    )

    list_filter = (
        "currently_working",
        "is_active",
    )

    search_fields = (
        "company",
        "designation",
    )

    filter_horizontal = (
        "technologies",
    )
    
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = (
        "institution",
        "degree",
        "end_date",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "institution",
        "degree",
    )
    
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "issuer",
        "issue_date",
        "display_order",
        "is_active",
    )

    search_fields = (
        "title",
        "issuer",
    )

    list_filter = (
        "is_active",
    )
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (

        "name",

        "email",

        "subject",

        "is_read",

        "created_at",

    )

    list_filter = (

        "is_read",

    )

    search_fields = (

        "name",

        "email",

        "subject",

    )