
// Creating the map object
var myMap = L.map("map", {
  center: [51.37999725, -0.406042069],
  zoom: 11
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

const markerCluster = new MarkerClusterGroup();

for (let i = 0; i < len(cord); i++)
{ console.log(cord[i][0])
  let lat = cord[i][0];
  let long = cord[i][1];


  const _mar = L.marker(new L.LatLng(lat, long), {
    icon: markerIcon
  });
  _mar.bindPopup(city);
  _mar.on('popupopen', function() {
    console.log('open popup');
  });
  _mar.on('popupclose', function() {
    console.log('close popup');
  });
  _mar.on('mouseout', function() {
    console.log('close popup with mouseout');
    myMap.closePopup();
  });
  console.log(myMap.getZoom());
  if (myMap.getZoom() > 15 && myMap.hasLayer(_mar)) {
    myMap.closePopup();
    console.log('zoom > 15 close popup');
  }
  markerCluster.addLayer(_mar);
}
myMap.addLayer(markerCluster);
