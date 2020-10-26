var mymap = L.map('mapid').setView([39.103119, -84.512016], 14);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'abcd' //enter your access token here
}).addTo(mymap);

mapMarkers1 =  []
mapMarkers2 =  []
mapMarkers3 =  []
mapMarkers4 =  []
mapMarkers5 =  []

var source = new EventSource('/topic/final_geodata')
source.addEventListener('message', function (e) {

    
    obj = JSON.parse(e.data);
    console.log(obj);

    if (obj.busline == '00001') {
        for (var i = 0; i < mapMarkers1.length; i++) {
            mymap.removeLayer(mapMarkers1[i]);
        }
        marker1 = L.marker([obj.latitude, obj.longitude]).addTo(mymap);
        mapMarkers1.push(marker1);
    }

    if (obj.busline == '00002') {
        for (var i = 0; i < mapMarkers2.length; i++) {
            mymap.removeLayer(mapMarkers2[i]);
        }
        marker2 = L.marker([obj.latitude, obj.longitude]).addTo(mymap);
        mapMarkers2.push(marker2);
    }

    if (obj.busline == '00003') {
        for (var i = 0; i < mapMarkers3.length; i++) {
            mymap.removeLayer(mapMarkers3[i]);
        }
        marker3 = L.marker([obj.latitude, obj.longitude]).addTo(mymap);
        mapMarkers3.push(marker3);
    }
    if (obj.busline == '00004') {
        for (var i = 0; i < mapMarkers4.length; i++) {
            mymap.removeLayer(mapMarkers4[i]);
        }
        marker4 = L.marker([obj.latitude, obj.longitude]).addTo(mymap);
        mapMarkers4.push(marker4);
    }

    if (obj.busline == '00005') {
        for (var i = 0; i < mapMarkers5.length; i++) {
            mymap.removeLayer(mapMarkers5[i]);
        }
        marker5 = L.marker([obj.latitude, obj.longitude]).addTo(mymap);
        mapMarkers5.push(marker5);
    }
}, false);