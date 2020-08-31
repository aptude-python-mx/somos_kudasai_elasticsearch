from somos_kudasai.article import Article as Article_base
from somos_kudasai_elasticsearch.models import Article as Article_model


class Article( Article_base ):
    def send_to_es( self ):
        if not Article_model.url_is_scaned( self.url ):
            model = Article_model( **self.info )
            model.save()
