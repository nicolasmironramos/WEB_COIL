from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_alter_userquery_llmodel_alter_userquery_maxlength_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquery',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=600, null=True),
        ),
    ]