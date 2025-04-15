

function initMap(){
  const map = new google.maps.Map(document.getElementById("map"),{
    center: {lat: 33.7756, lng:-84.3962},
    zoom: 13
  });
  const locations = [
    { lat: 33.7919857251714, lng: -84.40508479634288 },
    { lat: 33.77372313263816, lng: -84.40834636434231 },
    { lat: 33.7784675008004, lng: -84.39787502008299 }
  ];
  locations.forEach((loc, index) => {
    new google.maps.Marker({
      position: loc,
      map,
      title: `Marker ${index + 1}`,
    });
  });
  
}
window.initMap = initMap;
// future fetch function for memories
// function fetchJson () {
//   return fetch('http://localhost:8081/api/reports')
//   .then(response => {
//     if (!response.ok) {
//       console.error('Network response error');
//     }
//     return response.json(); // Parse the response as JSON
//   })
//   .then(data => {
//     console.log('Reports data:', data); // Log the reports data
//     return data; // Return the reports data for further use
//   })
//   .catch(error => {
//     console.error('Error fetching reports:');
//   });


// }
//const location = [];
//const markers =[];
//Fetches from backend
// fetchJson().then(reports => {
//   if (reports) {
//       reports.forEach(report => {
//           // write what to do for each report
//           const address = report.location;
//           const apiKey = "AIzaSyClxmOnTy2zT4cbTcQd6B5wczbj-aXZ2O4&";
//           const geocodeUrl = `https://maps.googleapis.com/maps/api/geocode/json?address=${encodeURIComponent(address)}&key=${apiKey}`;
//           fetch(geocodeUrl)
//               .then(response => response.json())
//               .then(data => {
//               if (data.status === "OK") {
//                   location.push(data.results[0].geometry.location);
//                   markers.push(new google.maps.Marker({
//                     position: data.results[0].geometry.location,
//                     map: map,
//                   }))
//                   console.log(location);
//                   markers.forEach((mark) => {
//                     new google.maps.Marker({
//                       position: mark.position,
//                       map: map,
//                     });
//                   });
//                   console.log("asjdfh "+ markers);
//               } else {
//                   console.error("Geocoding failed: " + data.status);
//               }
//               })
//           .catch(error => console.error("Error:", error));
//       })
//   }
// })
// function initMap() {
//   const map = new google.maps.Map(document.getElementById("map"), {
//     center: { lat: 33.7756, lng: -84.3962 },
//     zoom: 13,
//   });

//   new google.maps.Marker({
//     position: { lat: 37.422, lng: -122.084 },
//     map,
//     title: "Mountain View, CA",
//   });
// }

// window.initMap = initMap;
