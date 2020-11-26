# Python Django Web Framework - Full Course for Beginners

## Coding for Entrepeneurs and freeCodeCamp

### by Justin Mitchel

[YouTube](https://www.youtube.com/watch?v=F5mRW0jo-U4)

1. **Create a new App named blog in the terminal**:

```zsh
python manage.py startapp blog
```

2. **Add 'blog' to your Django project in [settings.py](./src/trydjango/settings.py)**:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # own
    'products',
    'pages',
    'blog',
]
```

3. **Create a Model named Article in blog/models.py**

```python
from django.db import models
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    active = models.BooleanField(default=True)
```

4. **Run migrations**

```zsh
python manage.py makemigrations
  blog/migrations/0001_initial.py
    - Create model Article

python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, products, sessions
Running migrations:
  Applying blog.0001_initial... OK
```

5. **Create a ModelForm for Article**

```python
from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the title"
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter the description",
                "class": "html-new-class-name html-another-class",
                "id": "html-id",
                "rows": 20,
                "cols": 60
            }
        )
    )
    active = forms.BooleanField(initial=True)

    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'active',
        ]

```

6. **Create _article_list.html_ and _article_detail.html_ Template**

- article_list

```html
{% extends 'base.html' %} {% block content %} {% for instance in object_list %}
<p>
  {{ instance.id }} -
  <a href="{{ instance.get_absolute_url }}">{{ instance.title }}</a>
</p>
{% endfor %} {% endblock %}
```

- article_detail

```html
{% extends 'base.html' %} {% block content %}
<h1>Item</h1>
<p>(In App template) Item: {{ object.title }}</p>
<p>
  Description: {% if object.description %} {{ object.description }} {% else %}
  Description coming soon {% endif %}
</p>
<p>Active: {{ object.active }}</p>
{% endblock %}
```

7. **Add Article Model to the Admin**

- blog/admin.py:

```python
from django.contrib import admin

# Register your models here.
from .models import Article

admin.site.register(Article)
```

8. **Save a new Article object in the admin**

[Confused?](https://kirr.co/9ypik6)
