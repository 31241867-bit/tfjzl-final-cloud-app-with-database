
from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'course', 'grade']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    list_filter = ['course']
    search_fields = ['title']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['name', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['name']


admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)
