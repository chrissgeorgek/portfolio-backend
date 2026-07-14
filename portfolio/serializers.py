from rest_framework import serializers
from .models import ContactMessage, Education, Hero, Skill, Project, Experience, Certificate

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"
        
class SkillSerializer(serializers.ModelSerializer):

    class Meta:

        model = Skill

        fields = "__all__"
        
class ProjectWriteSerializer(serializers.ModelSerializer):

    technologies = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Skill.objects.all(),
        required=False,
    )

    class Meta:

        model = Project

        fields = "__all__"

    def create(self, validated_data):

        technologies = validated_data.pop(
            "technologies",
            []
        )

        project = Project.objects.create(
            **validated_data
        )

        project.technologies.set(
            technologies
        )

        return project

    def update(self, instance, validated_data):

        technologies = validated_data.pop(
            "technologies",
            None
        )

        for attr, value in validated_data.items():

            setattr(
                instance,
                attr,
                value,
            )

        instance.save()

        if technologies is not None:

            instance.technologies.set(
                technologies
            )

        return instance

class ProjectReadSerializer(serializers.ModelSerializer):

    technologies = SkillSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Project

        fields = "__all__"
        
class ExperienceWriteSerializer(serializers.ModelSerializer):

    technologies = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Skill.objects.all(),
        required=False,
    )

    class Meta:

        model = Experience

        fields = "__all__"

    def create(self, validated_data):

        technologies = validated_data.pop(
            "technologies",
            []
        )

        experience = Experience.objects.create(
            **validated_data
        )

        experience.technologies.set(
            technologies
        )

        return experience

    def update(self, instance, validated_data):

        technologies = validated_data.pop(
            "technologies",
            None
        )

        for attr, value in validated_data.items():

            setattr(
                instance,
                attr,
                value,
            )

        instance.save()

        if technologies is not None:

            instance.technologies.set(
                technologies
            )

        return instance


class ExperienceReadSerializer(serializers.ModelSerializer):

    technologies = SkillSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Experience

        fields = "__all__"
        
class EducationWriteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Education

        fields = "__all__"


class EducationReadSerializer(serializers.ModelSerializer):

    class Meta:

        model = Education

        fields = "__all__"
        
class CertificateWriteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Certificate

        fields = "__all__"


class CertificateReadSerializer(serializers.ModelSerializer):

    class Meta:

        model = Certificate

        fields = "__all__"
        
class ContactMessageWriteSerializer(serializers.ModelSerializer):

    class Meta:

        model = ContactMessage

        fields = "__all__"


class ContactMessageReadSerializer(serializers.ModelSerializer):

    class Meta:

        model = ContactMessage

        fields = "__all__"