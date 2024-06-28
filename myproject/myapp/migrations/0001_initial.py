from django.db import migrations, models
import django.db.models.deletion


def create_initial_data(apps, schema_editor):
    Menu = apps.get_model('myapp', 'Menu')  # 'myapp' kısmını kendi uygulama adınızla değiştirin
    MenuItem = apps.get_model('myapp', 'MenuItem')  # 'myapp' kısmını kendi uygulama adınızla değiştirin

    # Menüyü Oluştur
    menu01 = Menu.objects.create(title='menu01', selected=True)

    # MenuItems Verileri
    menu_items_data = [
        {'title': 'Ana Sayfa', 'order': 1, 'url': '/'},
        {'title': 'Ürünlerimiz', 'order': 2, 'url': '/urunlerimiz', 'slug':'urunlerimiz'},
        {'title': 'Referanslar', 'order': 3, 'url': '/referanslar'},
        {'title': 'Hakkımızda', 'order': 4, 'url': '/hakkimizda'},
        {'title': 'İletişim', 'order': 5, 'url': '/iletisim'},
    ]

    # MenuItems Oluştur
    for item in menu_items_data:
        MenuItem.objects.create(
            title=item['title'],
            url=item['url'],
            order=item['order'],
            menu=menu01,
            durum=True,
            is_removed=False,
            parent=None  # Üst menü elemanı belirtilmemişse None olarak varsayıldı
        )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('selected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255, blank=True, null=True)),
                ('order', models.PositiveIntegerField()),
                ('durum', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                             to='myapp.menuitem')),
            ],
        ),
        migrations.RunPython(create_initial_data),
    ]

