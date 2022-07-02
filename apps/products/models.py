from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class MeasureUnit(BaseModel):
    description = models.CharField('description', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changeg_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Measure Unit'
        verbose_name_plural = 'Measure Units'

    def __str__(self) -> str:
        return self.description


class CategoryProduct(BaseModel):
    description = models.CharField('description', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changeg_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Category Product'
        verbose_name_plural = 'Category Products'

    def __str__(self) -> str:
        return self.description

class Indicator(BaseModel):
    discount_value = models.PositiveBigIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name= 'Discount indicator')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changeg_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Offert Indicator'
        verbose_name_plural = 'Offert Indicators'

    def __str__(self) -> str:
        return f'Category offert {self.category_product} : {self.discount_value}%'


class Product(BaseModel):
    name = models.CharField('name', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('description', blank=True, null=True)
    image = models.ImageField('product image', upload_to=None, blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='measure units', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categorys', null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changeg_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
