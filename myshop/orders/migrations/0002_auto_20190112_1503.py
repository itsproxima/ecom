# Generated by Django 2.0.7 on 2019-01-12 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('products', '0002_products'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=500)),
                ('cart_total_price', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(max_length=100)),
                ('shipping_address', models.CharField(max_length=500)),
                ('total_price', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('placed_date', models.DateTimeField(auto_now_add=True)),
                ('order_status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order_status')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orders'),
        ),
        migrations.AddField(
            model_name='cart',
            name='order_status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order_status'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
    ]