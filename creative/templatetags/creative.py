import re
from django import template

from creative.utils import get_menu_items

register = template.Library()
assignment_tag = register.assignment_tag if hasattr(register, 'assignment_tag') else register.simple_tag


@register.filter
def clean_text(value):
    res = value.replace('\n', ' ')
    return res


@register.filter
def checkbox(value):
    res = re.sub(r"</?(?i:td)(.|\n)*?>", "", value)
    return res


@assignment_tag(takes_context=True)
def creative_get_menu(context):
    return get_menu_items(context)


@assignment_tag(takes_context=True)
def get_direction(context):
    res = {
        'panel': 'text-left',
        'notify': 'right',
        'float': 'float-right',
        'reverse_panel': 'text-right',
        'nav': 'ml-auto'
    }
    if context.get('LANGUAGE_BIDI'):
        res['panel'] = 'text-right'
        res['notify'] = 'left'
        res['float'] = ''
        res['reverse_panel'] = 'text-left'
        res['nav'] = 'mr-auto'
    return res


@assignment_tag(takes_context=True)
def get_creative_setting(context):
    user = context.get('request').user
    creative_setting = user.creative_setting if hasattr(user, 'creative_setting') else None
    res = {
        'sidebar_background': creative_setting.sidebar_background if creative_setting else 'primary',
        'dark_mode': creative_setting.dark_mode if creative_setting else True,
        'input_bg_color': '#ffffff' if creative_setting and not creative_setting.dark_mode else '#27293c'
    }

    return res
