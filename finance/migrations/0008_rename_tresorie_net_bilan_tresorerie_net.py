# Generated by Django 4.2.1 on 2023-06-19 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_bilan_actif_bilan_autonomie_financiere_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bilan',
            old_name='tresorie_net',
            new_name='tresorerie_net',
        ),
    ]
