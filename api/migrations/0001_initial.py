# Generated by Django 3.1.7 on 2023-04-30 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=16)),
                ('book_name_abbrev', models.CharField(max_length=3)),
                ('book_num_chapters', models.IntegerField()),
                ('book_num_verses', models.IntegerField()),
                ('book_num_words', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chap',
            fields=[
                ('chap_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('chap_num_verses', models.IntegerField()),
                ('chap_num_words', models.IntegerField()),
                ('chap_num', models.IntegerField()),
                ('chap_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chap', to='api.book')),
            ],
        ),
        migrations.CreateModel(
            name='Gnt',
            fields=[
                ('word_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('word_greek', models.CharField(blank=True, max_length=36, null=True)),
                ('word_english', models.CharField(blank=True, max_length=36, null=True)),
                ('word_greek_punc', models.CharField(blank=True, max_length=2, null=True)),
                ('word_english_punc', models.CharField(blank=True, max_length=2, null=True)),
                ('word_book_name_abbrev', models.CharField(max_length=3)),
                ('word_chap_num', models.IntegerField()),
                ('word_vers_num', models.IntegerField()),
                ('word_word_num', models.IntegerField()),
                ('vers_id', models.CharField(blank=True, max_length=6, null=True)),
                ('vers_ref', models.CharField(max_length=22)),
                ('vers_ref_abbrev', models.CharField(max_length=10)),
                ('vers_chap_url', models.CharField(max_length=14)),
                ('vers_book_name_abbrev', models.CharField(max_length=3)),
                ('vers_chap_num', models.IntegerField()),
                ('vers_num', models.IntegerField()),
                ('vers_num_words', models.IntegerField()),
                ('chap_id', models.CharField(blank=True, max_length=4, null=True)),
                ('chap_num_verses', models.IntegerField()),
                ('chap_num_words', models.IntegerField()),
                ('chap_num', models.IntegerField()),
                ('book_id', models.CharField(blank=True, max_length=2, null=True)),
                ('book_name', models.CharField(max_length=16)),
                ('book_name_abbrev', models.CharField(max_length=3)),
                ('book_num_chapters', models.IntegerField()),
                ('book_num_verses', models.IntegerField()),
                ('book_num_words', models.IntegerField()),
                ('pars_id', models.CharField(blank=True, max_length=10, null=True)),
                ('pars_function', models.CharField(blank=True, max_length=5, null=True)),
                ('pars_tense', models.CharField(blank=True, max_length=2, null=True)),
                ('pars_voice', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_mood', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_person', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_case', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_gender', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_number', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_freq_nt', models.IntegerField(default=0)),
                ('pars_rank', models.IntegerField()),
                ('lexn_id', models.CharField(blank=True, max_length=4, null=True)),
                ('lexn_greek', models.CharField(blank=True, max_length=32, null=True)),
                ('lexn_greek_long', models.CharField(blank=True, max_length=64, null=True)),
                ('lexn_transliteration', models.CharField(blank=True, max_length=36, null=True)),
                ('lexn_gloss', models.CharField(blank=True, max_length=32, null=True)),
                ('lexn_definition', models.CharField(blank=True, max_length=128, null=True)),
                ('lexn_usage', models.CharField(blank=True, max_length=256, null=True)),
                ('lexn_strongs', models.CharField(max_length=6)),
                ('lexn_function', models.CharField(blank=True, max_length=5, null=True)),
                ('lexn_freq_nt', models.IntegerField(default=0)),
                ('pdgm_id', models.CharField(blank=True, max_length=15, null=True)),
                ('pdgm_greek', models.CharField(blank=True, max_length=36, null=True)),
                ('pdgm_freq_nt', models.IntegerField(default=0)),
                ('frlc_id', models.CharField(blank=True, max_length=7, null=True)),
                ('frlc_book_name_abbrev', models.CharField(max_length=3)),
                ('frlc_chap_num', models.IntegerField()),
                ('frlc_count', models.IntegerField()),
                ('frlb_id', models.CharField(blank=True, max_length=7, null=True)),
                ('frlb_book_name_abbrev', models.CharField(max_length=3)),
                ('frlb_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lexn',
            fields=[
                ('lexn_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('lexn_greek', models.CharField(blank=True, max_length=32, null=True)),
                ('lexn_greek_long', models.CharField(blank=True, max_length=64, null=True)),
                ('lexn_transliteration', models.CharField(blank=True, max_length=36, null=True)),
                ('lexn_gloss', models.CharField(blank=True, max_length=32, null=True)),
                ('lexn_definition', models.CharField(blank=True, max_length=128, null=True)),
                ('lexn_usage', models.CharField(blank=True, max_length=256, null=True)),
                ('lexn_strongs', models.CharField(max_length=6)),
                ('lexn_function', models.CharField(blank=True, max_length=5, null=True)),
                ('lexn_freq_nt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pars',
            fields=[
                ('pars_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pars_function', models.CharField(blank=True, max_length=5, null=True)),
                ('pars_tense', models.CharField(blank=True, max_length=2, null=True)),
                ('pars_voice', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_mood', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_person', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_case', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_gender', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_number', models.CharField(blank=True, max_length=1, null=True)),
                ('pars_freq_nt', models.IntegerField(default=0)),
                ('pars_rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vers',
            fields=[
                ('vers_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('vers_ref', models.CharField(max_length=22)),
                ('vers_ref_abbrev', models.CharField(max_length=10)),
                ('vers_chap_url', models.CharField(max_length=14)),
                ('vers_book_name_abbrev', models.CharField(max_length=3)),
                ('vers_chap_num', models.IntegerField()),
                ('vers_num', models.IntegerField()),
                ('vers_num_words', models.IntegerField()),
                ('vers_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vers', to='api.book')),
                ('vers_chap', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vers', to='api.chap')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('word_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('word_greek', models.CharField(blank=True, max_length=36, null=True)),
                ('word_english', models.CharField(blank=True, max_length=36, null=True)),
                ('word_greek_punc', models.CharField(blank=True, max_length=2, null=True)),
                ('word_english_punc', models.CharField(blank=True, max_length=2, null=True)),
                ('word_book_name_abbrev', models.CharField(max_length=3)),
                ('word_chap_num', models.IntegerField()),
                ('word_vers_num', models.IntegerField()),
                ('word_word_num', models.IntegerField()),
                ('word_lexn_id_copy', models.CharField(blank=True, max_length=4, null=True)),
                ('word_pars_id_copy', models.CharField(blank=True, max_length=10, null=True)),
                ('word_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='word', to='api.book')),
                ('word_chap', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='word', to='api.chap')),
                ('word_lexn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='word', to='api.lexn')),
                ('word_pars', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='word', to='api.pars')),
                ('word_vers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='word', to='api.vers')),
            ],
        ),
        migrations.CreateModel(
            name='Pdgm',
            fields=[
                ('pdgm_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('pdgm_greek', models.CharField(blank=True, max_length=36, null=True)),
                ('pdgm_freq_nt', models.IntegerField(default=0)),
                ('pdgm_lexn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pdgm', to='api.lexn')),
                ('pdgm_pars', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pdgm', to='api.pars')),
            ],
        ),
    ]
