from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0007_playlist_video_plist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlistvideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.playlist')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.video')),
            ],
        ),
    ]