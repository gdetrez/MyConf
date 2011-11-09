/* -*- coding: utf-8 -*-
 * Copyright (C) 2011 Grégoire Détrez
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */
/* This script builds a simple map, using the leaflet library.
 * The builded map will be based on OSM tiles, with a marker on the FSCONS
 * venue building.
 * It can then be extended further by adding more markers or other data.
 */
var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
var osm = new L.TileLayer(osmUrl,
			  {minZoom: 8, maxZoom: 18, attribution: osmAttrib});
/* Defining a few map icons */
var CVenueIcon = L.Icon.extend({
      iconUrl: STATIC_URL + 'icons/venue.png',
      shadowUrl: STATIC_URL + 'icons/shadow.png',
      iconSize: new L.Point(44, 44),
      shadowSize: new L.Point(44, 44),
      iconAnchor: new L.Point(42, 40),
      popupAnchor: new L.Point(-18, -40)
    });

var CATMIcon = CVenueIcon.extend({
    iconUrl: STATIC_URL + 'icons/ATM.png'
});
var CBoatIcon = CVenueIcon.extend({
    iconUrl: STATIC_URL + 'icons/boat.png'
});
var CBusIcon = CVenueIcon.extend({
    iconUrl: STATIC_URL + 'icons/bus.png'
});
var CRestaurantIcon = CVenueIcon.extend({
    iconUrl: STATIC_URL + 'icons/restaurant.png'
});

var ATMIcon = new CATMIcon();
var RestaurantIcon = new CRestaurantIcon();
var BoatIcon = new CBoatIcon();
var BusIcon = new CBusIcon();
var VenueIcon = new CVenueIcon();

function initmap(id, lat, long) {
    // set up the map
    var map = new L.Map(id);
    var hull = new L.LatLng(lat, long);    
    map.setView(hull,16);
    map.addLayer(osm);

    
    var marker = new L.Marker(new L.LatLng(57.706647, 11.937141),
			      {icon:VenueIcon});
    marker.bindPopup("FSCONS venue<br />Here we are...");
    map.addLayer(marker);

    var marker = new L.Marker(new L.LatLng(57.706085,11.940600), 
			      {icon: ATMIcon});
    // ATM
    map.addLayer(new L.Marker(new L.LatLng(57.706085,11.940600), 
			      {icon: ATMIcon}));
    // boat stop
    map.addLayer(new L.Marker(new L.LatLng(57.705661,11.939882),
			      {icon: BoatIcon}));
    // Bus stop
    map.addLayer(new L.Marker(new L.LatLng(57.708246,11.938173), 
			      {icon: BusIcon}));
  // workshop venue
    map.addLayer(new L.Marker(new L.LatLng(57.693977,11.981609), 
			      {icon: VenueIcon}));
    return map;
}
