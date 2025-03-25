from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def hello_world(self):
        self.client.get("http://127.0.0.1:8000/")
    
    @task(2)
    def nocodb(self):
        self.client.get("http://127.0.0.1:8000/nocodb-data/")

    @task(3)
    def polls(self):
        self.client.get("http://127.0.0.1:8000/api/questions/")

    @task(4)
    def admin(self):
        self.client.post("http://127.0.0.1:8000/admin/login/?next=/admin/", {"username": "admin", "password": "123123"})

    @task(5)
    def polls(self):
        self.client.get("http://127.0.0.1:8000/api/choices/")

    @task(6)
    def api(self):
        self.client.get("http://127.0.0.1:8000/api/")

    @task(7)
    def polls(self):
        self.client.get("http://127.0.0.1:8000/api/users/")
    
    @task(8)
    def polls(self):
        self.client.get("http://127.0.0.1:8000/polls/")    

    