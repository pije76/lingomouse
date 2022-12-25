from django.contrib.auth.models import *

from rest_framework import serializers

from .models import *

class ProgressField(serializers.Field):
	def get_progress(self, value):
		value = 1
		return value

class CourseSerializer(serializers.ModelSerializer):
	level_count = serializers.SerializerMethodField(read_only=True)
	# word_count = serializers.SerializerMethodField(read_only=True)
	# level = serializers.IntegerField()
	# level_count = serializers.IntegerField(source="level.count", read_only=True)
	# mastered_word_count = serializers.SerializerMethodField(read_only=True)
	# progress = serializers.SerializerMethodField(read_only=True)
	# progress = ProgressField()


	def get_level_count(self, obj):
		get_level = Level.objects.filter(course=obj).count()
		# levels = obj.level_set.all().count()
		return get_level

	# def get_mastered_word_count(self, obj):
	# 	get_mastered_word = "1"
	# 	return get_mastered_word

	# def get_progress(self, obj):
	# 	get_mastered_word = "1"
	# 	get_progress_word = get_mastered_word/self.word_count
	# 	return get_progress_word

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
			'img',
			'level_count',
			'word_count',
			'mastered_word_count',
			'progress',
		)
		# lookup_field = 'id',
		# extra_kwargs = {
		# 	'url': {'lookup_field': 'id'}
		# }
		depth = 2


class LevelSerializer(serializers.ModelSerializer):
	# word_count = serializers.SerializerMethodField(read_only=True)

	# def get_word_count(self, obj):
	# 	get_word = Word.objects.filter(word=obj).count()
	# 	# levels = obj.level_set.all().count()
	# 	return get_word

	class Meta:
		model = Level
		fields = (
			'id',
			'sequence',
			'name',
			'course',
			'level_progress',
			'word_count',
		)
		depth = 3


class WordSerializer(serializers.ModelSerializer):
	pk = serializers.ReadOnlyField(source='id')

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
