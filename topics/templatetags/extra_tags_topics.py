from django import template

register = template.Library()

@register.filter
def get_topic_notes(value, topic_pk):
    return value.filter(topic=topic_pk)

@register.filter
def get_importance_color(value):
    switcher = {
        0: "#dff0d8",
        1: "#fcf8e3",
        2: "#f2dede",
    }
    return switcher.get(value, "white")

#
#  Any note in color
#

@register.filter
def get_topic_color(value, topic_pk):
    # Return color of the topic header
    # @value - All notes
    # @topic_pk - Topic unique key
    if ( value.filter(topic=topic_pk, importance=2).count() > 0 ):
        return get_importance_color(2)
    if ( value.filter(topic=topic_pk, importance=1).count() > 0 ):
        return get_importance_color(1)
    return get_importance_color(0)

@register.filter
def get_topic_class(value, topic_pk):
    # Return class of the topic header
    # @value - All notes
    # @topic_pk - Topic unique key
    if ( value.filter(topic=topic_pk, importance=2).count() > 0 ):
        return "danger"
    if ( value.filter(topic=topic_pk, importance=1).count() > 0 ):
        return "warning"
    return "success "

#
#  Last note in color
#

# @register.filter
# def get_topic_color(value, topic_pk):
#     # Return color of the topic header
#     # @value - All notes
#     # @topic_pk - Topic unique key
#     switcher = {
#         0: "#dff0d8",
#         1: "#fcf8e3",
#         2: "#f2dede",
#     }
#     return switcher.get( value.values_list('importance', flat=True).filter(topic=topic_pk).order_by('-created')[:1].get(), "white")

# @register.filter
# def get_topic_class(value, topic_pk):
#     # Return class of the topic header
#     # @value - All notes
#     # @topic_pk - Topic unique key
#     switcher = {
#         0: "success",
#         1: "warning",
#         2: "danger",
#     }
#     #return switcher.get( value.values('importance').filter(topic=topic_pk).order_by('-created')[:1], "white" )
#     return switcher.get( value.values_list('importance', flat=True).filter(topic=topic_pk).order_by('-created')[:1].get(), "white")
