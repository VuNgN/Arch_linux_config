/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "/build/";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 113);
/******/ })
/************************************************************************/
/******/ ({

/***/ 113:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _constants__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(16);
/* global chrome */



let backendDisconnected = false;
let backendInitialized = false;

function sayHelloToBackend() {
  window.postMessage({
    source: 'react-devtools-content-script',
    hello: true,
    extensionId: _constants__WEBPACK_IMPORTED_MODULE_0__[/* CURRENT_EXTENSION_ID */ "a"]
  }, '*');
}

function handleMessageFromDevtools(message) {
  window.postMessage({
    source: 'react-devtools-content-script',
    payload: message,
    extensionId: _constants__WEBPACK_IMPORTED_MODULE_0__[/* CURRENT_EXTENSION_ID */ "a"]
  }, '*');
}

function handleMessageFromPage(evt) {
  if (evt.source === window && evt.data && evt.data.source === 'react-devtools-bridge') {
    backendInitialized = true;
    port.postMessage(evt.data.payload);
  }
}

function handleDisconnect() {
  backendDisconnected = true;
  window.removeEventListener('message', handleMessageFromPage);
  window.postMessage({
    source: 'react-devtools-content-script',
    payload: {
      type: 'event',
      event: 'shutdown'
    },
    extensionId: _constants__WEBPACK_IMPORTED_MODULE_0__[/* CURRENT_EXTENSION_ID */ "a"]
  }, '*');
} // proxy from main page to devtools (via the background page)


const port = chrome.runtime.connect({
  name: 'content-script'
});
port.onMessage.addListener(handleMessageFromDevtools);
port.onDisconnect.addListener(handleDisconnect);
window.addEventListener('message', handleMessageFromPage);
sayHelloToBackend(); // The backend waits to install the global hook until notified by the content script.
// In the event of a page reload, the content script might be loaded before the backend is injected.
// Because of this we need to poll the backend until it has been initialized.

if (!backendInitialized) {
  const intervalID = setInterval(() => {
    if (backendInitialized || backendDisconnected) {
      clearInterval(intervalID);
    } else {
      sayHelloToBackend();
    }
  }, 500);
}

/***/ }),

/***/ 16:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return CURRENT_EXTENSION_ID; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "c", function() { return EXTENSION_INSTALL_CHECK; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "f", function() { return SHOW_DUPLICATE_EXTENSION_WARNING; });
/* unused harmony export CHROME_WEBSTORE_EXTENSION_ID */
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "d", function() { return INTERNAL_EXTENSION_ID; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "e", function() { return LOCAL_EXTENSION_ID; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "b", function() { return EXTENSION_INSTALLATION_TYPE; });
/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * 
 */
const CURRENT_EXTENSION_ID = chrome.runtime.id;
const EXTENSION_INSTALL_CHECK = 'extension-install-check';
const SHOW_DUPLICATE_EXTENSION_WARNING = 'show-duplicate-extension-warning';
const CHROME_WEBSTORE_EXTENSION_ID = 'fmkadmapgofadopljbjfkapdkoienihi';
const INTERNAL_EXTENSION_ID = 'dnjnjgbfilfphmojnmhliehogmojhclc';
const LOCAL_EXTENSION_ID = 'ikiahnapldjmdmpkmfhjdjilojjhgcbf';
const EXTENSION_INSTALLATION_TYPE = CURRENT_EXTENSION_ID === CHROME_WEBSTORE_EXTENSION_ID ? 'public' : CURRENT_EXTENSION_ID === INTERNAL_EXTENSION_ID ? 'internal' : CURRENT_EXTENSION_ID === LOCAL_EXTENSION_ID ? 'local' : 'unknown';

/***/ })

/******/ });