from django.contrib.gis.db import models


class Urban_plot_point(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    daily_kwh = models.FloatField()
    f_tariff = models.FloatField()
    tariff_kwh = models.FloatField()
    d_revenue = models.FloatField()
    total_rev = models.FloatField()
    geom = models.MultiPointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Urban_plot_point"


class Urban_plot(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Urban_plot"


class Secondary_substation(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    revenue = models.FloatField()
    geom = models.MultiPointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Secondary_substation"


class Primary_substation(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    total_rev = models.FloatField()
    geom = models.MultiPointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Primary_substation"


class MV_pole(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    geom = models.MultiPointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "MV_pole"


class MV_line_section(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "MV_line_section"


class LV_polest(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    geom = models.MultiPointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "LV_polest"


class LV_pole(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    geom = models.MultiPointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "LV_pole"


class LV_line_section(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "LV_line_section"
