from tasks import simple_task

# Call the task asynchronously
result = simple_task.delay()

# Wait for the result and print it
print(result.get(timeout=10))  # This will print "Task Completed" after the task is processed.
