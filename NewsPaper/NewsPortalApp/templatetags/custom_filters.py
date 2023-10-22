from django import template

register = template.Library()

BAD_WORDS = ["bla", "badword1", "badword2"]
forbidden_words = []


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


@register.filter
def hide_forbidden(value):
    words = value.split()
    result = []
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)