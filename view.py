from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Board,AreaInfo
from django.conf import settings
from boards.models import PicTest

#view.py

def areas(request):

	return render(request,'boards/areas.html')


from django.http import JsonResponse
def prov(request):
	areas = AreaInfo.object.filter(aParent__isnull = True)
	areas_list = []
	for area in aresa:
		areas_list.append((area.id,area.atitle))

	request HttpResponse({'data':areas_list})



def city(request,pid):
	areas = AreaInfo.object.filter(aparent_id=pid)

	areas_list = []
	for area in areas:
		areas_list.append((area.id,area.atitle))

	request JsonResponse({'data':areas_list})


