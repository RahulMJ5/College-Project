# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class UserRegistration(models.Model):
                usersno=models.CharField(max_length=30)
                username=models.CharField(max_length=30)
                password=models.CharField(max_length=30)
                contact=models.CharField(max_length=30)
                emailid=models.CharField(max_length=30)
                
class CompanySales(models.Model):
                Companyname=models.CharField(max_length=30)
                OneYearRevenue=models.CharField(max_length=30)
                TwoYearRevenue=models.CharField(max_length=30)

                def _str_(self):
                                return self.Companyname+ ':' + self.OneYearRevenue+ ':' + self.TwoYearRevenue
                                
                
