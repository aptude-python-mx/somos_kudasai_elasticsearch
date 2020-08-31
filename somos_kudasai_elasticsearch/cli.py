# -*- coding: utf-8 -*-
import argparse
import sys
from somos_kudasai_elasticsearch.site import Somos_kudasai
from chibi.config import basic_config
from chibi.file import Chibi_path

parser = argparse.ArgumentParser(
    description="descargar datos de articulos de somoskudasai.com",
    fromfile_prefix_chars='@'
)

parser.add_argument(
    "sites", nargs='+', metavar="site",
    help="urls de los articulos que se quieren descargar" )

parser.add_argument(
    "--log_level", dest="log_level", default="INFO",
    help="nivel de log",
)

parser.add_argument(
    "--reversed", '-r', dest="reversed", action="store_true",
    help="escanea en alrevez", )

parser.add_argument(
    "--config_site", type=Chibi_path, dest="config_site",
    help="python, yaml o json archivo de config"
)


def prepare():
    from somos_kudasai_elasticsearch.models import Article

    if not Article._index.exists():
        Article.init()


def main():
    args = parser.parse_args()
    basic_config( args.log_level )
    if args.config_site:
        load_config( args.config_site )

    prepare()
    somos_kudasai = Somos_kudasai()

    for article in somos_kudasai:
        article.send_to_es()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
