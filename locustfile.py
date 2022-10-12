from locust import HttpUser, between, task, events

class MyLocust(HttpUser):
    wait_time = between(1, 3)

    @task
    def ibm(self):
        self.client.get('www.google.com')
    
    @task
    def msft(self):
        self.client.get('www.amazon.com')