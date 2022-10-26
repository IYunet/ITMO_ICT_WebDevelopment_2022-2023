# Generated by Django 4.1.1 on 2022-10-25 19:19

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration_user",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("username", models.CharField(max_length=30, verbose_name="Ник")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                ("first_name", models.CharField(max_length=30, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=30, verbose_name="Фамилия")),
                (
                    "passport_number",
                    models.CharField(
                        max_length=30,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Номер паспорта",
                    ),
                ),
                ("password", models.CharField(max_length=300, verbose_name="Пароль")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "number_flight",
                    models.CharField(
                        max_length=30,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Номер рейса",
                    ),
                ),
                ("date", models.DateField(unique=True, verbose_name="Дата вылета")),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "place_in_plane",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("7", "7"),
                            ("8", "8"),
                            ("9", "9"),
                            ("10", "10"),
                            ("11", "11"),
                            ("12", "12"),
                            ("13", "13"),
                            ("14", "14"),
                            ("15", "15"),
                            ("16", "16"),
                            ("17", "17"),
                            ("18", "18"),
                            ("19", "19"),
                            ("20", "20"),
                            ("21", "21"),
                            ("22", "22"),
                            ("23", "23"),
                            ("24", "24"),
                            ("25", "25"),
                            ("26", "26"),
                            ("27", "27"),
                            ("28", "28"),
                            ("29", "29"),
                            ("30", "30"),
                        ],
                        default="-1",
                        max_length=2,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Место",
                    ),
                ),
                (
                    "number_flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tablo.flight"
                    ),
                ),
                (
                    "passport_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("comment", models.TextField(verbose_name="Комментарий")),
                (
                    "rate",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("7", "7"),
                            ("8", "8"),
                            ("9", "9"),
                            ("10", "10"),
                        ],
                        max_length=2,
                        verbose_name="Оценка",
                    ),
                ),
                (
                    "sing_author",
                    models.CharField(max_length=30, verbose_name="Укажите ваш ник"),
                ),
                (
                    "number_flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="number_flight_2",
                        to="tablo.flight",
                    ),
                ),
            ],
        ),
    ]
