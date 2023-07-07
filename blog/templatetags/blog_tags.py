from urllib.parse import urlencode
from django import template
# urllib.parse.urlencode()
import re
# from django.template.defaultfilters import stringfilter
from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    query.pop('page', None)
    query.update(kwargs)            # query.update({"andy": "s"}) 
    # return "&" + query.urlencode()  # return query.urlencode()
    if query:
        fancy_url = "&" + query.urlencode()
    else:
        fancy_url = query.urlencode() #normal way; no & attached..
    return fancy_url

# https://stackoverflow.com/questions/2047622/how-to-paginate-django-with-other-get-variables/57899037#comment115168364_36288962

@register.filter
# def rcleanup(recipe):
#     result = []
#     for line in recipe.splitlines():
#         if "TOOLS" in line:
#             tools_found = True
#             continue
#         elif "INGREDIENTS" in line:
#             tools_found = False
#             continue
#         elif tools_found:
#             continue
#         elif "<li" and "</li>" in line:
#             stripped = re.sub(r'[\n\t]*<[^<]+?>', '', line).rstrip()
#             quoted = f'"{stripped}"'
#             result.append(quoted)
#         elif "INSTRUCTIONS" in line:
#             break
#     return mark_safe(",\n".join(result))
#MORE CONCISE
def rcleanup(recipe):
    result = []
    skip = False
    for line in recipe.splitlines():
        if "TOOLS" in line:
            skip = True
        elif "INGREDIENTS" in line:
            skip = False
        elif not skip and "<li" and "</li>" in line:
            result.append(f'"{re.sub(r"<[^<]+?>", "", line).strip()}"')
        elif not skip and "INSTRUCTIONS" in line:
            break
    return mark_safe(",\n".join(result))