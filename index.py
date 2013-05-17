#!/usr/local/bin/py
import ht
import sys

def htmain():
    ht.printintro()
    print(
        ht.tag("html", content=ht.greshead() +
            ht.tag("body", attributes={"class": "center"}, content=
                ht.grestoolbar() +
                ht.tag("h1", content="Welcome to Progress") +
                (ht.tag("p", content="Please log in. Anonymous access is in the works.") if ht.oid() == None else ht.tag("p", content="Nothing to see here. The ability to create tasks is in the works.")) +
                ht.tag("p", content=ht.tag("a", attributes={"href": "http://fenhl.net/gres/"}, content="What is Progress?"))
            )
        )
    )

if __name__ == "__main__":
    sys.stderr = sys.stdout
    htmain()
