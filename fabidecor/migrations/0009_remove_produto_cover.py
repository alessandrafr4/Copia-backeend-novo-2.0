# Generated by Django 4.2.5 on 2023-10-03 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabidecor', '0008_remove_produto_imagens_produto_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='cover',
        ),
    ]