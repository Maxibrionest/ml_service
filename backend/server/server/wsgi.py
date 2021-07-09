"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.value_boston_housing.decision_tree import DecisionTreeRegressor
from apps.ml.value_boston_housing.random_forest_a import RandomForestA
from apps.ml.value_boston_housing.random_forest_b import RandomForestB



try:
	registry = MLRegistry() # create ML registry
	# Decision Tree Regressor
	dtr = DecisionTreeRegressor()
	# add to ML registry
	registry.add_algorithm(endpoint_name="value_boston_housing",
							algorithm_object=dtr,
							algorithm_name="Decision Tree",
							algorithm_status="production",
							algorithm_version="0.1",
							owner="Maximiliano Briones Troncoso",
							algorithm_description="Decision Tree, considera {'rm', 'ptratio', 'lstat'}",
							algorithm_code=inspect.getsource(DecisionTreeRegressor))

	# Random Forest A
	rf_a = RandomForestA()
	# add to ML registry
	registry.add_algorithm(endpoint_name="value_boston_housing",
							algorithm_object=rf_a,
							algorithm_name="Random Forest A",
							algorithm_status="production",
							algorithm_version="0.1",
							owner="Maximiliano Briones Troncoso",
							algorithm_description="RandomForest, test_size=0.3, considera {'rm', 'ptratio', 'lstat'}",
							algorithm_code=inspect.getsource(RandomForestA))

	# Random Forest B
	rf_b = RandomForestB()
	# add to ML registry
	registry.add_algorithm(endpoint_name="value_boston_housing",
							algorithm_object=rf_b,
							algorithm_name="Random Forest B",
							algorithm_status="production",
							algorithm_version="0.1",
							owner="Maximiliano Briones Troncoso",
							algorithm_description="RandomForest, test_size=0.2, considera {'rm', 'ptratio', 'lstat'}",
							algorithm_code=inspect.getsource(RandomForestB))

except Exception as e:
	print("Exception while loading the algorithms to the registry,", str(e))