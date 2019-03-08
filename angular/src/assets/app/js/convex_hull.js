// Copyright 2001, softSurfer (www.softsurfer.com)
// This code may be freely used and modified for any purpose
// providing that this copyright notice is included with it.
// SoftSurfer makes no warranty for this code, and cannot be held
// liable for any real or imagined damage resulting from its use.
// Users of this code must verify correctness for their application.
// http://softsurfer.com/Archive/algorithm_0203/algorithm_0203.htm
// Assume that a class is already given for the object:
//    Point with coordinates {float x, y;}
//===================================================================

// isLeft(): tests if a point is Left|On|Right of an infinite line.
//    Input:  three points P0, P1, and P2
//    Return: >0 for P2 left of the line through P0 and P1
//            =0 for P2 on the line
//            <0 for P2 right of the line

function sortPointX(a, b) {
    return a.lng() - b.lng();
}
function sortPointY(a, b) {
    return a.lat() - b.lat();
}

function isLeft(P0, P1, P2) {
    return (P1.lng() - P0.lng()) * (P2.lat() - P0.lat()) - (P2.lng() - P0.lng()) * (P1.lat() - P0.lat());
}
//===================================================================

// chainHull_2D(): A.M. Andrew's monotone chain 2D convex hull algorithm
// http://softsurfer.com/Archive/algorithm_0109/algorithm_0109.htm
//
//     Input:  P[] = an array of 2D points
//                   presorted by increasing x- and y-coordinates
//             n = the number of points in P[]
//     Output: H[] = an array of the convex hull vertices (max is n)
//     Return: the number of points in H[]


function chainHull_2D(P, n, H) {
    // the output array H[] will be used as the stack
    var bot = 0,
        top = (-1); // indices for bottom and top of the stack
    var i; // array scan index
    // Get the indices of points with min x-coord and min|max y-coord
    var minmin = 0,
        minmax;

    var xmin = P[0].lng();
    for (i = 1; i < n; i++) {
        if (P[i].lng() != xmin) {
            break;
        }
    }

    minmax = i - 1;
    if (minmax == n - 1) { // degenerate case: all x-coords == xmin
        H[++top] = P[minmin];
        if (P[minmax].lat() != P[minmin].lat()) // a nontrivial segment
            H[++top] = P[minmax];
        H[++top] = P[minmin]; // add polygon endpoint
        return top + 1;
    }

    // Get the indices of points with max x-coord and min|max y-coord
    var maxmin, maxmax = n - 1;
    var xmax = P[n - 1].lng();
    for (i = n - 2; i >= 0; i--) {
        if (P[i].lng() != xmax) {
            break;
        }
    }
    maxmin = i + 1;

    // Compute the lower hull on the stack H
    H[++top] = P[minmin]; // push minmin point onto stack
    i = minmax;
    while (++i <= maxmin) {
        // the lower line joins P[minmin] with P[maxmin]
        if (isLeft(P[minmin], P[maxmin], P[i]) >= 0 && i < maxmin) {
            continue; // ignore P[i] above or on the lower line
        }

        while (top > 0) { // there are at least 2 points on the stack
            // test if P[i] is left of the line at the stack top
            if (isLeft(H[top - 1], H[top], P[i]) > 0) {
                break; // P[i] is a new hull vertex
            }
            else {
                top--; // pop top point off stack
            }
        }

        H[++top] = P[i]; // push P[i] onto stack
    }

    // Next, compute the upper hull on the stack H above the bottom hull
    if (maxmax != maxmin) { // if distinct xmax points
        H[++top] = P[maxmax]; // push maxmax point onto stack
    }

    bot = top; // the bottom point of the upper hull stack
    i = maxmin;
    while (--i >= minmax) {
        // the upper line joins P[maxmax] with P[minmax]
        if (isLeft(P[maxmax], P[minmax], P[i]) >= 0 && i > minmax) {
            continue; // ignore P[i] below or on the upper line
        }

        while (top > bot) { // at least 2 points on the upper stack
            // test if P[i] is left of the line at the stack top
            if (isLeft(H[top - 1], H[top], P[i]) > 0) {
                break;  // P[i] is a new hull vertex
            }
            else {
                top--; // pop top point off stack
            }
        }

// breaks algorithm
//        if (P[i].lng() == H[0].lng() && P[i].lat() == H[0].lat()) {
//            return top + 1; // special case (mgomes)
//        }

        H[++top] = P[i]; // push P[i] onto stack
    }

    if (minmax != minmin) {
        H[++top] = P[minmin]; // push joining endpoint onto stack
    }

    return top + 1;
}




<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml">
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title>Google Maps JavaScript API Example: Convex Hull</title>

<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false&amp;libraries=geometry"></script>

    <script type="text/javascript" src="scripts/convex_hull.js"></script>

    <script type="text/javascript">
//<![CDATA[

var gmarkers = [];
var points = [];
var hullPoints = [];
var map = null;
var polyline;

var infowindow = new google.maps.InfoWindow(
    {
        size: new google.maps.Size(150,50)
    });
/*
points = [
new GLatLng(37.455949,-122.184578),
new GLatLng(37.426063,-122.112959),
new GLatLng(37.442271,-122.099669),
new GLatLng(37.462248,-122.160239),
new GLatLng(37.454942,-122.140154),
new GLatLng(37.434649,-122.151661),
new GLatLng(37.439245,-122.119776),
new GLatLng(37.441485,-122.163136),
new GLatLng(37.450725,-122.119423),
new GLatLng(37.457801,-122.117583)
]
*/


function initialize() {
    var myOptions = {
        zoom: 13,
        center: new google.maps.LatLng(37.4419, -122.1419),
        mapTypeControl: true,
        mapTypeControlOptions: {style: google.maps.MapTypeControlStyle.DROPDOWN_MENU},
        navigationControl: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    map = new google.maps.Map(document.getElementById("map_canvas"),
        myOptions);

    google.maps.event.addListener(map, 'click', function() {
        infowindow.close();
    });

    google.maps.event.addListenerOnce(map, 'bounds_changed', function() {
        // Add 10 markers to the map at random locations
        var bounds = map.getBounds();
        var southWest = bounds.getSouthWest();
        var northEast = bounds.getNorthEast();
        var lngSpan = northEast.lng() - southWest.lng();
        var latSpan = northEast.lat() - southWest.lat();
        map.setCenter(map.getCenter());
        map.setZoom(map.getZoom()-1);
        /* */
        for (var i = 0; i < 10; i++) {
            var point = new google.maps.LatLng(southWest.lat() + latSpan * Math.random(),
                southWest.lng() + lngSpan * Math.random());
            points.push(point);
            var marker = createMarker(point, i);
            gmarkers.push(marker);
        }
        /* */
        /*
                for (var i = 0; i<points.length; i++) {
              var marker = createMarker(points[i], i);
              gmarkers.push(marker);
                  map.addOverlay(marker);
                }
        */
        for (var i=0; i < points.length; i++) {
            document.getElementById("input_points").innerHTML += i+": "+points[i].toUrlValue()+"<br>";
        }

        calculateConvexHull();
    });
    google.maps.event.addListener(map, "click", function(evt) {
        if (evt.latLng) {
            var latlng = evt.latLng;
//            alert("latlng:"+latlng.toUrlValue());
            var marker = createMarker(latlng, gmarkers.length-1);
            points.push(latlng);
            gmarkers.push(marker);
            calculateConvexHull();

        }
    });
}

function removeMarker(latlng) {
    for (var i= 0; i < gmarkers.length;i++) {
        if (google.maps.geometry.spherical.computeDistanceBetween(
                latlng, gmarkers[i].getPosition()) < 0.1)
        {
            gmarkers[i].setMap(null);
            gmarkers.splice(i,1);
        }
    }
    calculateConvexHull();
}

function createMarker(latlng, marker_number) {
    var html = "marker "+marker_number;
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        zIndex: Math.round(latlng.lat()*-100000)<<5
    });

    google.maps.event.addListener(marker, 'click', function() {
        var contentString = html + "<br>"+marker.getPosition().toUrlValue()+"<br><a href='javascript:removeMarker(new google.maps.LatLng("+marker.getPosition().toUrlValue()+"));'>Remove Marker</a>";
        infowindow.setContent(contentString);
        infowindow.open(map,marker);
    });
    return marker;
}



function calculateConvexHull() {
    if (polyline) polyline.setMap(null);
    document.getElementById("hull_points").innerHTML = "";
    points = [];
    for (var i=0; i < gmarkers.length; i++) {
        points.push(gmarkers[i].getPosition());
    }
    points.sort(sortPointY);
    points.sort(sortPointX);
    DrawHull();
}

function sortPointX(a,b) { return a.lng() - b.lng(); }
function sortPointY(a,b) { return a.lat() - b.lat(); }

function DrawHull() {
    hullPoints = [];
    chainHull_2D( points, points.length, hullPoints );
    polyline = new google.maps.Polygon({
        map: map,
        paths:hullPoints,
        fillColor:"#FF0000",
        strokeWidth:2,
        fillOpacity:0.5,
        strokeColor:"#0000FF",
        strokeOpacity:0.5
    });
    displayHullPts();
}

function displayHullPts() {
    document.getElementById("hull_points").innerHTML = "";
    for (var i=0; i < hullPoints.length; i++) {
        document.getElementById("hull_points").innerHTML += hullPoints[i].toUrlValue()+"<br>";
    }
}

//]]>
</script>
</head>
<body onload="initialize()">
    <h2>Convex Hull of random set of points</h2>
<table border="0">
    <tr><td>
    <button onclick="polyline.setMap(null);">hide polygon</button>
<button onclick="calculateConvexHull();">calculate Convex Hull</button>
<button onclick="displayHullPts();">display Hull Points</button>
</td></tr>

<tr><td valign="top">
    <div id="map_canvas" style="width: 500px; height: 300px"></div>
    <table border="1" width="100%">
    <tr><th>random pts</th><th>hull points</th></tr>
<tr><td valign="top">
    <div id="input_points"></div>
    </td><td valign="top">
    <div id="hull_points"></div>
    </td></tr></table>
</td>

<td>
<script type="text/javascript"><!--
    google_ad_client = "pub-8586773609818529";
/* Verticle Ad */
google_ad_slot = "4289667470";
google_ad_width = 160;
google_ad_height = 600;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
    </script>
    </td>

    </tr>
    <tr><td><a href="http://www.geocodezip.com/map-markers_ConvexHull_Polygon.asp">v2 version of convex hull</a></td></tr>
</table>
<div id="info"></div>
    <div id="w3valid">
    <a href="http://validator.w3.org/check?uri=referer" ><!-- target="validationresults" --><img
src="http://www.w3.org/Icons/valid-xhtml10"
alt="Valid XHTML 1.0 Transitional" height="31" width="88" /></a>
    </div>
    <script src="http://www.google-analytics.com/urchin.js" type="text/javascript">
    </script>
    <script type="text/javascript">
_uacct = "UA-162157-1";
urchinTracker();
</script>
</body>
</html>
