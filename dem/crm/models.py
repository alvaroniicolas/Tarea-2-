from django.db import models


class LocalisationCountry(models.Model):
    name = models.CharField(max_length=144)
    iso_code_2= models.CharField(max_length=2)   
    iso_code_3= models.CharField(max_length=3)
    sort_order= models.IntegerField()
    status = models.IntegerField()
    def __str__(self):
        return self.name 
        
class LocalisationZone(models.Model):
    name = models.CharField(max_length=144)
    code= models.CharField(max_length=32)   
    sort_order= models.IntegerField()
    status = models.IntegerField()
    country_id=models.ForeignKey(LocalisationCountry, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

class LocalisationState(models.Model):
    name = models.CharField(max_length=144)
    sort_order= models.IntegerField()   
    status = models.IntegerField()
    zone_id= models.ForeignKey(LocalisationZone, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 

class GroupClient(models.Model):
    name = models.CharField(max_length=144)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.name 


class Client(models.Model):
    Opcion3 = (
      ('opcion', (
              ('1', 'RUT'),
              ('2', 'DNI'),
          )
      )
    tecnical_contact = models.EmailField(blank=True , max_length=254)
    comercial_contact = models.EmailField(blank=True , max_length=254)
    finance_contact = models.EmailField(blank=True , max_length=254)
    name = models.CharField(max_length=144)
    address_1 = models.CharField(max_length=144)
    business_name = models.CharField(max_length=144)
    identification_type = models.CharField(max_length=144 , choices=Opcion3)
    identification_number = models.CharField(max_length=50)
    group_client = models.ForeignKey(GroupClient, null=False, blank=False, on_delete=models.CASCADE)
    state_id= models.ForeignKey(LocalisationState, null=False, blank=False, on_delete=models.CASCADE)
    country_id=models.ForeignKey(LocalisationCountry, null=False, blank=False, on_delete=models.CASCADE)
    zone_id= models.ForeignKey(LocalisationZone, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Area(models.Model):
    name = models.CharField(max_length=144)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.name 

class ProfitCenter(models.Model):
    name = models.CharField(max_length=144)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.name 

class TypeService(models.Model):
    name = models.CharField(max_length=144)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=144)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)   
    area_id = models.ForeignKey(Area, null=False, blank=False, on_delete=models.CASCADE) 
    profit_center_id= models.ForeignKey(ProfitCenter, null=False, blank=False, on_delete=models.CASCADE)
    type_service_id= models.ForeignKey(TypeService, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ClientService(models.Model):
    Opcion1 = (
      ('opcion', (
              ('1', '8x5'),
              ('2', '24x7'),
          )
      )
    Opcion2 = (
      ('opcion', (
              ('1', 'Definido'),
              ('2', 'Indefinido'),
          )
      )
    type_contract = models.CharField(max_length=50, choices=Opcion2) 
    type_sla = models.CharField(max_length=50, choices=Opcion1)
    pay_day = models.IntegerField()    
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    service_id = models.ForeignKey(Service, null=False, blank=False, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, null=False, blank=False, on_delete=models.CASCADE)
    profit_center_id= models.ForeignKey(ProfitCenter, null=False, blank=False, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.name


