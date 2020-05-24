function randomString() {
    var chars = "0123456789";
    var string_length = 7;
    var randomstring = '';
    for (var i = 0; i < string_length; i++) {
        var rnum = Math.floor(Math.random() * chars.length);
        randomstring += chars.substring(rnum, rnum + 1);
    }
    return randomstring;
}

var loadPixel = function () {
    var url = '';
    var refer = '';

    if ('referrer' in document) {
        refer = document.referrer;
    }

    if (typeof ClickMeter_pixel_url !== 'undefined' && ClickMeter_pixel_url != null && ClickMeter_pixel_url != '') {
        var urlWithProtocol = ClickMeter_pixel_url;
        if (urlWithProtocol.indexOf("//") == 0) {
            if (window.location.protocol != "https:") {
                urlWithProtocol = "http:" + ClickMeter_pixel_url;
            } else {
                urlWithProtocol = "https:" + ClickMeter_pixel_url;
            }
        }
		
		var additionalParams = 'c=' + randomString();
		
		if (typeof refer !== 'undefined' && refer != null && refer != '') {
			additionalParams = additionalParams + "&r=" + encodeURIComponent(refer);
		}	
		
		if (urlWithProtocol.indexOf('?') != -1) {
			url = urlWithProtocol + '&' + additionalParams;
		}
		else {
			url = urlWithProtocol + '?' + additionalParams;
		}
    }

    var panel = document.createElement('div');
    panel.setAttribute('id', 'pixel_container');
    panel.style.height = '0px';
    panel.style.width = '0px';
    panel.style.overflow = 'hidden';

    var iFrame = document.createElement('iframe');
    iFrame.setAttribute('src', url);
    iFrame.setAttribute('frameborder', '0');
    iFrame.setAttribute('height', '0');
    iFrame.setAttribute('width', '0');
    iFrame.setAttribute('noresize', '0');
    iFrame.setAttribute('id', 'convframe');
    iFrame.setAttribute('name', 'convframe');
    iFrame.setAttribute('allowtransparency', 'true');
    var scripts = document.getElementsByTagName('script');
    var index = scripts.length - 1;
    var myScript = scripts[index];
    panel.appendChild(iFrame);
    myScript.parentNode.appendChild(panel);

    if (typeof ClickMeter_pixel_url !== 'undefined') {
        ClickMeter_pixel_url = null;
    }
};

loadPixel();