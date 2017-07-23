from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User





class masterUser(models.Model):
		username = models.IntegerField(db_column='ID')
		firstname = models.TextField()
		lastname = models.TextField()
		location = models.TextField()
		govermentID = models.TextField()
		email_address = models.TextField()
		phone_number = models.TextField()
		work_email = models.TextField()
        def __unicode__(self):
            return self.username

class Tesr(models.Model):
    rererere = models.BigIntegerField(blank=True, null=True)
    location = models.TextField()

    class Meta:
        managed = False
        db_table = 'tesr'


# class NewsSources(models.Model):
#     id = models.IntegerField(db_column='ID')  # Field name made lowercase.
#     name = models.TextField(primary_key=True)
#     description = models.TextField()
#     urls = models.TextField()
#     category = models.TextField()
#     language = models.TextField()
#     country = models.TextField()
#     alltext = models.TextField()

#     class Meta:
#         managed = False
#         db_table = 'News_sources'

# class NewsSourcesLatest(models.Model):
#     id = models.IntegerField(db_column='ID')  # Field name made lowercase.
#     author = models.TextField()
#     title = models.TextField()
#     description = models.TextField()
#     url = models.TextField()
#     urltoimage = models.TextField(db_column='urlToImage')  # Field name made lowercase.
#     publishedat = models.TextField(db_column='publishedAt')  # Field name made lowercase.
#     pkey = models.TextField(db_column='PKEY', primary_key=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'News_sources_latest'


# class LocationlistReal(models.Model):
#     id = models.IntegerField(db_column='ID')  # Field name made lowercase.
#     country = models.TextField()
#     city = models.TextField()
#     location = models.TextField()
#     pk_cocity = models.TextField(db_column='PK_cocity', primary_key=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'locationList_real'


# class BooksMaster(models.Model):
#     id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     nameshort = models.TextField(db_column='NameShort')  # Field name made lowercase.
#     fullname = models.TextField(db_column='FullName')  # Field name made lowercase.
#     published = models.TextField()
#     comments = models.TextField(db_column='Comments')  # Field name made lowercase.
#     other_locations = models.TextField(db_column='Other Locations')  # Field name made lowercase. Field renamed to remove unsuitable characters.

#     class Meta:
#         managed = False
#         db_table = 'books_master'


# class UserProfile(models.Model):
#     # This line is required. Links UserProfile to a User model instance.
#     user = models.OneToOneField(User)

#     # The additional attributes we wish to include.
#     website = models.URLField(blank=True)
#     picture = models.ImageField(upload_to='profile_images', blank=True)

#     # Override the __unicode__() method to return out something meaningful!
#     def __unicode__(self):
#         return self.user.username