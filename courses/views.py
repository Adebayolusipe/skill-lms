from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course, Module, Lesson
from content.models import TextContent, ImageContent, VideoContent, FileContent


def module_detail_with_lessons_view(request, module_id):
    """
    Displays a module with all its lessons and their content in a tabbed interface.
    Fetches lessons and all related content blocks for each lesson.
    """
    module = get_object_or_404(Module, id=module_id)

    lessons = module.lessons.all().order_by('order')

    lessons_data = []

    for lesson in lessons:
        text_blocks = lesson.text_content.all()
        image_blocks = lesson.image_content.all()
        video_blocks = lesson.video_content.all()
        file_blocks = lesson.file_content.all()

        all_content_for_lesson = sorted(
            list(text_blocks) + list(image_blocks) + list(video_blocks) + list(file_blocks),
            key=lambda content_block: content_block.order
        )

        lessons_data.append({
            'lesson_obj': lesson,
            'contents': all_content_for_lesson
        })

    context = {
        'module': module,
        'lessons_data': lessons_data,
        'current_module_id': module_id,
    }

    return render(request, 'courses/module_detail_with_lessons_view.html', context)


def course_list(request):
    """
    Displays a list of all available courses.
    """
    courses = Course.objects.all().order_by('title')
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, course_slug):
    """
    Displays details of a single course, including its modules and lessons.
    """
    course = get_object_or_404(Course, slug=course_slug)

    modules = course.modules.all().order_by('order')

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'modules': modules,
    })


def lesson_detail(request, course_slug, lesson_slug):
    """
    Displays the content of a single lesson.
    """

    lesson = get_object_or_404(
        Lesson,
        slug=lesson_slug,
        module__course__slug=course_slug
    )

    text_blocks = lesson.text_content.all()
    image_blocks = lesson.image_content.all()
    video_blocks = lesson.video_content.all()
    file_blocks = lesson.file_content.all()

    all_content = sorted(
        list(text_blocks) + list(image_blocks) + list(video_blocks) + list(file_blocks),
        key=lambda content_block: content_block.order
    )

    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson,
        'all_content': all_content,
    })
