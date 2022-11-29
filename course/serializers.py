from django.contrib.auth.models import *

from rest_framework import serializers

from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'description',
            'native',
            'foreign',
            'img',
            'is_active',
            # 'lang_code',
            'img',
            # 'level_count,
            # 'current_active_level_id',
            # 'word_count',
            # 'mastered_word_count',
            # 'word_to_review_count',
            # 'word_ignored_count',
            # 'word_difficult_count',
            # 'xp_point',
            # 'progress',
        )

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = (
            'id',
            'sequence',
            'name',
            'course',
        )

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = (
            'id',
            'word',
            'description',
            'literal_translation',
            'course',
            'level',
            'is_active',
        )
