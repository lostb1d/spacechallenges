var mymap = L.map('mapid').setView([28.319,83.903], 6);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibG9zdGIxIiwiYSI6ImNqaTBjcGd4bjE2cGMza3M2MWEzcTRwd3gifQ.Ps6yKHol2bmEPndMSeYKKw'
}).addTo(mymap);

// L.geoJSON(nepal_data).addTo(mymap);

function check(data){
    
    
    // $.getJSON(data.value, function(data1){
    //     L.geoJSON(data1).addTo(mymap);
    // })
    
  }
  document.getElementById('input-file-now').addEventListener('change', function() { 
    
  var fr=new FileReader(); 
  fr.onload=function(){ 
      document.getElementById('output').textContent=fr.result; 
  } 
  fr.readAsText(this.files[0]); 
}) 