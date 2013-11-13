### Description goes here

### Installation

Install via pip:

```
pip install git+ssh://git@bitbucket.org/ivoscc/django_countrymodel.git
```

Add countrymodel to your installed apps

```
INSTALLED_APPS = (
    ...
    'countrymodel',
    ...
)
```

Create the database table:

```
python manage.py migrate countrymodel
```

Optionally load all the countries into your DB:

```
python manage.py load_all_countries
```

### Usage

```
from countrymodel import CountryMode

class MyCoolModel(models.Model):
    countries = models.ManyToManyField(Countrymode)
```
