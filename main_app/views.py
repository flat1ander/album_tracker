from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = "about.html"

class Album:
    def __init__(self, name, artist, image, info):
        self.name = name
        self.artist = artist
        self.image = image
        self.info = info
    
albums = [
  Album("Fun House", "The Stooges", "https://m.media-amazon.com/images/I/81WBfQUaksL._AC_UY436_FMwebp_QL65_.jpg",
          "Fun House is the second studio album by American rock band The Stooges. It was released on July 7, 1970, by Elektra Records. Though initially commercially unsuccessful, Fun House developed a strong cult following. Like it's predecessor (1969's The Stooges) and its successor (1973's Raw Power) it is generally considered integral in the development of punk rock"),
  Album("Future Me Hates Me", "The Beths",
          "https://m.media-amazon.com/images/I/81UF+cfpgQL._AC_UY436_FMwebp_QL65_.jpg", "Future Me Hates Me is the debut studio album by New Zealand indie rock band The Beths. It was produced by the band's lead guitarist Jonathan Pearce and released on Carpark Records label on August 10th, 2018."),
  Album("Transformer", "Lou Reed",
          "https://m.media-amazon.com/images/I/61Gsn9nePPL._AC_UY436_FMwebp_QL65_.jpg", "Transformer is the second solo studio album by American recording artist Lou Reed. Produced by David Bowie and Mick Ronson, the album was released on November 1972 by RCA Records. It is considered an influential landmark of the glam rock genre."),
  Album("Smoke Ring for My Halo", "Kurt Vile",
          "https://m.media-amazon.com/images/I/91Bpyl19vkS._AC_UY436_FMwebp_QL65_.jpg", "Smoke Rin for My Halo is the fourth studio album by American indie rock musician Kurt Vile, released on March 8, 2011 on Matador. The album was released to critical aclaim upon it's release."),
  Album("Something More Than Free", "Jason Isbell",
          "https://m.media-amazon.com/images/I/418sTXuSdCL._AC_UY436_FMwebp_QL65_.jpg", "Something More Than Free is the fifth sutdio album from Jason Isbell, released on July 17, 2015. It was produced by Dave Cobb who had produced Isbell's previous record Southeastern. At the 58th annual Grammy Awards, the album won the award for the Best Americana Album and the song '24 Frames' won the award for Best American Roots Song."),
  Album("Slanted and Enchanted", "Pavement",
          "https://m.media-amazon.com/images/I/81e8OyML7aL._AC_UY436_FMwebp_QL65_.jpg", "Slanted and Enchanted is the debut studio album by American indie rock band PAvement, released on April 20, 1992, by Matador Records. It is the only Pavement album to feature drummer Gary Young. The album received critical acclaim and is seen as a landmark for indie rock with Rolling Stone ranking it 199th on the 500 greatest Albums of All Time."),
  Album("On the Beach", "Neil Young",
          "https://m.media-amazon.com/images/I/51q-aXge42L._AC_UY436_FMwebp_QL65_.jpg", "On the Beach is the 5th studio album by Canadian-American musician Neil Young, released by Reprise Records in July 1974. The album is the second of the so-called 'Ditch Trilogy' of albums that Young recorded following the major success of 1972's Harvest, whereupon the scope of his success and accllaim became apparent; On the BEach was inspired by his feelings of retreat, alienation, and melancholy in reposnse to his success."),
   Album("The Boatman's Call", "Nick Cave and the Bad Seeds",
          "https://m.media-amazon.com/images/I/81sw5wK+y4L._AC_UY436_FMwebp_QL65_.jpg", "The Boatman's Call is the tenth studio album by Nick Cave and the Bad Seeds, released in 1997. The album is entirely piano-based, alternately somber and romantic in mood, making it a marked departure formt he bulk of the band's post-punk catalogue up to that point. The Boatman's Call remains one of the most critically acclaimed releases of Nick Cave's career."),         
]

class AlbumsList(TemplateView):
    template_name = "albums_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = albums
        return context
