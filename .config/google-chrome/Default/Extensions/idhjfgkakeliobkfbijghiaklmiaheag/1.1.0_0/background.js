chrome.tabs.onCreated.addListener(function(tab) {
	chrome.windows.getCurrent(function(window) {
		localStorage['isViewMeasureIt'+tab.id]=false;
	});
});

chrome.tabs.onUpdated.addListener(function(tabId,changeInfo,tab) {
	if ((localStorage['isViewMeasureIt'+tabId]==true) || (localStorage['isViewMeasureIt'+tabId]=="true")) {
		chrome.browserAction.setIcon({path: "off.png",tabId: tabId});
		chrome.browserAction.setTitle({title: "MeasureIt",tabId: tabId});
		localStorage['isViewMeasureIt'+tabId]=false;
	}
});

chrome.browserAction.onClicked.addListener(function(tab) {
	if ((localStorage['isViewMeasureIt'+tab.id]===undefined) || (localStorage['isViewMeasureIt'+tab.id]===null))
		localStorage['isViewMeasureIt'+tab.id]=false;

	if ((localStorage['isViewMeasureIt'+tab.id]==true) || (localStorage['isViewMeasureIt'+tab.id]=="true"))
		localStorage['isViewMeasureIt'+tab.id]=false;
	else
		localStorage['isViewMeasureIt'+tab.id]=true;

	chrome.tabs.getSelected(null, function(tab) {
		chrome.tabs.sendRequest(tab.id, {flag: localStorage['isViewMeasureIt'+tab.id]}, function(response) {

		});
	});
});

chrome.extension.onRequest.addListener(
	function(request, sender, sendResponse) {
		if ((request.myStatusMeasureIt == false) || (request.myStatusMeasureIt == "false")) {
			chrome.browserAction.setIcon({path: "off.png",tabId: sender.tab.id});
			chrome.browserAction.setTitle({title: "MeasureIt",tabId: sender.tab.id});
		}
		else {
			chrome.browserAction.setIcon({path: "on.png",tabId: sender.tab.id});
			chrome.browserAction.setTitle({title: "MeasureIt",tabId: sender.tab.id});
		}
});
function getVersion() {
    var details = chrome.app.getDetails();
    return details.version;
}
if(localStorage['firstUse'] == undefined){
	localStorage['firstUse'] = false;
}