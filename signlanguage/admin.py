from django.contrib import admin

# Register your models here.
from .models import Result, AiModel

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id','image','version','isCorrect','pub_date']
    list_display_links = ['id']
    models = AiModel.objects.all()
    model_count = AiModel.objects.all().count()
    model_context = []
    for idx, model in enumerate(models):
        if Result.objects.filter(version=model.version).count() != 0:
            model_context.append( [model.version, int(Result.objects.filter(version=model.version, isCorrect=True).count() / Result.objects.filter(version=model.version).count() * 100)] )
        else:
            pass
    print(model_context)
    
    def changelist_view(self, request, extra_context=None):
        chart_data = {
            'model_context' : self.model_context,
        }
        return super().changelist_view(request, extra_context=chart_data)


class AiModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'version','is_selected','pub_date']
    list_display_links = ['id', 'version']
    
        
# 관리에서 Result 객체에 대해  기본 CRUD 관리를 한다. 
admin.site.register(Result, ResultAdmin)
admin.site.register(AiModel, AiModelAdmin)






# from django.contrib import admin

# # Register your models here.
# from .models import Result, AiModel

# class ResultAdmin(admin.ModelAdmin):
#     list_display = ['id','image','version','isCorrect','pub_date']
#     list_display_links = ['id']
#     global p1, p2, p3, p4, p5
#     p1 = int(Result.objects.filter(version='v01', isCorrect=True).count() / Result.objects.filter(version='v01').count() *100) if Result.objects.filter(version='v01').count() != 0 else 0
#     p2 = int(Result.objects.filter(version='v02', isCorrect=True).count() / Result.objects.filter(version='v02').count() *100) if Result.objects.filter(version='v02').count() != 0 else 0
#     p3 = int(Result.objects.filter(version='v03', isCorrect=True).count() / Result.objects.filter(version='v03').count() *100) if Result.objects.filter(version='v03').count() != 0 else 0
#     p4 = int(Result.objects.filter(version='v04', isCorrect=True).count() / Result.objects.filter(version='v04').count() *100) if Result.objects.filter(version='v04').count() != 0 else 0
#     p5 = int(Result.objects.filter(version='v05', isCorrect=True).count() / Result.objects.filter(version='v05').count() *100) if Result.objects.filter(version='v05').count() != 0 else 0
    
#     def changelist_view(self, request, extra_context=None):
#         chart_data = {
#             'v01': p1,
#             'v02': p2,
#             'v03': p3,
#             'v04': p4,
#             'v05': p5,   
#         }
#         return super().changelist_view(request, extra_context=chart_data)


# class AiModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'version','is_selected','pub_date']
#     list_display_links = ['id', 'version']
    
        
# # 관리에서 Result 객체에 대해  기본 CRUD 관리를 한다. 
# admin.site.register(Result, ResultAdmin)
# admin.site.register(AiModel, AiModelAdmin)