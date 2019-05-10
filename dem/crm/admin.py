from django.contrib import admin
from crm.models import Client , GroupClient , Area , ProfitCenter, Service, ClientService, TypeService, LocalisationCountry, LocalisationZone, LocalisationState

@admin.register(Client, GroupClient, Area, ProfitCenter , Service, ClientService, TypeService, LocalisationCountry, LocalisationZone, LocalisationState )

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('tecnical_contact','comercial_contact' , 'finance_contact','name','address_1','business_name','identification_type', 'identification_number','group_client','state_id','country_id','zone_id','created_at','modified_at')
    pass

class GroupClienteAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','modified_at')
    pass

class AreaAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','modified_at')
    pass

class ProfitCenterAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','modified_at')
    pass

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','modified_at', 'comment', 'area_id', 'profit_center_id', 'type_service_id' )
    pass

class ClienteServiceAdmin(admin.ModelAdmin):
    list_display = ('type_contract','type_sla','pay_day',' amount ', 'servide_id client_id ', 'profit_center_id' ,'start_date ', 'end_date')
    list_filter  = ('type_sla','type_contract','service_id')
    pass

class TypeServiceAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','modified_at', 'comment', 'area_id', 'profit_center_id', 'type_service_id' )
    pass

class LocalisationCountryAdmin(admin.ModelAdmin):
    list_display = ('name' ,'iso_code_2','iso_code_3','stort_order','status')
    pass

class LocalisationZoneAdmin(admin.ModelAdmin):
    list_display = ('name' ,'code','sort_order','status','country_id')
    pass

class LocalisationStateAdmin(admin.ModelAdmin):
     list_display = ('name' ,'sort_order','status','zone_id')
    pass