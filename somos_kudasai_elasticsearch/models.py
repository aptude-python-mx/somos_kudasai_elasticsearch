#!/usr/bin/env python3
import sys
import fileinput
import json
from elasticsearch_dsl import Document, field, InnerDoc
import logging


logger = logging.getLogger( 'somos_kudasai_elasticsearch.models.article' )


from elasticsearch_dsl import analyzer, tokenizer

category = analyzer(
    'category',
    tokenizer=tokenizer( 'trigram', 'nGram', min_gram=3, max_gram=3 ),
    filter=[ "lowercase", ],
)

titles = analyzer(
    'titles',
    tokenizer=tokenizer( 'trigram', 'nGram', min_gram=3, max_gram=5 ),
    filter=[ "lowercase", ],
)

titles_space = analyzer(
    'titles_space',
    tokenizer='whitespace',
    filter=[ "lowercase", ],
)


class Article( Document ):
    title = field.Text(
        analyzer=titles, multi=True,
        fields={
            'space': field.Text( analyzer=titles_space, multi=True ),
            'keyword': field.Keyword( multi=True ),
        } )
    text = field.Text(
        analyzer=titles, multi=True,
        fields={
            'space': field.Text( analyzer=titles_space, multi=True ),
            'keyword': field.Keyword( multi=True ),
        } )
    category = field.Text(
        analyzer=category, multi=True,
        fields={
            'keyword': field.Keyword( multi=True ),
        } )
    create_at = field.Date()
    upload_at = field.Date()
    scan_at = field.Date()
    url = field.Keyword()

    class Index:
        name = 'somos_kudasai__articles'
        settings = { 'number_of_shards': 2, 'number_of_replicas': 1 }

    @classmethod
    def url_is_scaned( cls, url ):
        logger.info( f"buscando articulo {url}" )
        if cls.search().filter( "term", url=url ).count() > 0:
            return True
        return False

    def save( self, *args, **kw ):
        super().save( *args, **kw )
