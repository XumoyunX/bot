from django.db import models



class Region(models.Model):
    name_uz = models.CharField(max_length=250)
    name_ru = models.CharField(max_length=250)

    def __str__(self):
        return self.name_uz




class District(models.Model):
    region = models.ForeignKey(Region, null=True, on_delete=models.CASCADE, related_name='data')
    name_uz = models.CharField(max_length=250)
    name_ru = models.CharField(max_length=250)    


    def __str__(self):
        return self.name_uz
    






class Post(models.Model):
    user = models.ForeignKey('clinet.User', null=True, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    district = models.ForeignKey(District, null=True, on_delete=models.SET_NULL, related_name='data')
    img = models.ImageField(upload_to="images/")
    text_uz = models.TextField()
    text_ru = models.TextField()
    number = models.CharField(max_length=250)
    vaqt = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    maydon_soni = models.IntegerField()
    longtitude = models.FloatField()
    latitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):

        return self.text_uz
    


    





