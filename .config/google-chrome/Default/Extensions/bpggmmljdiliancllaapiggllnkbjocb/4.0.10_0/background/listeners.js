parcelRequire=function(e,r,t,n){var i,o="function"==typeof parcelRequire&&parcelRequire,u="function"==typeof require&&require;function f(t,n){if(!r[t]){if(!e[t]){var i="function"==typeof parcelRequire&&parcelRequire;if(!n&&i)return i(t,!0);if(o)return o(t,!0);if(u&&"string"==typeof t)return u(t);var c=new Error("Cannot find module '"+t+"'");throw c.code="MODULE_NOT_FOUND",c}p.resolve=function(r){return e[t][1][r]||r},p.cache={};var l=r[t]=new f.Module(t);e[t][0].call(l.exports,p,l,l.exports,this)}return r[t].exports;function p(e){return f(p.resolve(e))}}f.isParcelRequire=!0,f.Module=function(e){this.id=e,this.bundle=f,this.exports={}},f.modules=e,f.cache=r,f.parent=o,f.register=function(r,t){e[r]=[function(e,r){r.exports=t},{}]};for(var c=0;c<t.length;c++)try{f(t[c])}catch(e){i||(i=e)}if(t.length){var l=f(t[t.length-1]);"object"==typeof exports&&"undefined"!=typeof module?module.exports=l:"function"==typeof define&&define.amd?define(function(){return l}):n&&(this[n]=l)}if(parcelRequire=f,i)throw i;return f}({"UscR":[function(require,module,exports) {
const e=chrome||browser,t="GoogleTranslate/Ddict.me";function r(e){const r=[];let s=!1;for(let n=0;n<e.length;n++)"ddict"===e[n].name&&(s=!0),"User-Agent"!=e[n].name?r.push(e[n]):r.push({name:"User-Agent",value:t});return s?r:e}function s(){n||(n=function(e){let t={requestHeaders:e.requestHeaders};return e&&e.url&&e.requestHeaders&&e.requestHeaders.length>0&&(t={requestHeaders:r(e.requestHeaders)}),t}),e.webRequest.onBeforeSendHeaders.addListener(n,{urls:["http://*/*","https://*/*"]},["requestHeaders","blocking"])}let n=null;s();
},{}]},{},["UscR"], null)