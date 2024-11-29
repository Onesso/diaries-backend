# Generated by Django 5.1.3 on 2024-11-26 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteInfo', '0002_alter_note_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(choices=[('EDUCATION', 'Education'), ('BITCOIN', 'Bitcoin'), ('GAMING', 'Gaming'), ('DATA ENGINEERING', 'Data engineering'), ('TYPESCRIPT', 'Typesript'), ('CYBERSECURITY', 'Cybersecurity'), ('CROSS PLATFORM', 'Cross platform'), ('FRONTEND', 'Frontend'), ('BACKEND', 'Backend'), ('QUANTUM', 'Quantum'), ('MECHANICAL', 'Mechanical'), ('IOT', 'Iot')], default='EDUCATION', max_length=50),
        ),
    ]
