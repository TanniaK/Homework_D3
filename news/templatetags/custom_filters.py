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

@register.filter(name='update_page')
def update_page(full_path:str, page:int):
    try:
        params_list = full_path.split('?')[1].split('&')
        params = dict([tuple(str(param).split('=')) for param  in params_list])
        params.update({'page' : page})
        link = ''
        for key, value in params.items():
            link += (f"{key}={value}&")
        return link[:-1]
    except:
        return f"page={page}"