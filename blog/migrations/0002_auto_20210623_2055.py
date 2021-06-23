# Generated by Django 3.2.4 on 2021-06-23 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='updated_date',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('random_thoughts', 'Random_thoughts'), ('entertainment', 'Entertainment'), ('life', 'Life'), ('carrer', 'Carrer'), ('travel', 'Travel'), ('business', 'Business')], default='life', max_length=25),
        ),
    ]