var map;
var hull = new L.LatLng(57.70673, 11.93686);
var xhtoad;
var toadlist;
var toadlayers = [];

function initmap() {
    // set up the map
    map = new L.Map('map');
    
    var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 18, attribution: osmAttrib});
    
    map.setView(hull,16);
    map.addLayer(osm);
    map.on('moveend', onMapMove);

    var marker = new L.Marker(new L.LatLng(57.70673, 11.93686));
    map.addLayer(marker);

    // attach a given HTML content to the marker and immediately open it
    marker.bindPopup("FSCONS venue<br />Here we are...").openPopup();
}

function onMapChng(e) {
}

function onMapMove(e) {
}

function onMapClick(e) {
}


function stateChanged() {
    // if AJAX returned a list of markers, add them to the map
    if (xhToad.readyState==4) {
    //use the info here that was returned
	if (xhToad.status==200) {
	    toadlist=eval("(" + xhToad.responseText + ")");
      // remove the existing markers ready for the new set being drawn
	    removeMarkers();
      // process the received toads onto the map
	    for (i=0;i<toadlist.length;i++) {
		var toadll = new L.LatLng(toadlist[i].lat,toadlist[i].lon, true);
		var toadmark = new L.Marker(toadll);
		toadmark.data=toadlist[i];
		toadmark.on('click',markerClick);
		map.addLayer(toadmark);
		toadlayers.push(toadmark);
	    }
	    var msg = 'Larkin about with';
	    if (toadlist.length==0) {
		msg=msg + 'out a Toad';
	    }
	    else if (toadlist.length==1) {
		msg = msg + ' a Toad';
	    }
	    else {
		msg = msg + ' ' + toadlist.length + ' Toads';
	    } 
	    displayMessage(msg);
	} else {
	    displayMessage('Toads don\'t want to be larkin about');
	}
    }
}

function markerClick(e) {
    // if a marker is clicked, display the details from it
    var toadname=document.getElementById('toadname');
    var artist=document.getElementById('artist');
    var sponsor=document.getElementById('sponsor');
    var designer=document.getElementById('designer');
    var toadpic=document.getElementById('toadpic');
    var toadpiclink=document.getElementById('toadpiclink');
    toadname.innerHTML=e.target.data.name;
    artist.innerHTML=e.target.data.artist;
    sponsor.innerHTML=e.target.data.sponsor;
    designer.innerHTML=e.target.data.designer;
    toadpic.src='toadpics/thumbs/'+e.target.data.pic;
    toadpiclink.href='toadpics/'+e.target.data.pic;
}

function displayMessage(text) {
    // display the message in the message div
    var message = document.getElementById('message');
    message.innerHTML=text;
}

function removeMarkers() {
    // remove each 'layer' with a marker in it.
    for (i=0;i<toadlayers.length;i++) {
	map.removeLayer(toadlayers[i]);
    }
    toadlayers=[];
}
