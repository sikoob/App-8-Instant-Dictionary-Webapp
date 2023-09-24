import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
                Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
                sed diam nonumy eirmod tempor invidunt ut labore et dolore 
                magna aliquyam erat, sed diam voluptua. At vero eos et accusam et 
                justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea t
                akimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor 
                sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
                invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
                """, classes="text-lg")
        return wp




