from django.contrib import admin
from .models import Portfolio, Blog, Comment, Reply, Category, SlideImage, PaymentCode
# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'slug',
    )
    prepopulated_fields = {'slug': ('project_name',)}

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.prepopulated_fields = {}
            return self.readonly_fields + ('slug',)
        return self.readonly_fields


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Category)
admin.site.register(SlideImage)
admin.site.register(PaymentCode)
