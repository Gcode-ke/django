import os
from django.contrib.gis.utils import LayerMapping
from .models import *

maps_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'daily_kwh': 'Daily_Kwh',
    'f_tariff': 'F_tariff',
    'tariff_kwh': 'Tariff_kwh',
    'd_revenue': 'D_Revenue',
    'total_rev': 'Total_rev',
    'geom': 'MULTIPOINT25D',
}
maps_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data', 'Urban_plot_point.shp'),)


def run1(verbose=True):
    lm = LayerMapping(
        Urban_plot_point, maps_shp, maps_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


maps_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'clamped': 'Clamped',
    'extruded': 'Extruded',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON25D',
}

maps_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data', 'Urban_plot.shp'), )


def run2(verbose=True):
    lm = LayerMapping(
        Urban_plot, maps_shp, maps_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


maps_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'revenue': 'Revenue',
    'geom': 'MULTIPOINT25D',
}
maps_shp = os.path.abspath(os.path.join(os.path.dirname(
    __file__), 'data', 'Secondary_substation.shp'),)


def run3(verbose=True):
    lm = LayerMapping(
        Secondary_substation, maps_shp, maps_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


maps_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'total_rev': 'Total_Rev',
    'geom': 'MULTIPOINT25D',
}
maps_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data', 'Primary_substation.shp'),)


def run4(verbose=True):
    lm = LayerMapping(
        Primary_substation, maps_shp, maps_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


maps_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'geom': 'MULTIPOINT25D',
}
maps_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data', 'MV_pole.shp'),)


def run5(verbose=True):
    lm = LayerMapping(
        MV_pole, maps_shp, maps_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


maps_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'clamped': 'Clamped',
    'extruded': 'Extruded',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING25D',
}
maps_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data', 'MV_line_section.shp'),)


def run6(verbose=True):
    lm = LayerMapping(
        MV_line_section, maps_shp, maps_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


maps_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'geom': 'MULTIPOINT25D',
}
maps_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data', 'LV_polest.shp'),)


def run7(verbose=True):
    lm = LayerMapping(
        LV_polest, maps_shp, maps_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


maps_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'geom': 'MULTIPOINT25D',
}
maps_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data', 'LV_pole.shp'),)


def run8(verbose=True):
    lm = LayerMapping(
        LV_pole, maps_shp, maps_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


maps_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'clamped': 'Clamped',
    'extruded': 'Extruded',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING25D',
}
maps_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data', 'LV_line_section.shp'),)


def run9(verbose=True):
    lm = LayerMapping(
        LV_line_section, maps_shp, maps_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


run1()
