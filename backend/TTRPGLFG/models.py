# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order (DONE)
#   * Make sure each model has one field with primary_key=True (I hope this is done automatically)
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior (DONE)
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table (DONE)
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    username = models.CharField(unique=True, max_length=30)
    profilepicture = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=600, blank=True, null=True)
    candm = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class Game(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'game'


class Group(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=600, blank=True, null=True)
    location = models.CharField(max_length=45)
    isopen = models.BooleanField()
    languages = models.CharField(max_length=45, blank=True, null=True)
    maxsize = models.IntegerField()
    dmneeded = models.BooleanField()
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='gameid')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'group'


class Application(models.Model):
    applicantid = models.ForeignKey('User', models.CASCADE, db_column='applicantid')
    groupid = models.ForeignKey('Group', models.CASCADE, db_column='groupid')
    description = models.CharField(max_length=600, blank=True, null=True)

    def __str__(self):
        return f'{self.applicantid} -> {self.groupid}'

    class Meta:
        db_table = 'application'


class Belongsto(models.Model):
    userid = models.ForeignKey('User', models.CASCADE, db_column='userid')
    groupid = models.ForeignKey('Group', models.CASCADE, db_column='groupid')
    isowner = models.BooleanField()
    isdm = models.BooleanField(default=False)
    nickname = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.userid} -> {self.groupid} ({self.nickname})'

    class Meta:
        db_table = 'belongsto'


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'


class Grouptag(models.Model):
    groupid = models.ForeignKey(Group, models.CASCADE, db_column='groupid')
    tagid = models.ForeignKey('Tag', models.CASCADE, db_column='tagid')

    def __str__(self):
        return f'{self.groupid}, {self.tagid}'

    class Meta:
        db_table = 'grouptag'


class Schedule(models.Model):
    userid = models.ForeignKey('User', models.CASCADE, db_column='userid')
    day = models.CharField(max_length=2)
    starttime = models.TimeField()
    endtime = models.TimeField()

    def __str__(self):
        return f'{self.userid}, {self.day}, {self.starttime} - {self.endtime}'

    class Meta:
        db_table = 'schedule'


class Session(models.Model):
    groupid = models.ForeignKey(Group, models.CASCADE, db_column='groupid')
    num = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=600, blank=True, null=True)
    starttime = models.DateTimeField()
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.groupid}, {self.num}'

    class Meta:
        db_table = 'session'


class Usertag(models.Model):
    userid = models.ForeignKey(User, models.CASCADE, db_column='userid')
    tagid = models.ForeignKey(Tag, models.CASCADE, db_column='tagid')
    islooking = models.BooleanField()

    def __str__(self):
        return f'{self.userid}, {self.tagid}'

    class Meta:
        db_table = 'usertag'

class Chat(models.Model):
    class chatTypes(models.TextChoices):
        APPLICATION = 'APP', _('application')
        GROUP = 'GRP', _('group')

    applicationid = models.ForeignKey(Application, models.CASCADE, db_column='applicationid', null=True)
    groupid = models.ForeignKey(Group, models.CASCADE, db_column='groupid', null=True)
    chattype = models.CharField(max_length=3,choices=chatTypes.choices, default=chatTypes.APPLICATION)

class Chatmessage(models.Model):
    class chatMessageTypes(models.TextChoices):
        TEXT = 'TXT', _('text')
        SCHEDULE = 'SCD', _('schedule')
        PREFS = 'PRF', _('prefs')
    
    chatid = models.ForeignKey(Chat, models.CASCADE, db_column='chatid')
    userid = models.ForeignKey(User, models.CASCADE, db_column='userid')
    timestamp = models.DateTimeField(null=False)
    chatmessagetype = models.CharField(max_length=3, choices=chatMessageTypes.choices, default=chatMessageTypes.TEXT)
    content = models.CharField(max_length=600, null=False)


