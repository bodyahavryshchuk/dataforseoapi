from django.db import models


class Task(models.Model):
    """ Task model """
    id = models.CharField(max_length=50, primary_key=True)
    status_code = models.IntegerField()
    status_message = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    cost = models.FloatField()

    def __str__(self):
        return self.id


class TaskData(models.Model):
    """ Task data model """
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name="data"
    )
    api = models.CharField(max_length=50)
    function = models.CharField(max_length=50)
    se = models.CharField(max_length=50)
    se_type = models.CharField(max_length=50)
    language_code = models.CharField(max_length=50)
    location_code = models.CharField(max_length=50)
    keyword = models.CharField(max_length=200)
    device = models.CharField(max_length=50)
    os = models.CharField(max_length=50)

    def __str__(self):
        return str(self.task)


class TaskResult(models.Model):
    """ Task result model """
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="result"
    )
    type = models.CharField(max_length=50)
    rank_group = models.IntegerField()
    rank_absolute = models.IntegerField()
    domain = models.CharField(max_length=100)
    title = models.CharField(max_length=400)
    description = models.TextField(null=True)
    url = models.URLField(max_length=400)
    breadcrumb = models.CharField(max_length=400)

    def __str__(self):
        return str(self.task)
