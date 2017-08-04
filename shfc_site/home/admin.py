from home.models import Home
from django.contrib import admin


# class BoatReservationAdmin(admin.ModelAdmin):
#   fieldsets = [
#     ("Reservation Information",               {'fields': ['boat','person','boat_rental_creation_date' ]}),
#     ("Rental Fees", {'fields': ['boat_rental_fee_half_day','boat_rental_fee_full_day']})
#   ]

class HomeAdmin(admin.ModelAdmin):
  fieldsets = [
    ("Home Page Information",  {'fields': ['about','facilities','general',
    	'presidents_word', ]}),
  ]
  list_display = ( 'about','facilities','general',
      'presidents_word',)
  date_hierarchy = 'creation_date'
  readonly_fields = ("creation_date",)

admin.site.register(Home, HomeAdmin)

# boat_name = models.CharField(max_length=40)
#   boat_desc = models.CharField(max_length=3000)
#   boat_motor = models.CharField(max_length=1000)
#   boat_storage_location = models.CharField(max_length=3000)
#   boat_rental_fee = models.IntegerField(blank=True)
