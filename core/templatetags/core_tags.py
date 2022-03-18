from django import template
from ..forms import FeedbackForm

register = template.Library()

@register.simple_tag(name='feedback_form')
def feedback_form(prefix=''):
    return FeedbackForm(prefix=prefix)
