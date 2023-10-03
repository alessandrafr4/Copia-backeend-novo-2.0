# Generated by Django 4.2.5 on 2023-10-03 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('fabidecor', '0007_produto_imagens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='imagens',
        ),
        migrations.AddField(
            model_name='produto',
            name='cover',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='uploader.image'),
            preserve_default=False,
        ),
    ]
