from django.urls import reverse

from seminare.problems.models import Problem, ProblemSet
from seminare.style.tables import Table


class ProblemSetTable(Table):
    fields = [
        "name",
        "start_date",
        "end_date",
    ]

    labels = {
        "name": "Názov",
        "start_date": "Začiatok",
        "end_date": "Koniec",
    }

    def get_links(
        self, object: ProblemSet, context: dict
    ) -> list[tuple[str, str] | tuple[str, str, str]]:
        return [
            (
                "mdi:cards",
                "Úlohy",
                reverse("org:problem_list", args=[object.contest_id, object.id]),
            ),
            (
                "mdi:pencil",
                "Upraviť",
                reverse("org:problemset_update", args=[object.contest_id, object.id]),
            ),
        ]


class ProblemTable(Table):
    fields = [
        "name",
        "number",
        "problem_set",
    ]

    labels = {
        "name": "Názov",
        "number": "Číslo úlohy",
        "problem_set": "Sada úloh",
    }

    # TODO link na opravovanie
    def get_links(
        self, object: Problem, context: dict
    ) -> list[tuple[str, str] | tuple[str, str, str]]:
        return [
            (
                "mdi:pencil",
                "Upraviť",
                reverse(
                    "org:problem_update",
                    args=[
                        object.problem_set.contest_id,
                        object.problem_set_id,
                        object.id,
                    ],
                ),
            )
        ]
