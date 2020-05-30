function populate_district(s1,s2){
  var s1 = document.getElementById(s1);
  var s2 = document.getElementById(s2);
  var district = "";
  if(s1.value == "Provice One"){
    
  }
  alert(s1.value);

}
// $.ajax({
//   url: './static/js/nepal_district.geojson' ,
//   dataType:'JSON',
//   success:function(data){
//         console.log("Winner");
//   },
//   error : function(err){
//       console.log(err);
//   }
// });
var district_boundary = "";
$.ajax({
  dataType : "json",
  url : "./static/js/nepal_district.geojson",
  success : function(data){
   console.log("OK DONE");
  }
}).error(function(err){
  console.log("NOT OK")
});



function drag_drop(event){
  event.preventDefault();
  alert(event.dataTransfer.files[0]);
  console.log(event.dataTransfer.files[0].name);
}

