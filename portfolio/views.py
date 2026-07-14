from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Certificate, ContactMessage, Education, Hero, Skill,Project, Experience
from .serializers import CertificateReadSerializer, CertificateWriteSerializer, ContactMessageReadSerializer, ContactMessageWriteSerializer, HeroSerializer, ProjectReadSerializer, ProjectWriteSerializer, SkillSerializer,ExperienceReadSerializer
from .serializers import ExperienceWriteSerializer,EducationReadSerializer,EducationWriteSerializer
from rest_framework.generics import (
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    
    
)

class HeroAPIView(RetrieveUpdateAPIView):

    serializer_class = HeroSerializer

    def get_permissions(self):

        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]

    def get_object(self):
        return Hero.objects.first()
    
class SkillAPIView(ListCreateAPIView):

    serializer_class = SkillSerializer

    queryset = Skill.objects.all()

    def get_permissions(self):

        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]
    
class SkillDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = SkillSerializer

    queryset = Skill.objects.all()

    permission_classes = [IsAuthenticated]    
    
class ProjectAPIView(ListCreateAPIView):

    queryset = Project.objects.prefetch_related(
    "technologies"
).all()

    def get_permissions(self):

        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]

    def get_serializer_class(self):

        if self.request.method == "GET":

            return ProjectReadSerializer

        return ProjectWriteSerializer
    
class ProjectDetailAPIView(
    RetrieveUpdateDestroyAPIView
):

    queryset = Project.objects.prefetch_related(
        "technologies"
    ).all()

    permission_classes = [
        IsAuthenticated
    ]

    def get_serializer_class(self):

        if self.request.method == "GET":

            return ProjectReadSerializer

        return ProjectWriteSerializer

    
@api_view(["GET"])
def DashboardAPIView(request):

    return Response({

        "hero": Hero.objects.count(),

        "skills": Skill.objects.count(),

        "projects": Project.objects.count(),

        "experience": Experience.objects.count(),

        "education": Education.objects.count(),

        "certificates": Certificate.objects.count(),

        "messages": ContactMessage.objects.count(),

    })
    
class ExperienceAPIView(ListCreateAPIView):

    queryset = Experience.objects.prefetch_related(
        "technologies"
    ).all()

    def get_permissions(self):

        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]

    def get_serializer_class(self):

        if self.request.method == "GET":

            return ExperienceReadSerializer

        return ExperienceWriteSerializer


class ExperienceDetailAPIView(
    RetrieveUpdateDestroyAPIView
):

    queryset = Experience.objects.prefetch_related(
        "technologies"
    ).all()

    permission_classes = [
        IsAuthenticated
    ]

    def get_serializer_class(self):

        if self.request.method == "GET":

            return ExperienceReadSerializer

        return ExperienceWriteSerializer
    
class EducationAPIView(ListCreateAPIView):

    queryset = Education.objects.all()

    def get_permissions(self):

        if self.request.method == "GET":

            return [AllowAny()]

        return [IsAuthenticated()]

    def get_serializer_class(self):

        if self.request.method == "GET":

            return EducationReadSerializer

        return EducationWriteSerializer


class EducationDetailAPIView(
    RetrieveUpdateDestroyAPIView
):

    queryset = Education.objects.all()

    permission_classes = [
        IsAuthenticated
    ]

    def get_serializer_class(self):

        if self.request.method == "GET":

            return EducationReadSerializer

        return EducationWriteSerializer
    
class CertificateAPIView(ListCreateAPIView):

    queryset = Certificate.objects.all()

    def get_permissions(self):

        if self.request.method == "GET":

            return [AllowAny()]

        return [IsAuthenticated()]

    def get_serializer_class(self):

        if self.request.method == "GET":

            return CertificateReadSerializer

        return CertificateWriteSerializer


class CertificateDetailAPIView(
    RetrieveUpdateDestroyAPIView
):

    queryset = Certificate.objects.all()

    permission_classes = [
        IsAuthenticated
    ]

    def get_serializer_class(self):

        if self.request.method == "GET":

            return CertificateReadSerializer

        return CertificateWriteSerializer
    
class ContactMessageAPIView(ListCreateAPIView):

    queryset = ContactMessage.objects.all()

    def get_permissions(self):

        if self.request.method == "POST":

            return [AllowAny()]

        return [IsAuthenticated()]

    def get_serializer_class(self):

        if self.request.method == "GET":

            return ContactMessageReadSerializer

        return ContactMessageWriteSerializer


class ContactMessageDetailAPIView(
    RetrieveUpdateDestroyAPIView
):

    queryset = ContactMessage.objects.all()

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = ContactMessageReadSerializer