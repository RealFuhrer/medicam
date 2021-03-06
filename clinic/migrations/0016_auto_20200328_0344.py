# Generated by Django 3.0.4 on 2020-03-28 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0015_doctor_verification_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='verification_problem',
            field=models.PositiveIntegerField(choices=[(0, 'N/A'), (2, 'Submitted an unacceptable credential'), (3, 'Fake or malicious submission'), (4, 'Other')], default=0, help_text='Set this if the provider cannot be approved.', verbose_name='reason for non-approval'),
        ),
    ]
