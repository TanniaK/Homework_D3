from django import template
 
register = template.Library() # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются :(

FILTR_CENS = ['boogers','snot', 'poop', 'shucks', 'argh'] # ненормативная лексика

@register.filter(name='preview') 
def preview(value): 
    return value[0:50]+'...   ' 

@register.filter(name='CENSOR') 
def censor(text):
    text_censor = ''
    for word in text.split():
        if word.strip('.,"/') in FILTR_CENS:
            word = '$$'
        text_censor += f' {word}'
    return text_censor 
