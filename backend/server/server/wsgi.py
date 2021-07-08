"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.value_boston_housing.decision_tree import DecisionTreeRegressor

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()




try:
	registry = MLRegistry() # create ML registry
	# Random Forest classifier
	dt = DecisionTreeRegressor()
	# add to ML registry
	registry.add_algorithm(endpoint_name="value_boston_housing",
							algorithm_object=dt,
							algorithm_name="Decision Tree",
							algorithm_status="production",
							algorithm_version="0.1",
							owner="Maximiliano Briones Troncoso",
							algorithm_description="Decision Tree, considera {'rm', 'ptratio', 'lstat'}",
							algorithm_code=inspect.getsource(DecisionTreeRegressor))

except Exception as e:
	print("Exception while loading the algorithms to the registry,", str(e))