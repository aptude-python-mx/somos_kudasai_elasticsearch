from somos_kudasai.site import Somos_kudasai as Somos_kudasai_base
from .article import Article


class Somos_kudasai( Somos_kudasai_base ):
    @property
    def article_class( self ):
        return Article
