from django.db.models.signals import post_save, post_delete, pre_save
from cars.models import Car, CarInventory
from django.dispatch import receiver
from django.db.models import Sum




def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
        )['total_value']
    
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


@receiver(post_save, sender=Car)
def car_postsave(sender, instance, **kwargs):
    car_inventory_update()



@receiver(post_delete, sender=Car)
def car_postsave(sender, instance, **kwargs):
    car_inventory_update()

@receiver(pre_save, sender=Car)
def car_presave(sender, instance, **kwargs):
    if not instance.description:
        instance.description = 'Sem descrição'
    