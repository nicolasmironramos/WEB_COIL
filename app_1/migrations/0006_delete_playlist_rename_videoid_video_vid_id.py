from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_playlist_video'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Playlist',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='videoid',
            new_name='vid_id',
        ),
    ]