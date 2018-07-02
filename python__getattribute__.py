class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)

>>> import javascriptobject
>>> jso = javascriptobject.JavaScriptObject
>>> jso = javascriptobject.JavaScriptObject({'name': 'Andreza'})
>>> jso
{'name': 'Andreza'}
>>> jso.language = 'Python'
>>> jso.name
'Andreza'
>>> jso.language
'Python'