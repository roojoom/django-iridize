# see http://stackoverflow.com/questions/2160261/access-request-in-django-custom-template-tags
from django import template
from django.conf import settings
import time

register = template.Library()


# settings value
@register.inclusion_tag('iridize_script.html', takes_context=True)
def iridize_script(context):
    request = context['request']
    joined_at_epoch = int(time.mktime(request.user.date_joined.timetuple())) if request.user.is_authenticated() else 0
    vars = {
        'iridize_env': settings.IRIDIZE_ENV,
        'iridize_appid': settings.IRIDIZE_APP_ID,
        'is_iridize_enabled': settings.IS_IRIDIZE_ENABLED,
        'user_id': request.user.id,
        'joined_at': joined_at_epoch
    }
    return vars


# Usage:
# {% load iridize %}
#
# {% iridize_script %}