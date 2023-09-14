from django import template

register = template.Library()

BAD_WORDS = ["bla", "badword1", "badword2"]


@register.filter()
def censor(value):

    checker = value.split(" ")

    for word in checker:
        if word in BAD_WORDS:
            get_id = checker.index(word)
            checker.remove(word)
            checker.insert(get_id, "*")
        else:
            continue

    censored_value = " ".join(checker)
    return censored_value
