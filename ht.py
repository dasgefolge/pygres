#!/usr/local/bin/py

import cgi
import os

def oid():
    return os.environ.get("REMOTE_USER", None)

def query():
    return cgi.parse_qs(os.environ.get("QUERY_STRING", ""))

def header(logout=False):
    ret = "Content-type: text/html\n"
    # from http://stackoverflow.com/questions/404617/disabling-the-browser-cache-in-php-or-using-javascript
    ret += "Expires: Tue, 01 Jan 2000 00:00:00 GMT\n"
    ret += "Cache-Control: no-store, no-cache, must-revalidate, max-age=0\n"
    ret += "Cache-Control: post-check=0, pre-check=0\n"
    ret += "Pragma: no-cache\n"
    if logout:
        ret += "Set-Cookie: open_id_session_id=logout; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/id/\n"
        newquery = os.environ.get("QUERY_STRING", "").replace("logout=1&", "").replace("logout=1", "")
        ret += "Refresh: 1;url=" + (lambda x: "/" if x == "/index.py" else x)(os.environ.get("SCRIPT_NAME", "/")) + ("" if newquery == "" else "?") + newquery + "\n"
    return ret

def doctype():
    return "<!DOCTYPE html>"

def tag(name, attributes={}, content=None):
    ret = "<" + name
    for attribute, value in attributes.items():
        ret += " " + attribute + "=\"" + cgi.escape(value, quote=True) + "\""
    if content == None:
        ret += " />"
    else:
        ret += ">" + content + "</" + name + ">"
    return ret

def printintro():
    print(header(logout=bool(query().get("logout", False))))
    print(doctype())

def greshead():
    return tag("head", content=
        tag("title", content="Progress") +
        tag("meta", attributes={"charset": "utf-8"}) +
        tag("link", attributes={"rel": "stylesheet", "type": "text/css", "href": "http://fenhl.net/fenhl.css"})
    )

def grestoolbar():
    if oid() == None:
        return tag("div", attributes={"class": "purple center", "style": "border-bottom: 1px solid #60f; padding: 10px; margin: 0;"}, content=
            tag("a", attributes={"href": "/id" + os.environ.get("REQUEST_URI", "/")}, content="log in")
        )
    else:
        return tag("div", attributes={"class": "center", "style": "border-bottom: 1px solid #60f; padding: 10px; margin: 0;"}, content=(
            "You are logged in as " +
            tag("a", attributes={"href": oid()}, content=oid()) +
            " &mdash; " +
            tag("a", attributes={"href": os.environ.get("REQUEST_URI", "/")[3:] + ("&" if "?" in os.environ.get("REQUEST_URI", "") else "?") + "logout=1"}, content="log out")
        )
    )

if __name__ == "__main__":
    printintro()
    print(
        tag("html", content=
            tag("head", content=
                tag("title", content=
                    cgi.escape("Progress: Error 403")
                )
            ) +
            tag("body", content=
                tag("h1", content=
                    cgi.escape("Error 403: Forbidden (Wait, what?)")
                ) + tag("p", content=
                    cgi.escape("You're not supposed to be here. Try the ") +
                    tag("a", attributes={"href": "/"}, content=
                        cgi.escape("main page")
                    ) +
                    cgi.escape(".")
                )
            )
        )
    )
