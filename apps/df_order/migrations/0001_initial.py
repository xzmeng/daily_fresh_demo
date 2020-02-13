# Generated by Django 2.0.7 on 2020-02-13 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='商品价格')),
                ('count', models.IntegerField(verbose_name='商品数')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsInfo', verbose_name='商品')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='大订单号')),
                ('odate', models.DateTimeField(auto_now=True, verbose_name='时间')),
                ('oIsPay', models.BooleanField(default=False, verbose_name='是否支付')),
                ('ototal', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='总价')),
                ('oaddress', models.CharField(max_length=150, verbose_name='订单地址')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.UserInfo', verbose_name='订单用户')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_order.OrderInfo', verbose_name='订单'),
        ),
    ]
