let map = L.map('map').setView([48.85, 2.35], 13); //coords of Paris

L.tileLayer("https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=FaOWvrcTPKiDQ2FGKKVY", {
    attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> ' +
        '<a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
}).addTo(map);

let current_url = window.location.href.split('/');
let let_url = current_url[0] + "//" + current_url[1] + current_url[2] +
    "/api/method/erpnext_poc_homecoming.erpnext_poc_homecoming.doctype.organization.organization.get_list_map";

window.onload = function () {
    $.ajax({
    datatype: "json",
    beforeSend: function (xhr) {
        xhr.setRequestHeader('X-Frappe-CSRF-Token', frappe.csrf_token);
    },
    url: let_url,
    success: function (r) {
        let places = r.message;
        console.log(places.length);
        console.log(places);
        for (let i = 0; i < places.length; i++) {
            let place = JSON.parse(places[i].location);
            L.marker(place.features[0].geometry.coordinates.reverse()).addTo(map)
                .bindPopup('<a href="' + places[i].route + '">' + places[i].title + '</a>')
                .openPopup();
        }
    },
});

};