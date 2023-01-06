
// Creating the map object
var myMap = L.map("map", {
  center: [51.37999725, -0.406042069],
  zoom: 11
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

var markers =  L.markerClusterGroup();

for (let i = 0; i < cord.length; i++){ 
  row = cord[i]
  let lat = row.latitude
  let long = row.longitude
  
  markers.addLayer(L.marker([lat, long]));
}
myMap.addLayer(markers);

