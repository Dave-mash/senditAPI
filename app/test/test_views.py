"""Tests"""
import unittest
from app import create_app
import json
     
class TestViews(unittest.TestCase):
    """Tests class"""
    def setUp(self):
        """set up method for tests"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app

        self.order = {
            "order_id":"100",
            "pickup_location":"nakuru",
            "destination":"nairobi",
            "price":"1400",
            "user_id":"5"

        }
        self.user = {
            "user_id":"25",
            "firstname":"James",
            "lastname":"Martin",
            "username":"senge",
            "email":"senge@yahoo.com",
            "password":"andela"
        }
    def test_post(self):
        """test create order endpoint"""
        response = self.client.post('/api/v1/parcels', data = json.dumps(self.order), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Order placed Successfully", msg = "Order registration failed")
        self.assertEqual(response.status_code, 201)

    def test_get_one(self):
        """test get single order endpoint"""
        response = self.client.get('/api/v1/parcels/100')
        self.assertEqual(response.status_code, 200)

    def test_put_one(self):
        """test cancel order endpoint"""
        response = self.client.put('/api/v1/parcels/100')
        self.assertEqual(response.status_code, 200)

    def test_get_all(self):
        """test get all orders endpoint"""
        response = self.client.get('/api/v1/parcels')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Success", msg = "No orders to retrieve")
        self.assertEqual(response.status_code, 200)

    def test_get_all_by_one_user(self):
        """test get single user orders endpoint"""
        response = self.client.get('/api/v1/users/5/parcels')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "User does not have orders", msg = "User orders")
        self.assertEqual(response.status_code, 200)

    def test_post_user(self):
        """test create user endpoint"""
        response = self.client.post('/api/v1/users', data = json.dumps(self.user), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "successful registration", msg = "Registration failed")
        self.assertEqual(response.status_code, 201)

   
