from django.test import TestCase

import numpy as np
import inspect

from apps.ml.registry import MLRegistry
from apps.ml.value_boston_housing.decision_tree import DecisionTreeRegressor

class MLTests(TestCase):


    def test_dt_algorithm(self):
        input_data = {
        "rm":6.998,
        "ptratio":18.7,
        "lstat":2.94
        }

        my_alg = DecisionTreeRegressor()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        #self.assertTrue('label' in response)
        self.assertEqual(34.5375, np.around(response['medv'], decimals=4))


    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "value_boston_housing"
        algorithm_object = DecisionTreeRegressor()
        algorithm_name = "Desicion Tree"
        algorithm_status = "production"
        algorithm_version = "0.1"
        algorithm_owner = "Maximiliano Briones Troncoso"
        algorithm_description = "Decision Tree, considera {'rm', 'ptratio', 'lstat'}"
        algorithm_code = inspect.getsource(DecisionTreeRegressor)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)