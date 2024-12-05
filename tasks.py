from celery import Celery

# Create a Celery app instance with Redis as both the broker and result backend
app = Celery('tasks', 
             broker='redis://localhost:6379/0',  # Redis as the message broker
             backend='redis://localhost:6379/0')  # Redis as the result backend

# Define tasks
@app.task
def add(x, y):
    print(f"Adding {x} and {y}")
    return x + y

@app.task
def simple_task():
    print("Task is running")
    return "Task Completed"
