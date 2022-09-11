from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    company = models.CharField(max_length=200, verbose_name="Empresa", null=True, blank=True)
    description = models.TextField(verbose_name="Descripción")
    jobs_1 = models.CharField(max_length=400, verbose_name="Primer trabajo", null=True, blank=True)
    jobs_2 = models.CharField(max_length=400, verbose_name="Segundo trabajo", null=True, blank=True)
    jobs_3 = models.CharField(max_length=400, verbose_name="Tercer trabajo", null=True, blank=True)
    jobs_4 = models.CharField(max_length=400, verbose_name="Cuarto trabajo", null=True, blank=True)
    jobs_5 = models.CharField(max_length=400, verbose_name="Quinto trabajo", null=True, blank=True)
    location = models.CharField(max_length=200, verbose_name="Lugar", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Dirección web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title
