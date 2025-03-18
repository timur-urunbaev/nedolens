# import requests
import platform
import math
import os
import re
import webbrowser
import subprocess
from datetime import datetime

class Web:
    def __init__(self):
        """
        This class is used for websearch related integrations.
        """
        self.name = "Web"
        self.icon = "folder-saved-search-symbolic"

    def search(self, text):
        query = text.split()
        webbrowser.open(f"https://www.google.com/search?q={'+'.join(query)}")

class Calculator:
    def __init__(self):
        """
        This class is used for calculator related integrations.
        """
        # Define the patterns
        number_pattern = r"[+-]?\d+(\.\d+)?([eE][+-]?\d+)?"
        pi_pattern = r"pi"

        function_pattern = r"(sin|cos|tan|exp|log)"
        parentheses_pattern = r"\((.*?)\)"

        self.name = "Calculator"
        self.icon = "accessories-calculator-symbolic"
        self.pattern = rf"{number_pattern}|{function_pattern}\({number_pattern}|{pi_pattern}"

    def calculate(self, expression):
        # Replace 'pi' with its numeric value
        expression = expression.replace('pi', str(math.pi))
        # Replace 'sin', 'cos', 'tan' with the respective math functions
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        # Replace 'asin', 'acos', 'atan' with the respective math functions
        expression = expression.replace('asin', 'math.asin')
        expression = expression.replace('acos', 'math.acos')
        expression = expression.replace('atan', 'math.atan')
        # Replace 'exp', 'sqrt', 'log', 'log10', 'factorial' with the respective math functions
        expression = expression.replace('exp', 'math.exp')
        expression = expression.replace('sqrt', 'math.sqrt')
        expression = expression.replace('log', 'math.log')
        expression = expression.replace('log10', 'math.log10')
        expression = expression.replace('factorial', 'math.factorial')
        try:
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

class Calendar:
    def __init__(self):
        """
        This class is used for calendar related integrations.
        """
        self.name = "Calendar"
        self.icon = "external-link-symbolic"
        self.pattern = r"\d{1,2}[-./]\d{1,2}[-./]\d{2,4}"

    def get_day_of_week(self, match):
        try:
            date_obj = datetime.strptime(f"{match.group(1)}-{match.group(2)}-{match.group(3)}", "%d-%m-%Y")
            day_of_week = date_obj.strftime("%A")
            return day_of_week
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD format."

class Weather:
    def __init__(self):
        self.result = None
        self.name = "Weather"
        self.icon = "weather-overcast-symbolic"

class Clock:
    def __init__(self):
        self.result = None
        self.name = "Clock"
        self.icon = ""

class Contacts:
    def __init__(self):
        self.result = None
        self.name = "Contacts"
        self.icon = ""

class Files:
    def __init__(self):
        self.conn = None
        self.db_name = "index.sqlite"
        self.name = "Files"
        self.icon = "external-link-symbolic"

    def search(self, query):
        results = []

        # Run the tracker3 command to search for files and directories
        search_command = f"tracker3 search {query}"
        process = subprocess.Popen(search_command.split(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f"Error during search: {stderr.decode('utf-8')}")
            return results

        # Parse the output
        for line in stdout.decode('utf-8').split('\n'):
            if line:
                path = line.strip()
                name = path.split('/')[-1]
                if '.' in name:  # crude way to distinguish between files and directories
                    file_type = 'File'
                    icon = 'text-x-generic-symbolic'
                else:
                    file_type = 'Directory'
                    icon = 'folder-symbolic'
                results.append({'path': path, 'name': name, 'type': file_type, 'icon': icon})

        return results

class Settings:
    def __init__(self):
        self.result = None
        self.name = "Settings"
        self.icon = ""

    def search(self):
        pass
