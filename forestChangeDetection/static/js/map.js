// function getData(){
//     var inputNode = document.createElement('input');
//         inputNode.setAttribute('type','file');
//         inputNode.setAttribute('id','leaflet-draw-shapefile-selector');
//         inputNode.setAttribute('accept','.geojson');

//         inputNode.addEventListener("change", function(e){
//           var files = inputNode.files;
//           var file = files[0];
//           var reader = new FileReader();
//           reader.onload = function() {
//             var geo = omnivore.geojson(reader.result)
//             .on('ready',function(){
//                 mymap.fitBounds(geo.getBounds());
//               })
//             .addTo(mymap);
//             };
//           reader.readAsDataURL(file);
//         });
//         inputNode.click();
//   }
// var drawnItems;
// function draw(){
//     if(drawnItems==undefined){
//         drawnItems = new L.FeatureGroup();
//         mymap.addLayer(drawnItems);
//         var drawControl = new L.Control.Draw({
//             // position: 'topright',
//             draw: {
//                 polygon:  {
//                     shapeOptions: {
//                      color: 'red'
//                     },
//                    },
//                 polyline: false,
//                 rect: {
//                 shapeOptions: {
//                 color: 'green'
//                 },
//                 },
//                 circle: false,
//                 circlemarker: false,
//                 marker: false
//             },
//                 edit: {
//                     featureGroup: drawnItems,
//                     edit: false
//                 }
//             });
//         mymap.addControl(drawControl);
//         mymap.on('draw:created', function (e) {
//                     drawnItems.addLayer(e.layer);
//                 });
//         mymap.on(L.Draw.Event.CREATED, function (e) {
//             var layer = e.layer;
//         mymap.addLayer(layer);
//         });
//     }else{return;}
// }