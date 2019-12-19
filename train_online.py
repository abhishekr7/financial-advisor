from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
#from rasa_core.train import online
from rasa_core.utils import EndpointConfig
from rasa_core.training import interactive

import rasa_core

logger = logging.getLogger(__name__)


def run_weather_online(input_channel, interpreter,
                          domain_file="weather_domain.yml",
                          training_data_file='data/stories.md'):

    action_endpoint = EndpointConfig(url = "http://localhost:5056/webhook")
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=interpreter,
                  action_endpoint = action_endpoint)

    data = agent.load_data(training_data_file)

    agent.train(data)

    interactive.run_interactive_learning(agent)
    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
    run_weather_online('cmdline', nlu_interpreter)
