from django import template

register = template.Library()

@register.filter
def get_importance_label(value):
    switcher = {
        0: "<button type=\"button\" class=\"btn btn-success btn-sm\">Good</button>",
        1: "<button type=\"button\" class=\"btn btn-warning btn-sm\">Warning</button>",
        2: "<button type=\"button\" class=\"btn btn-danger btn-sm\"> Bad</button>",
    }
    return switcher.get(value, "<button type=\"button\" class=\"btn btn-default\">Unknown</button>")

