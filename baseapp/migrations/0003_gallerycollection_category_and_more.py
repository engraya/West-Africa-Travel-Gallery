# Generated by Django 4.1.3 on 2023-07-01 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_alter_country_about_alter_country_capital_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerycollection',
            name='category',
            field=models.CharField(blank=True, choices=[('Nigeria', 'Nigeria'), ('Niger', 'Niger'), ('Ghana', 'Ghana'), ('Gambia', 'Gambia'), ('Sierra Leone', 'Sierra Leone'), ('Togo', 'Togo'), ('Benin Republic', 'Benin Republic'), ('Mali', 'Mali'), ('Senegal', 'Senegal'), ('Guinea', 'Guinea'), ('Mauritania', 'Mauritania'), ('Ivory Coast', 'Ivory Coast'), ('Liberia', 'Liberia'), ('Guinea Bissau', 'Guinea Bissau'), ('Burkina Faso', 'Burkina Faso')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gallerycollection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='baseapp.country')),
            ],
        ),
    ]