
console.log("File got loaded");


mapboxgl.accessToken = 'pk.eyJ1Ijoic2VyemFucyIsImEiOiJjaXl1ZHVobTEwMDBvMnFycjlzcm9rcXB4In0.upeL8wQ_YbuTjQ8oN1SOFA';
var map = new mapboxgl.Map({
    container: 'map', // container id
    style: 'mapbox://styles/mapbox/streets-v9', //stylesheet location
    center: [-1.2577, 51.7520], // starting position
    zoom: 12, // starting zoom
});
map.addControl(new MapboxGeocoder({
    accessToken: mapboxgl.accessToken
}));

$(document).ready( function() {
  $('#search').click(function(){

    var APIarray = [];

    $.each($("input[name='API']:checked"), function(){
        APIarray.push($(this).val());
});

searchRequest = {type: $('#businessType').val(), API: APIarray, coord: map.getCenter().toArray()};
    $.ajax({
        method: "GET",
        url: "ajax/",
        success: function(data) {
            alert("success");
            updateMap(data);
        }
    });

});
});

function updateMap(data) {
    console.log(data);
    var layer = {
    "id": "points",
    "type": "symbol",
    "source": {
        "type": "geojson",
        "data": {
            "type": "FeatureCollection",
            "features": data
        }
    },
    "layout": {
        "icon-image": "{icon}-15",
        "text-field": "{title}",
        "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
        "text-offset": [0, 0.6],
        "text-anchor": "top"
    }
    };
    console.log(layer);
    map.addLayer(layer);
}
