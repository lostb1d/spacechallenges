var mymap = L.map('mapid').setView([28.319,83.903], 6);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibG9zdGIxIiwiYSI6ImNqaTBjcGd4bjE2cGMza3M2MWEzcTRwd3gifQ.Ps6yKHol2bmEPndMSeYKKw'
}).addTo(mymap);

function getData(){
    var inputNode = document.createElement('input');
        inputNode.setAttribute('type','file');
        inputNode.setAttribute('id','leaflet-draw-shapefile-selector');
        inputNode.setAttribute('accept','.geojson');

        inputNode.addEventListener("change", function(e){
          var files = inputNode.files;
          var file = files[0];
          var reader = new FileReader();
          reader.onload = function() {
            var geo = omnivore.geojson(reader.result)
            .on('ready',function(){
                mymap.fitBounds(geo.getBounds());
              })
            .addTo(mymap);
            };
          reader.readAsDataURL(file);
        });
        inputNode.click();
  }
var drawnItems;
function draw(){
    if(drawnItems==undefined){
        drawnItems = new L.FeatureGroup();
        mymap.addLayer(drawnItems);
        var drawControl = new L.Control.Draw({
            // position: 'topright',
            draw: {
                polygon:  {
                    shapeOptions: {
                     color: 'red'
                    },
                   },
                polyline: false,
                rect: {
                shapeOptions: {
                color: 'green'
                },
                },
                circle: false,
                circlemarker: false,
                marker: false
            },
                edit: {
                    featureGroup: drawnItems,
                    edit: false
                }
            });
        mymap.addControl(drawControl);
        mymap.on('draw:created', function (e) {
                    drawnItems.addLayer(e.layer);
                });
        mymap.on(L.Draw.Event.CREATED, function (e) {
            var layer = e.layer;
        mymap.addLayer(layer);
        });
    }else{return;}
}