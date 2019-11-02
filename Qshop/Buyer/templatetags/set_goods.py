from django import template

register=template.Library()

@register.filter
def uper(obj):
    return obj.upper()


@register.filter('rep')
def get_four(obj):
    return obj[:4]

@register.filter
def get_filter(obj):
    ret=obj.goods_set.filter(statue=1)[:4]
    return ret