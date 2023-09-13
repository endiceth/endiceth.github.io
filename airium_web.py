from airium import Airium

filenames = ["index.html", "aboutme.html", "placeholder.html", "placeholder2.html"]

titles = ["Index", "About Me", "Placeholder 1", "Placeholder 2"]

contents = ["<h2>List:</h2><b>Element1</b><br><br><b>Element2</ b><br>Element3<br><br>Element4<br>Element5<br>Element6<br><br>",

"<h2>About Me</h2>Student<br>",

"<h2>Placeholder 1-1</h2>Lorum ipsum something something",

"<h2>Placeholder 2-2</h2>Something something, etc"]
for i in range(4):
    page = Airium()
        
    page('<!DOCTYPE html>')
    with page.html():
        with page.head():
            with page.title():
                page (titles [i])
        with page.body(text="#000000", link="#EAEAFF", vlink="#8888FF"):
            with page.center():
                with page.table(width="45%", bgcolor="#ffffff", border="#000000", style="border-radius: 25px"):
                    with page.tr():
                        with page.td(colspan="2"):
                            with page.center():
                                with page.h1():
                                    page (titles [i])
                    with page.tr():
                        with page.td():
                            with page.center():
                                page('<b>Menu</b><br><a href="aboutme.html">About me</a><br><a href="placeholder.html">Placeholder 1</a><br><a href="placeholder2.html">Placeholder 2</a><br>Empty1<br>Empty2')
                        with page.td():
                            with page.center():
                                page(contents[i])
    
    html_str = str(page)
    
    with open(filenames[i], 'w') as f:
        f.write(html_str)
