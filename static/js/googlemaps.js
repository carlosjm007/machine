$(document).ready(initMap);
var map;
var stilo = [{"featureType":"water","elementType":"geometry","stylers":[{"color":"#193341"}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#2c5a71"}]},{"featureType":"road","elementType":"geometry","stylers":[{"color":"#29768a"},{"lightness":-37}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#406d80"}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#406d80"}]},{"elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#3e606f"},{"weight":2},{"gamma":0.84}]},{"elementType":"labels.text.fill","stylers":[{"color":"#ffffff"}]},{"featureType":"administrative","elementType":"geometry","stylers":[{"weight":0.6},{"color":"#1a3541"}]},{"elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#2c5a71"}]}];
function initMap() {
	$("#mapContainer").width($(window).width() - 313);	
	$("#mapContainer").height($(window).height() - 79);
	map = new google.maps.Map(document.getElementById('map'), {
		center: {lat: 4.138365546724636, lng: -73.62459378814697},
		zoom: 14,
		styles: stilo
	});
	// map.addListener('center_changed', function() {
	// 	console.log(map.getCenter().lat() + " <-> " + map.getCenter().lng());
	// });
	$("#map").css({"width":$("#mapContainer").width(),"height":$(window).height() - 120});
}
$(window).resize(function() {
	$("#mapContainer").width($(window).width() - 313);
	$("#mapContainer").height($(window).height() - 79);
  	$("#map").css({"width":$("#mapContainer").width(),"height":$(this).height() - 120});
});