from rest_framework.response import Response
from django.http import JsonResponse
import random
from rest_framework.decorators import api_view
from Base.models import (
    Topic,
    Category,
    Indicator,
    AnnualData,
    DataPoint
)
@api_view(['GET'])
def get_indicators(request,id):
   '''
   filter Indicator by category id with children
   '''
   indicators_list = []
   indicators = Indicator.objects.filter(for_category__id = id, is_deleted = False).select_related()
   for i in indicators:
      indicators_list.append({
         'id' : i.id,
         'title_ENG' : i.title_ENG,
         'title_AMH' : i.title_AMH,
         'composite_key' : i.composite_key,
         'parent_id' : i.parent.id if i.parent else None,
         'for_category' : list(i.for_category.filter().values_list('name_ENG', flat=True)),
         'measurement_units' : i.measurement_units,
         'kpi_characteristics' : i.kpi_characteristics,
         'is_dashboard_visible' : i.is_dashboard_visible,
         'is_public' : i.is_public,
      })
   context ={
      'indicators' : indicators_list
   }
   return Response(context)

@api_view(['GET'])
def filter_topic_and_category(request):
   '''
   filter indicator and category
   '''
   topics = list(Topic.objects.filter(is_deleted = False).select_related().values('id','title_ENG','title_AMH'))
   categories = list(Category.objects.filter(is_deleted = False).select_related().values('id','name_ENG','name_AMH','topic__id'))
   context = {
      'topics' : topics,
      'categories' : categories,
   }
   return Response(context)


@api_view(['GET'])
def filter_indicator_by_category(request, id):   
   '''
   filter indicator by category
   '''
   indicators = list(Indicator.objects.filter(for_category__id = id, parent = None ,is_deleted = False).select_related().values('id','title_ENG','title_AMH'))
   context = {
      'indicators' : indicators
   }
   return Response(context)


@api_view(['GET'])
def filter_indicator_annual_value(request):
   if request.method == 'GET':
      indicator_ids = request.GET.getlist('indicator_ids')
      parent_indicator_id = indicator_ids[0].split(',')
      indicator_list_id_with_children = []
      def child_list(parent):
            child = Indicator.objects.filter(parent = parent).select_related()
            for i in child:
               indicator_list_id_with_children.append(i.id)
               child_list(i)
                    
      for i in parent_indicator_id:
          parent = Indicator.objects.filter(id = i).select_related().first()
          indicator_list_id_with_children.append(parent.id)
          child_list(parent)
      
      

      annual_data_value =list( AnnualData.objects.filter(indicator__id__in = indicator_list_id_with_children ).values(
         'id',
         'indicator__title_ENG',
         'indicator__title_AMH',
         'indicator__id',
         'indicator__parent_id',
         'for_datapoint__year_EC',
         'for_datapoint__year_GC',
         'performance',
         'target'
      ))
      year = list( AnnualData.objects.filter(indicator__id__in = indicator_list_id_with_children).values(
         'for_datapoint__year_EC',
         'for_datapoint__year_GC',
      ).distinct())

      context = {
         'year' : year,
         'annual_data_value' : annual_data_value
      }
      return Response(context)


@api_view(['GET'])
def detail_indicator_with_children(request, id):
   if request.method == 'GET':
      indicator = Indicator.objects.filter(id = id, is_deleted = False).select_related().first()
      indicator_id_with_children = []

      def child_list(parent):
            child = Indicator.objects.filter(parent = parent).select_related()
            for i in child:
               indicator_id_with_children.append(i.id)
               child_list(i)

      indicator_id_with_children.append(indicator.id)
      child_list(indicator)


      annual_data_value =list(AnnualData.objects.filter(indicator__id__in = indicator_id_with_children ).values(
         'id',
         'indicator__title_ENG',
         'indicator__title_AMH',
         'indicator__id',
         'indicator__parent_id',
         'for_datapoint__year_EC',
         'for_datapoint__year_GC',
         'performance',
         'target'
      ))

      year = list(DataPoint.objects.all().values('year_EC', 'year_GC'))

      #for_datapoint__year_EC

      context = {
         'year' : year,
         'annual_data_value' : annual_data_value
      }

      return Response(context)
   

      