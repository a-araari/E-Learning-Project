# Generated by Django 3.0.3 on 2020-03-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='User full name', max_length=30, null=True)),
                ('from_email', models.EmailField(help_text='Email address (required)', max_length=254)),
                ('subject', models.CharField(blank=True, choices=[('sp', 'Site problem'), ('aa', 'An advice')], default='sp', help_text='Contact subject', max_length=5, null=True)),
                ('content', models.TextField(help_text='Contact content (required)')),
                ('date', models.DateField(auto_now_add=True)),
                ('reviewed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
