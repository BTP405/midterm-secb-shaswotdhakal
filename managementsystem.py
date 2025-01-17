"""
Module: management_system.py

This module contains classes for managing employees, projects, and tasks in a fictional company.

Classes:
    - Employee: Represents an employee in the company.
    - Project: Represents a project in the company.
    - Task: Represents a task in the company.
    - ManagementSystem: Provides functionality to manage employees, projects, and tasks.
"""

class ManagementSystem:
 
    """
    Class representing a management system for employees, projects, and tasks in the company.

    Attributes:
        employees (list): List of employees in the system.
        projects (list): List of projects in the system.
        tasks (list): List of tasks in the system.
    """

    def __init__(self):
        self.employees = []
        self.projects = []
        self.tasks = []
        
        """
        Initialize a ManagementSystem object.
        """
        pass

    def add_employee(self, employee):
        self.employees.append(employee)
        """
        Add an employee to the management system.

        Args:
            employee (Employee): The employee to be added.
        """
        pass

    def remove_employee(self, emp_id):
        """
        Remove an employee from the management system.

        Args:
            emp_id (str): The ID of the employee to be removed.
        """
        self.employees = [e for e in self.employees if e.emp_id != emp_id]
        

        pass

    def add_project(self, project):
        self.projects.append(project)
        """
        Add a project to the management system.

        Args:
            project (Project): The project to be added.
        """
        pass

    def add_task(self, task):
        self.tasks.append(task)
        """
        Add a task to the management system.

        Args:
            task (Task): The task to be added.
        """
        pass

    def assign_employee_to_project(self, emp_id, project_id):
        
        """
        Assign an employee to a project.

        Args:
            emp_id (str): The ID of the employee to be assigned.
            project_id (str): The ID of the project to which the employee will be assigned.
        
        Raises:
            ValueError: If employee or project is not found.
        """
        employee = next((e for e in self.employees if e.emp_id == emp_id), None)
        project = next((p for p in self.projects if p.project_id == project_id), None)
        if employee is None or project is None:
            raise ValueError("Employee or project not found")
        project.employees.append(employee)
        
        pass

