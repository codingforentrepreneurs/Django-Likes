import datetime
import math
import re
import random
import string

from django.utils.text import slugify
from django.utils.html import strip_tags


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """
    Source: https://www.codingforentrepreneurs.com/blog/random-string-generator-in-python/
    """
    return ''.join(random.choice(chars) for _ in range(size))



def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    Source: https://www.codingforentrepreneurs.com/blog/a-unique-slug-generator-for-django/
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug



def count_words(html_string):
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    return count


def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count/200.0) #assuming 200wpm reading
    return int(read_time_min)