"""
Module: management_system.py

This module contains classes for managing employees, projects, and tasks in a fictional company.
"""

class Task:
    def __init__(self, task_id, description, deadline, status, project):
        self.task_id = task_id
        self.description = description
        self.deadline = deadline
        self.status = status
        self.project = project
    """
    Class representing a task in the company.

    Attributes:
        task_id (str): The ID of the task.
        description (str): The description of the task.
        deadline (str): The deadline of the task.
        status (str): The status of the task.
        project (Project): The project associated with the task.
    """

    def __init__(self, task_id, description, deadline, status, project):
        self.task_id = task_id
        self.description = description
        self.deadline = deadline
        self.status = status
        self.project = project
        """
        Initialize a Task object.

        Args:
            task_id (str): The ID of the task.
            description (str): The description of the task.
            deadline (str): The deadline of the task.
            status (str): The status of the task.
            project (Project): The project associated with the task.
        """
        pass
