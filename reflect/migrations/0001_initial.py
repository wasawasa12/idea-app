# Generated by Django 4.0 on 2022-01-11 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReflectProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.TextField()),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='ReflectIssues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issues', models.CharField(max_length=50)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='ReflectContents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_type', models.CharField(choices=[('Positive', 'ポジティブ'), ('Negative', 'ネガティブ'), ('Conclusion', '結論')], max_length=20)),
                ('comment_content', models.TextField()),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('ref_issues', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reflect.reflectissues')),
            ],
        ),
    ]
