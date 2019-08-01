from django.contrib import admin
from jet.admin import CompactInline

from people.models import Staff, HoldingTeam, Speaker, TechnicalExpert, Role, StudentApplication


class StaffInline(CompactInline):
    model = Staff
    extra = 0


class HoldingTeamInline(CompactInline):
    model = HoldingTeam
    extra = 0


class HoldingTeamAdmin(admin.ModelAdmin):
    filter_vertical = ('staff',)
    list_display = ('__str__', 'wss')
    list_filter = ('wss__year',)


class StudentApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]


admin.site.register(Role)
admin.site.register(TechnicalExpert)
admin.site.register(HoldingTeam, HoldingTeamAdmin)
admin.site.register(Staff)
admin.site.register(Speaker)
admin.site.register(StudentApplication, StudentApplicationAdmin)
