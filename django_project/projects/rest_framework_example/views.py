from django.shortcuts import render

# Create your views here.

"""
python manage.py shell
>>> from rest_framework_example.models import Article
>>> from rest_framework_example.serializers import ArticleSerializers
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import  JSONParser

# We are going to serialized model instance 
>>> a = Article(title="Article Title", auther="Rohit", email="rohitpandey5491@gmail.com")
a.save() # it will call create method 
serializer = ArticleSerializers(a)
print(serializer)
print(serializer.data) # dict: {'title': 'Article Title', 'author': 'Rohit', 'email': 'rohitpandey5491@gmail.com', 'date': '2021-06-15T02:57:41.855222Z'}
content = JSONRenderer().render(serializer.data)
print(content) # json: b'{"title":"Article Title","author":"Rohit","email":"rohitpandey5491@gmail.com","date":"2021-06-15T02:57:41.855222Z"}'

# Now we are going to serialized query sets
serializer = ArticleSerializers(Article.objects.all(), many=True)
[OrderedDict([('title', 'Article Title'), ('author', 'Rohit'), ('email', 'rohitpandey5491@gmail.com'), ('date', '2021-06-15T02:57:41.855222Z')])]
"""
