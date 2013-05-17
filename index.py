#!/usr/local/bin/py
import ht
import sys

def htmain():
    ht.printintro()
    print(
        ht.tag("html", content=ht.greshead() +
            ht.tag("body", attributes={"class": "center"}, content=
                ht.grestoolbar() +
                ht.tag("h1", content=
                    ht.tag("a", attributes={"href": "http://fenhl.net/gres/"}, content="Progress") +
                    " test implementation"
                ) +
                ht.tag("p", content="Coming soon!")
            )
        )
    )

if __name__ == "__main__":
    sys.stderr = sys.stdout
    htmain()
