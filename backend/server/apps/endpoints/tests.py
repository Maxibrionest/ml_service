from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient

class EndpointTests(TestCase):

	def test_predict_view(self):
		client = APIClient()

		input_data = {
		"rm":6.998,
		"ptratio":18.7,
		"lstat":2.94
		}

		classifier_url = "/api/v1/value_boston_housing/predict"

		response = client.post(classifier_url, input_data, format='json')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data["medv"], 34.537499999999994)
		self.assertTrue("request_id" in response.data)
		self.assertTrue("status" in response.data)