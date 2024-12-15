from django.contrib.auth import get_user_model
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django import template
from django.utils.html import format_html

user_model = get_user_model()
register = template.Library()

@register.filter
def author_details(author, current_user= None):
  if not isinstance(author, user_model):
    return ""

  if author.first_name and author.last_name:
    name= escape(f"{author.first_name} {author.last_name}")
  else:
    name= escape(f"{ author.username}")

  if author.email:
    prefix = format_html('<a href="mailto:{}">', author.email)
    suffix = "</a>"

  else:
    prefix = ""
    suffix = ""

  return mark_safe(f"{prefix}{name}{suffix}")