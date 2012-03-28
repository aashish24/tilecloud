from tilecloud.layout.template import TemplateTileLayout
from tilecloud.store.url import URLTileStore


tile_store = URLTileStore(
        (TemplateTileLayout('http://%s.tile.stamen.com/watercolor/%%(z)d/%%(x)d/%%(y)d.jpg' % server) for server in 'abcd'),
        attribution='Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.',
        content_type='image/png')