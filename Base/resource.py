from import_export import resources, fields
import datetime
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from .models import (
    Topic,
    Category,
    Indicator,
)
class TopicResource(resources.ModelResource):

    class Meta:
        model = Topic
        skip_unchanged = True
        report_skipped = True
        exclude = ( 'id', 'updated', 'created', 'is_deleted', 'rank', 'icon', 'is_dashboard')
        import_id_fields = ('title_ENG', 'title_AMH')


class CategoryResource(resources.ModelResource):
    topic = fields.Field(
        column_name='topic',
        attribute='topic',
        widget=ForeignKeyWidget(Topic, field='title_ENG'),
        saves_null_values = True,
        )


    def before_import_row(self, row, **kwargs):
            if row.get('topic') is None:
               pass
            else :
               topic_name = row["topic"]
               Topic.objects.get_or_create(title_ENG=topic_name, defaults={"title_ENG": topic_name, "title_AMH":topic_name})
    
    class Meta:
        model = Category
        report_skipped = True
        skip_unchanged = True
        exclude = ( 'id', 'created_at', 'is_deleted','is_dashboard_visible', )
        import_id_fields = ('name_ENG', 'name_AMH','topic')



class IndicatorResource(resources.ModelResource):    
    for_category = fields.Field(
        column_name='for_category',
        attribute='for_category',
        widget=ManyToManyWidget(Category, field='name_ENG', separator='|'),
        saves_null_values = True,
    )

    
    parent = fields.Field(
        column_name='parent',
        attribute='parent',
        widget=ForeignKeyWidget(Indicator, field='id'),
        saves_null_values = True,
    )





    class Meta:
        model = Indicator
        report_skipped = True
        skip_unchanged = True
        exclude = ( 'created_at', 'is_deleted', 'composite_key','op_type')