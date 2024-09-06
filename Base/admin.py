from django.contrib import admin
from .models import *
from .resource import(
    TopicResource,
    CategoryResource,
    IndicatorResource
)


from import_export.admin import ImportExportModelAdmin

class TopicAdmin(ImportExportModelAdmin):
    resource_classes = [TopicResource]
    list_display = ('title_ENG', 'title_AMH', 'created')

admin.site.register(Topic, TopicAdmin)


class CategoryAdmin(ImportExportModelAdmin):
    resource_classes = [CategoryResource]
    list_display = ('name_ENG', 'name_AMH', 'topic', 'is_dashboard_visible', 'is_deleted')
    search_fields = ['name_ENG', 'name_AMH', 'topic__title_ENG']

admin.site.register(Category, CategoryAdmin)


class IndicatorAdmin(ImportExportModelAdmin):
    resource_classes = [IndicatorResource]
    list_display = ('title_ENG', 'title_AMH', 'kpi_characteristics', 'is_dashboard_visible', 'is_public')
    filter_horizontal = ('for_category', )

admin.site.register(Indicator, IndicatorAdmin)