from datetime import datetime, time

from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse
from django.utils import timezone


class ProblemSetQuerySet(models.QuerySet):
    def for_user(self, user):
        # TODO: real permission check
        return self.filter(is_public=True)

    def only_current(self):
        return self.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())


class ProblemSet(models.Model):
    id: int
    contest = models.ForeignKey("contests.Contest", on_delete=models.CASCADE)
    contest_id: int
    name = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    is_public = models.BooleanField(default=False)

    objects = ProblemSetQuerySet.as_manager()

    class Meta:
        ordering = ["start_date", "end_date"]

    def __str__(self):
        return self.name

    @property
    def end_date_time(self):
        return datetime.combine(self.end_date, time(hour=23, minute=59, second=59))


class Problem(models.Model):
    id: int
    name = models.CharField(blank=True, max_length=256)
    number = models.IntegerField(default=0)
    problem_set = models.ForeignKey(
        ProblemSet, on_delete=models.CASCADE, related_name="problems"
    )
    problem_set_id: int

    class Meta:
        ordering = ["problem_set", "number"]

    def __str__(self):
        return f"{self.number}. {self.name}"

    def get_absolute_url(self):
        return reverse(
            "problem_detail",
            kwargs={"problem_set_id": self.problem_set_id, "number": self.number},
        )

    def get_texts(self):
        texts = self.text_set.all()
        text_types = {}

        for text in texts:
            text_types[text.type] = text

        return text_types


class Text(models.Model):
    class Type(models.TextChoices):
        PROBLEM_STATEMENT = "PS", "Problem statement"
        EXAMPLE_SOLUTION = "ES", "Example solution"
        SUSI_SMALL_HINT = "SSH", "Susi small hint"
        SUSI_LARGE_HINT = "SLH", "Susi large hint"

    text = models.TextField(blank=True)
    type = models.CharField(choices=Type, max_length=3)
    problem = models.ForeignKey(
        Problem, on_delete=models.CASCADE, related_name="text_set"
    )

    class Meta:
        ordering = ["problem", "type"]
        constraints = [
            UniqueConstraint("problem", "type", name="text__unique_problem_type")
        ]

    def __str__(self):
        return f"{self.problem}({self.type})"
