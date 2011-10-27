# -*- coding: utf-8 -*-
# Copyright (C) 2011 Grégoire Détrez
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Person(models.Model):
    
    name = models.CharField(max_length=30, help_text="Full name")
    slug = models.SlugField(primary_key=True,
                            help_text="The slug is used to build the URL. Could be a nickname or a ASCII representation of the name (only lowerase, numbers and hyphen)")
    photo = models.ImageField(upload_to="avatars", blank=True,
                              help_text="Use a square image, prefereably 200px large.")

    # Profile info
    blog = models.URLField(blank=True, verify_exists=False)
    microblog = models.URLField(blank=True, verify_exists=False,
                                help_text="status.net, identi.ca or twitter")
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=30, blank=True,
                                 help_text="Please include the country's prefix")

    micro_biography = models.CharField(max_length=140, blank=True,
                                       help_text="micro = imited to 140 characters.")
    physical_location = models.CharField(max_length=200, blank=True,
                                         help_text="Country or city name")

    biography = models.TextField(blank=True, 
                                 help_text="For speakers' bio. Uses <a href=\"http://en.wikipedia.org/wiki/Markdown\">Markdown</a> syntax")
# <pre>
# =Heading1=
# ==Heading2==
# ===Heading3===

# **bold**     _italic_
# `inline code`

# links: [link text here](link.address.here "link title here")

# * An item in a bulleted (unordered) list
#     * A subitem, indented with 4 spaces
# * Another item in a bulleted list

#     verbatim code block
#     is indeted with
#     at least 4 spaces

# Horizontal rule
# ----


# > "This entire paragraph of text will be enclosed in an HTML blockquote element.
# Blockquote elements are reflowable. You may arbitrarily
# wrap the text to your liking, and it will all be parsed
# into a single blockquote element."
# </pre>
# """)

    # Flags
    staff = models.BooleanField()

    class Meta:
        ordering = ('name', )


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return u"/people/%s/" % self.slug
