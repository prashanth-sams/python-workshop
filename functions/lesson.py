
def keyword_check(kwargs):
    kc = {}
    if 'index' in kwargs: kc['index'] = 'elements'
    if 'index' not in kwargs: kc['index'] = 'element'
    return "".join(kc.values())


def xfunc(**kwargs):
    print(keyword_check(kwargs))


xfunc(index=2, inaasddex=3)