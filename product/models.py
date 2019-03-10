from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
          return self.name

    class Meta:
        abstract = False   
        # app_label
        db_table = "product"
        # db_tablespace
        # default_related_name
        # get_latest_by
        # managed
        # order_with_respect_to
        # ordering
        # permissions
        # default_permissions
        # proxy
        # select_on_save
        # unique_together      设定组合在一起时必须唯一的多个字段名称
        # index_together       索引的
        # verbose_name            可读名称（单数）
        # verbose_name_plural     可读名称（复数）