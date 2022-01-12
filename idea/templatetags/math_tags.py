from django import template

register = template.Library()  # Djangoのテンプレートタグライブラリ

# カスタムタグとして登録する


@register.simple_tag
def multiply(value1, value2):
    result = 2*value1 + value2
    return result
