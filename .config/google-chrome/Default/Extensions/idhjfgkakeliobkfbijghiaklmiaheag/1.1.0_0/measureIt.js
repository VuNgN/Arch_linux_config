var myStatusMeasureIt = false;
var isMoveMeasureIt = false;
var startXMeasureIt;
var startYMeasureIt;
var startScrollXMeasureIt;
var startScrollYMeasureIt;
var theWidthMeasureIt;
var theHeightMeasureIt;
var oldOverflowMeasureIt;
var callOnLoadMeasureIt = true;

function doOnLoadMeasureIt() {
	if (callOnLoadMeasureIt) {
		callOnLoadMeasureIt = false;
		var _body = document.getElementsByTagName('body') [0];
		var _divCoord = document.createElement('div');
		var _divRectangle = document.createElement('div');
		var _divRectangleBG = document.createElement('div');
		var _divShadow = document.createElement('div');
		
		_divCoord.id = "divCoordMeasureIt";
		_divRectangle.id = "divRectangleMeasureIt";
		_divRectangleBG.id = "divRectangleBGMeasureIt";
		_divShadow.id = "shadowMeasureIt";
		_divShadow.onmousemove = setValuesMeasureIt;
		_divShadow.onmousedown = mouseDownShadowMeasureIt;
		_divShadow.onmouseup = mouseUpShadowMeasureIt;
		
		_divRectangle.appendChild(_divRectangleBG);
		_body.appendChild(_divShadow);
		_body.appendChild(_divCoord);
		_body.appendChild(_divRectangle);
	}
}
function addLoadEventMeasureIt(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      if (oldonload) {
        oldonload();
      }
      func();
    }
  }
}
addLoadEventMeasureIt(doOnLoadMeasureIt);

chrome.extension.onRequest.addListener(
	function(request, sender, sendResponse) {
		if ((request.flag == false) || (request.flag == "false"))
			hideShadowMeasureIt();
		else
			showShadowMeasureIt();
		myStatusMeasureIt = request.flag;
		chrome.extension.sendRequest({myStatusMeasureIt: myStatusMeasureIt}, function(response) {
			
		});
});
function showShadowMeasureIt() {
	if (document.getElementById("shadowMeasureIt")==null) {
		doOnLoadMeasureIt();
	}
	document.getElementById("shadowMeasureIt").style.display = "block";
}
function hideShadowMeasureIt() {
	document.getElementById("shadowMeasureIt").style.display = "none";
	document.getElementById("divCoordMeasureIt").style.display = "none";
	document.getElementById("divRectangleMeasureIt").style.display = "none";
}
function setValuesMeasureIt() {
	if (isMoveMeasureIt) {
		currentXMeasureIt = window.event.clientX;
		currentYMeasureIt = window.event.clientY;
		theWidthMeasureIt = Math.abs(startXMeasureIt-currentXMeasureIt);
		theHeightMeasureIt = Math.abs(startYMeasureIt-currentYMeasureIt);
    var tooltip = document.getElementById('divCoordMeasureIt');
    tooltip.style.fontSize = '20px';
    tooltip.innerHTML = "width: "+theWidthMeasureIt+"<span class='smallTextMeasureIt'>px</span><br />height: "+theHeightMeasureIt+"<span class='smallTextMeasureIt'>px</span>";
		
		if (currentXMeasureIt<startXMeasureIt)
			document.getElementById('divRectangleMeasureIt').style.left = startScrollXMeasureIt+currentXMeasureIt+"px";
		else
			document.getElementById('divRectangleMeasureIt').style.left = startScrollXMeasureIt+startXMeasureIt+"px";
		
		if (currentYMeasureIt<startYMeasureIt)
			document.getElementById('divRectangleMeasureIt').style.top = startScrollYMeasureIt+currentYMeasureIt+"px";
		else
			document.getElementById('divRectangleMeasureIt').style.top = startScrollYMeasureIt+startYMeasureIt+"px";
		
		document.getElementById('divRectangleMeasureIt').style.height = theHeightMeasureIt+"px";
		document.getElementById('divRectangleMeasureIt').style.width = theWidthMeasureIt+"px";
		
		if (startYMeasureIt>screen.height-180)
			document.getElementById('divCoordMeasureIt').style.top = startScrollYMeasureIt+(startYMeasureIt-20)+"px";
		else
			document.getElementById('divCoordMeasureIt').style.top = startScrollYMeasureIt+startYMeasureIt+"px";
		
		if (currentXMeasureIt>screen.width-130)
			document.getElementById('divCoordMeasureIt').style.left = startScrollXMeasureIt+(screen.width-130)+"px";
		else {
			document.getElementById('divCoordMeasureIt').style.left = startScrollXMeasureIt+(currentXMeasureIt+5)+"px";
		}
		
		document.getElementById("divCoordMeasureIt").style.display = "block";
		document.getElementById("divRectangleMeasureIt").style.display = "block";
	}
}
function mouseDownShadowMeasureIt() {
	startXMeasureIt = window.event.clientX;
	startYMeasureIt = window.event.clientY;
	startScrollXMeasureIt = document.body.scrollLeft;
	startScrollYMeasureIt = document.body.scrollTop;
	isMoveMeasureIt = true;
}
function mouseUpShadowMeasureIt() {
	isMoveMeasureIt = false;
}