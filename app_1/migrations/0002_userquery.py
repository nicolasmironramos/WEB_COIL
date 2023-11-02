from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200)),
                ('llmodel', models.CharField(max_length=150)),
                ('maxlength', models.IntegerField()),
                ('topk', models.IntegerField()),
                ('prompt_template', models.CharField(max_length=250)),
                ('reply', models.CharField(max_length=500)),
            ],
        ),
    ]