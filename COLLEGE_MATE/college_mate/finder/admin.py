# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from finder.models import Post,FinderStatus,FinderStatus2
# Register your models here.
admin.site.register(Post)
admin.site.register(FinderStatus)
admin.site.register(FinderStatus2)
