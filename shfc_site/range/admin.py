from range.models import ShootingRangeDetail, RSOCalendar
from django.contrib import admin


class RangShootingAdmin(admin.ModelAdmin):
  fieldsets = [
    ("Shooting Range Page Information",  {'fields': ['range_pistol','range_100_yard','range_200_300_yard',
    	'range_trap_skeet', ]}),
  ]
  list_display = ( 'id','range_pistol','range_100_yard','range_200_300_yard',
    	'range_trap_skeet',)
  date_hierarchy = 'creation_date'
  readonly_fields = ("creation_date",)

class RSOCalendarAdmin(admin.ModelAdmin):
  fieldsets = [
    ("Shooting Range Page Information",  {'fields': ['rso_person','rso_start_date','rso_end_date']}),
  ]
  list_display = ( 'id','rso_person','rso_start_date','rso_end_date', 'creation_date')
  date_hierarchy = 'creation_date'
  readonly_fields = ("creation_date",)	
		

admin.site.register(ShootingRangeDetail, RangShootingAdmin)
admin.site.register(RSOCalendar, RSOCalendarAdmin)
