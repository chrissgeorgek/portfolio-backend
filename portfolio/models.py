from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=100)

    designation = models.CharField(max_length=150)

    headline = models.CharField(max_length=250)

    description = models.TextField()

    profile_image = models.ImageField(
        upload_to="hero/",
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )

    github = models.URLField()

    linkedin = models.URLField()

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=120)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):

    CATEGORY_CHOICES = [
        ("Frontend", "Frontend"),
        ("Backend", "Backend"),
        ("Database", "Database"),
        ("Tools", "Tools"),
        ("Cloud", "Cloud"),
    ]

    name = models.CharField(max_length=80)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["display_order", "name"]
        

class Project(models.Model):

    title = models.CharField(
        max_length=150
    )

    short_description = models.CharField(
        max_length=250
    )

    description = models.TextField()

    technologies = models.ManyToManyField(
        Skill,
        blank=True,
        related_name="projects",
    )

    project_image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
    )

    github_url = models.URLField(
        blank=True
    )

    live_demo_url = models.URLField(
        blank=True
    )

    featured = models.BooleanField(
        default=False
    )

    display_order = models.PositiveIntegerField(
        default=1
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:

        ordering = [
            "display_order",
            "-created_at",
        ]
        
class Experience(models.Model):

    company = models.CharField(
        max_length=150
    )

    designation = models.CharField(
        max_length=150
    )

    employment_type = models.CharField(
        max_length=50,
        blank=True
    )

    company_logo = models.ImageField(
        upload_to="experience/",
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    currently_working = models.BooleanField(
        default=False
    )

    description = models.TextField()

    technologies = models.ManyToManyField(
        Skill,
        blank=True,
        related_name="experiences"
    )

    display_order = models.PositiveIntegerField(
        default=1
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = [
            "display_order",
            "-start_date",
        ]

    def __str__(self):

        return f"{self.designation} - {self.company}"
    
    
class Education(models.Model):

    institution = models.CharField(max_length=200)

    degree = models.CharField(max_length=200)

    field_of_study = models.CharField(max_length=200, blank=True)

    location = models.CharField(max_length=150, blank=True)

    start_date = models.DateField()

    end_date = models.DateField()

    grade = models.CharField(max_length=50, blank=True)

    description = models.TextField(blank=True)

    institution_logo = models.ImageField(
        upload_to="education/",
        blank=True,
        null=True
    )

    display_order = models.PositiveIntegerField(default=1)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-end_date"]

    def __str__(self):
        return f"{self.degree} - {self.institution}"
    
class Certificate(models.Model):

    title = models.CharField(
        max_length=200,
    )

    issuer = models.CharField(
        max_length=200,
    )

    issue_date = models.DateField()

    credential_id = models.CharField(
        max_length=200,
        blank=True,
    )

    certificate_url = models.URLField(
        blank=True,
    )

    certificate_image = models.ImageField(
        upload_to="certificates/",
        blank=True,
        null=True,
    )

    display_order = models.PositiveIntegerField(
        default=1,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        ordering = [
            "display_order",
            "-issue_date",
        ]

    def __str__(self):

        return self.title    
    
class ContactMessage(models.Model):

    name = models.CharField(
        max_length=150,
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200,
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = [
            "-created_at",
        ]

    def __str__(self):

        return f"{self.name} - {self.subject}"