# Generated by Django 5.2.1 on 2025-05-16 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        help_text="The downloadable file.", upload_to="lesson_files/"
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="Title of the file.", max_length=200),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Order of this content block within the lesson.",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        help_text="The lesson this file content is part of.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="file_content",
                        to="courses.lesson",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "File Content",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="ImageContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="The image file.", upload_to="lesson_images/"
                    ),
                ),
                (
                    "caption",
                    models.CharField(
                        blank=True, help_text="A caption for the image.", max_length=255
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Order of this content block within the lesson.",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        help_text="The lesson this image content is part of.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="image_content",
                        to="courses.lesson",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Image Content",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="TextContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField(help_text="The main text content.")),
                (
                    "order",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Order of this content block within the lesson.",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        help_text="The lesson this text content is part of.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="text_content",
                        to="courses.lesson",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Text Content",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="VideoContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "video_url",
                    models.URLField(
                        help_text="URL of the embedded video (e.g., YouTube link)."
                    ),
                ),
                (
                    "caption",
                    models.CharField(
                        blank=True, help_text="A caption for the video.", max_length=255
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Order of this content block within the lesson.",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        help_text="The lesson this video content is part of.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_content",
                        to="courses.lesson",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Video Content",
                "ordering": ["order"],
            },
        ),
    ]
