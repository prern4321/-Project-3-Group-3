import cord from '../../Untitled.ipynb.ipynb';

// Creating the map object
var myMap = L.map("map", {
  center: [51.37999725, -0.406042069],
  zoom: 11
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

for (let i = 0; i < cord.length; i++) {
  let lat = cord[i][0];
  let long = cord[i][1];


  const _mar = L.marker(new L.LatLng(lat, long), {
    icon: markerIcon
  });


  
// Get the data with d3.
d3.json(url).then(function(response) {

  // Create a new marker cluster group.
  var markers = L.markerClusterGroup();

  // Loop through the data.
  for (var i = 0; i < response.length; i++) {

    // Set the data location property to a variable.
    var location = response[i].location;

    // Check for the location property.
    if (location) {

      // Add a new marker to the cluster group, and bind a popup.
      markers.addLayer(L.marker([location.coordinates[1], location.coordinates[0]])
        .bindPopup(response[i].descriptor));
    }

  }

  // Add our marker cluster layer to the map.
  myMap.addLayer(markers);

});
