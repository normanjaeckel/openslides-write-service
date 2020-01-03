from ...utils.routing import RuleFactory
from ...utils.types import Environment
from .views import get_get_rules_func


class TopicRuleFactory(RuleFactory):
    """
    Rule factory for simple topics that can be shown in agenda.

    During initialization we bind the get_rules method from apps's views.
    """

    def __init__(self, environment: Environment) -> None:
        self.get_rules_func = get_get_rules_func(environment)