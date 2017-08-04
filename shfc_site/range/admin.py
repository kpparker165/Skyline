from range.models import RangeShooting
from django.contrib import admin


# class BoatReservationAdmin(admin.ModelAdmin):
#   fieldsets = [
#     ("Reservation Information",               {'fields': ['boat','person','boat_rental_creation_date' ]}),
#     ("Rental Fees", {'fields': ['boat_rental_fee_half_day','boat_rental_fee_full_day']})
#   ]


class RangShootingAdmin(admin.ModelAdmin):
  fieldsets = [
    ("Shooting Range Page Information",  {'fields': ['range_about','range_pistol','range_100_yard','range_200_300_yard',
    	'range_trap_skeet', ]}),
  ]
  list_display = ( 'id','range_about','range_pistol','range_100_yard','range_200_300_yard',
    	'range_trap_skeet',)
  date_hierarchy = 'creation_date'
  readonly_fields = ("creation_date",)

admin.site.register(RangeShooting, RangShootingAdmin)

# boat_name = models.CharField(max_length=40)
#   boat_desc = models.CharField(max_length=3000)
#   boat_motor = models.CharField(max_length=1000)
#   boat_storage_location = models.CharField(max_length=3000)
#   boat_rental_fee = models.IntegerField(blank=True)
