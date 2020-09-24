# Generated by Django 3.1.1 on 2020-09-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_paymentcode_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentcode',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='paymentcode',
            name='lastname',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]