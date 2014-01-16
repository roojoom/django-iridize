# see http://stackoverflow.com/questions/2160261/access-request-in-django-custom-template-tags
from django import template
from django.conf import settings
import time

register = template.Library()


# settings value
@register.inclusion_tag('iridize_script.html', takes_context=True)
def iridize_script(context):
    request = context['request']
    vars = {
        'iridize_env': settings.IRIDIZE_ENV,
        'is_iridize_enabled': settings.IS_IRIDIZE_ENABLED,
        'user_id': request.user.id,
        'joined_at': int(time.mktime(request.user.date_joined.timetuple()))
    }
    return vars


# Usage:
# {% load iridize %}
#
# {% iridize_script %}