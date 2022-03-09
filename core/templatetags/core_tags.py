from django import template
from ..forms import FeedbackForm

register = template.Library()

@register.simple_tag
def feedback_form():
    return FeedbackForm()