from django.db import models

class Equipment(models.Model):
  # eq_type
  BOOK = 1
  DEVICE = 2
  COMPUTER = 3

  # state
  NOT_ON_LOAN = 0
  ON_LOAN = 1
  
  name = models.CharField(max_length=50)
  eq_type = models.IntegerField()
  owner = models.CharField(max_length=20)
  state = models.IntegerField()
  due = models.DateField(auto_now = False, auto_now_add = False)
  borrower = models.CharField(max_length=20)
  remark = models.TextField()

  def __str__(self):
    return self.name