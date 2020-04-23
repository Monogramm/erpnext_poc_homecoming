let map = L.map('map').setView([48.85, 2.35], 13); //coords of Paris

L.tileLayer("https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=FaOWvrcTPKiDQ2FGKKVY", {
    attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> ' +
        '<a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
}).addTo(map);


frappe.call({
    method: "erpnext_poc_homecoming.erpnext_poc_homecoming.doctype.organization.organization_utils.get_all_organizations",
    callback: function (r) {
        let places = r.message;
        console.log(places.length);
        console.log(places);
        for (let i = 0; i < places.length; i++){
            let place = JSON.parse(places[i].location);
            L.marker(place.features[0].geometry.coordinates.reverse()).addTo(map);
        }
    }
});