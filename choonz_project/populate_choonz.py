import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'choonz_project.settings')

import django
django.setup()
from choonz.models import Playlist, Page

def populate():
    # Create a list of dictionaries containing pages to add to each Playlist
    # Then create dictionaries for our categories
    # This allows us to iterate through each data structure and add data to out models

    python_pages = [
        {
            "title": "Official Python Tutorial",
            "url": "http://docs.python.org/3/tutorial",
            "views": 15,
        },
        {
            "title": "How to Think like a Computer Scientist",
            "url": "http://www.greenteapress.com/thinkpython/",
            "views": 18,
        },
        {
            "title": "Learn Python in 10 Minutes",
            "url": "http://www.korokithakis.net/tutorials/python/",
            "views": 9,
        }
    ]

    django_pages = [
        {
            "title": "Official Django Tutorial",
            "url": "https://docs.djangoproject.com/en/2.1/intro/tutorial01/",
            "views": 14,
        },
        {
            "title":"Django Rocks",
            "url":"http://www.djangorocks.com/",
            "views": 20,
        },
        {
            "title":"How to Tango with Django",
            "url":"http://www.tangowithdjango.com/",
            "views": 6,
        }
    ]

    other_pages = [
        {
            "title":"Bottle",
            "url":"http://bottlepy.org/docs/dev/",
            "views": 19,
        },
        {
            "title":"Flask",
            "url":"http://flask.pocoo.org",
            "views": 11,
        }
    ]

    cats = {
        "Python": {"pages": python_pages, "views": 128, "likes": 64},
        "Django": {"pages": django_pages, "views": 64, "likes": 32},
        "Other Frameworks": {"pages": other_pages,  "views": 32, "likes": 16},
        "Pascal": {"pages": [], "views": 0, "likes": 0},
        "Perl": {"pages": [], "views": 0, "likes": 0},
        "PHP": {"pages": [], "views": 0, "likes": 0},
        "Prolog": {"pages": [], "views": 0, "likes": 0},
        "PostScript": {"pages": [], "views": 0, "likes": 0},
        "Programming": {"pages": [], "views": 0, "likes": 0},
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    for c in Playlist.objects.all():
        for p in Page.objects.filter(Playlist=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(Playlist=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Playlist.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print("Starting choonz population script...")
    populate()

