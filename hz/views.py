# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from urllib2 import Request, urlopen
from .forms import RestForm
from multiprocessing import Pool
from django.contrib.auth.forms import AuthenticationForm
import json


# Create your views here.
def rest_api(title, keyword):
    client_id = "NcX91n74ipkTU9hJevhc"
    client_secret = "5ameCGlFSL"
    url = "https://openapi.naver.com/v1/datalab/search";
    body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-10-31\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\""+title+"\",\"keywords\":[\""+ keyword+"\"]}],\"device\":\"pc\",\"ages\":[\"3\",\"4\"],\"gender\":\"m\"}";

    request = Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")
    response = urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        json_result = json.load(response)
        return json_result
    else:
        print("Error Code:" + rescode)


@login_required
def rest_post(request):
    if request.method == "POST":
        form = RestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            json_data = rest_api(post.title, post.keyword)
            result = json_data['results'][0]
            # post.title =
            # post.keyword = str(result['keywords'][0])
            # post.start_date = str(json_data['startDate'])
            # post.end_date = str(json_data['endDate'])


            # post.save()
            period_list = []
            ratio_list = []
            for data in result['data']:
                period_list.append(str(data['period']))
                ratio_list.append(str(data['ratio']))
            return render_to_response('hz/data.html', {'title': str(result['title']), 'keyword':str(result['keywords'][0]), 'period': period_list, 'ratio':ratio_list})
    else:
        form = RestForm()
    return render(request, 'hz/rest.html', {'form':form})
