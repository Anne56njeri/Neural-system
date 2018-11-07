from django.db import models

# Create your models here.
class Stock:
    def __init__(self,open,close,volume):
        self.open=open
        self.close=close
        self.volume=volume
    
