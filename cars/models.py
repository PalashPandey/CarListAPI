from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGAUGE_CHOICE = sorted([(item[1][0] , item[0] for item in LEXERS )])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# CAR_MAKES = ['Honda', 'Ford' , 'Tesla'] 
# CAR_MODELS = ['C']

class CarMaker(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Car_Maker"
        verbose_name_plural = "Car_Makerzzzz"

    def __str__(self):
        return self.name

class Cars(models.Model):
    car_model_name = models.CharField(max_length = 100)
    car_make_year = models.IntegerField()
    # car_mileage = models.FloatField()
    car_maker_name = models.ForeignKey(CarMaker)
 
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Carzzz'

    def __str__(self):
        return str(self.car_maker_name) + ' '  + str(self.car_model_name ) + ' ' +  str( self.car_make_year) 
