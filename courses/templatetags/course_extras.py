from django import template

register = template.Library()


@register.simple_tag
def get_lessons_names(course, module_name):
    module = course.modules.filter(name__exact=module_name)
    return [lesson.name for lesson in module.lessons.all()]
