# Generated by Django 3.0.8 on 2020-08-04 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20200729_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
    ]
