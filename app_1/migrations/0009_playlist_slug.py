from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0008_playlistvideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=250, null=True),
        ),
    ]