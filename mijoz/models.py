from django.db import models

class Mijoz(models.Model):

    Viloyatlar = (
            ('Andijon', 'Andijon'), ('Buxoro', 'Buxoro'), (
             'Farg`ona', 'Farg`ona'), ('Jizzax', 'Jizzax'), ('Namangan', 'Namangan'), ('Navoiy', 'Navoiy'), (
             'Qashqadaryo', 'Qashqadaryo'), ('Qoraqalpogʻiston', 'Qoraqalpogʻiston'), ('Samarqand', 'Samarqand'), (
             'Sirdaryo', 'Sirdaryo'), ('Surxondaryo', 'Surxondaryo'), ('Toshkent', 'Toshkent'), (
             'Toshkent viloyati', 'Toshkent viloyati'), ('Xorazm', 'Xorazm')

)

    ism = models.CharField(max_length=20)
    telefon = models.CharField(max_length=14)
    citi = models.CharField(max_length=40,choices=Viloyatlar,null=True,blank=True)
    status = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f'{self.ism}({self.telefon}) {self.status}'
