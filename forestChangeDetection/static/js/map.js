




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