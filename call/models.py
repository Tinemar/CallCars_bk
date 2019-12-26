from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Orders(models.Model):
    order_id = models.CharField(max_length=128,null=False,default='',verbose_name='订单编号')
    order_user = models.ForeignKey(User,verbose_name='行程单用户',default='',on_delete=models.SET_DEFAULT)
    start_palce = models.CharField(max_length=500,null=False,default='',verbose_name="出发地")
    end_place = models.CharField(max_length=500,null=False,default='',verbose_name="目的地")
    start_time = models.DateTimeField('行程开始时间',null=False)
    end_time = models.DateTimeField('行程结束时间',null=False)
    status = models.IntegerField('状态',default=0,choices=((0,'未派单'),(1,'行程中'),(2,'行程结束')))
