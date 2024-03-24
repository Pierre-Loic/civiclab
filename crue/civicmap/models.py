from django.db import models

class Vigicrue(models.Model):
    niveau_alerte = models.IntegerField(unique=True)
    time = models.CharField(max_length=20)
    main_color = models.CharField(max_length=20)
    color_4 = models.CharField(max_length=20)
    color_3 = models.CharField(max_length=20)
    color_2 = models.CharField(max_length=20)
    color_1 = models.CharField(max_length=20)
    text = models.CharField(max_length=20)
    full_text = models.CharField(max_length=20)

    def __str__(self):
        return str(self.niveau_alerte)

class Station(models.Model):
    code = models.CharField(max_length=30, unique=True)
    nom = models.CharField(max_length=200)
    riviere = models.CharField(max_length=100)
    hauteur_max = models.FloatField(null=True, blank=True)
    debit_max = models.FloatField(null=True, blank=True)
    date_max = models.DateField(null=True, blank=True)
    hauteur = models.FloatField(null=True, blank=True)
    debit = models.FloatField(null=True, blank=True)
    date_hauteur = models.DateField(null=True, blank=True)
    niveau_alerte = models.ForeignKey(Vigicrue, on_delete=models.CASCADE, to_field='niveau_alerte', related_name='station')
    date_alerte = models.DateField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nom

class RepereCrue(models.Model):
    id_gsheet = models.IntegerField(unique=True)
    nom = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    presentation_crue = models.TextField(null=True, blank=True)
    contexte = models.TextField(null=True, blank=True)
    impact_humain_urbain = models.TextField(null=True, blank=True)
    photo1 = models.URLField(null=True, blank=True)
    photo2 = models.URLField(null=True, blank=True)
    photo3 = models.URLField(null=True, blank=True)
    video1 = models.URLField(null=True, blank=True)
    video2 = models.URLField(null=True, blank=True)
    en_savoir_plus = models.URLField(null=True, blank=True)
    code_station = models.ForeignKey(Station, on_delete=models.CASCADE, to_field='code', related_name='reperes_crues')

    def __str__(self):
        return self.nom