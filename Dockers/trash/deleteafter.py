#!/usr/bin/python3

import json

x = "
[
{"target":"http://whiskeyprovsechny.cz","http_status":301,"request_config":{"headers":{"User-Agent":"WhatWeb/0.5.5"}},"plugins":{"Country":{"string":["CZECH REPUBLIC"],"module":["CZ"]},"HTTPServer":{"string":["nginx"]},"IP":{"string":["31.15.10.85"]},"nginx":{},"RedirectLocation":{"string":["https://whiskeyprovsechny.cz/"]},"Title":{"string":["301 Moved Permanently"]}}}
,
{"target":"https://whiskeyprovsechny.cz/","http_status":200,"request_config":{"headers":{"User-Agent":"WhatWeb/0.5.5"}},"plugins":{"Bootstrap":{},"Country":{"string":["CZECH REPUBLIC"],"module":["CZ"]},"Email":{"string":["whiskeybar@turbomost.cz"]},"HTML5":{},"HTTPServer":{"string":["nginx"]},"IP":{"string":["31.15.10.85"]},"JQuery":{"version":["3.2.1"]},"Lightbox":{},"Meta-Author":{"string":["Lidizbaru.cz"]},"nginx":{},"Open-Graph-Protocol":{"version":["website"]},"Script":{},"Title":{"string":["Whiskey bar, který neexistuje – místo pro Váš nejlepší vánoční večírek"]}}}
])

x = json.loads(x)

