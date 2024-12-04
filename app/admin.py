from .models import *




from django.contrib import admin
class meAdmin(admin.ModelAdmin):
    list_display = ('img', 'nomi', 'mualif', 'asar','file')  # Displaying file in the list view


admin.site.register(KopSotilganKitob,meAdmin)
admin.site.register(kun_iqtibos)
admin.site.register(Kitob,meAdmin)