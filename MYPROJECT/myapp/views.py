from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests
import json


# Create your views here.
STATION_STATUS = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
BIKE_STATUS = "https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json"



def available_docks(request):
    res = requests.get(STATION_STATUS)
    data = res.json()
    result = data["data"]["stations"]
    # print(len(result))

    active_stations = 0
    docks_available = 0
    ebikes_available = 0
    for station in result:
        if station['station_status'] == "active":
            active_stations += 1
            docks_available += station['num_docks_available']
            ebikes_available += station['num_ebikes_available']

    # print("active_stations : ", active_stations)
    # print("docks_available : ", docks_available)
    # print("ebikes_available : ", ebikes_available)
    d = {
        "active_stations": active_stations,
        "docks_available": docks_available,
        "ebikes_available": ebikes_available,
         "data": result,

    }
    return JsonResponse(d)


def free_bike_status(request):
    res1 = requests.get(BIKE_STATUS)
    data1 = res1.json()
    result1 = data1["data"]["bikes"]
    # print(len(result1))
    reserved_bikes = 0
    for bike in result1:
        reserved_bikes += bike['is_reserved']

    # print("is_reserved: ", reserved_bikes)
    d1 = {"reserved bikes": reserved_bikes}

    return JsonResponse(d1)