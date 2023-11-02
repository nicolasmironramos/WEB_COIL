from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0006_delete_playlist_rename_videoid_video_vid_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=200)),
                ('playlist_url', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='plist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.playlist'),
        ),
    ]