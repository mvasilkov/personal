from django import template

register = template.Library()

URLS = {
    'steamdb_app': 'https://steamdb.info/app/%d/',
    'steam_run': 'steam://rungameid/%d',
}


@register.simple_tag
def absolute_url(url_name, appid):
    return URLS[url_name] % appid
