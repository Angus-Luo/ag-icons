"""{% icon %} template tag — inline SVG from the ag_icons registry.

Usage:
    {% load icons %}
    {% icon "archive-box" %}
    {% icon "sparkles" class="w-4 h-4 text-warning" %}
"""

from django import template

from ag_icons import render_icon

register = template.Library()


@register.simple_tag
def icon(name, **kwargs):
    css_class = kwargs.get("class", "w-5 h-5")
    return render_icon(name, css_class)
