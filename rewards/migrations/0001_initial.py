# Generated by Django 2.1.3 on 2018-11-06 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('points_remain', models.IntegerField(default=0)),
                ('points_received', models.IntegerField(default=0)),
                ('user_em', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Giftcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('redeem_date', models.DateTimeField(verbose_name='date redeemed')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rewards.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giver', models.CharField(max_length=200)),
                ('points_given', models.IntegerField(default=0)),
                ('message', models.TextField()),
                ('give_date', models.DateTimeField(verbose_name='date of giving')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rewards.Employee')),
            ],
        ),
    ]
