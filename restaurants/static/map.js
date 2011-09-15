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
var map;
var hull = new L.LatLng(57.70673, 11.93686);

function initmap() {
    // set up the map
    map = new L.Map('map');
    
    var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 18, attribution: osmAttrib});
    
    map.setView(hull,14);
    map.addLayer(osm);
    //map.on('moveend', onMapMove);

    var marker = new L.Marker(new L.LatLng(57.70673, 11.93686));
    map.addLayer(marker);

    // attach a given HTML content to the marker and immediately open it
    marker.bindPopup("FSCONS venue<br />Here we are...").openPopup();
}
