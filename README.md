# bsi_crawler

Authors:

    Dmytro Yurchenko

    Daryna Kovyrina

Techniques:

    Beautiful Soup:
    1. provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree: a toolkit for dissecting a document and extracting what you need. It doesn't take much code to write an application
    2. automatically converts incoming documents to Unicode and outgoing documents to UTF-8. You don't have to think about encodings, unless the document doesn't specify an encoding and Beautiful Soup can't detect one. Then you just have to specify the original encoding.
    3. is on top of popular Python parsers like lxml and html5lib, allowing you to try out different parsing strategies or trade speed for flexibility.
    
    Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server.
    They are the real backbones behind web browsing. In simpler terms there is a server and a client.

Web crawler source:
    bs4.BeautifulSoup package
    socket package

Other resources:
    https://www.crummy.com/software/BeautifulSoup/
    https://docs.python.org/3/library/socket.html

# Summary
    Beautiful Soup is a Python library for pulling data out of HTML and XML files. 
    It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 
    It commonly saves programmers hours or days of work.
    nternet-connected applications that need to operate in realtime greatly benefit from the implementation of sockets in their networking code. 
    Sockets may be implemented over a number of different channel types: Unix domain sockets, TCP, UDP, and so on.