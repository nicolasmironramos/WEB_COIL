from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_userquery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquery',
            name='llmodel',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userquery',
            name='maxlength',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userquery',
            name='prompt_template',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='userquery',
            name='topk',
            field=models.IntegerField(null=True),
        ),
    ]