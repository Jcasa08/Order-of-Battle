# Generated manually by Copilot on 2026-01-14
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.add_field(
            model_name='listunit',
            name='unit_size',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
