import requests
import platform
import getpass
import math
import webbrowser
from datetime import datetime

class Web:
    def __init__(self, text):
        """
        This class is used for websearch related integrations.
        """
        self.result =  None
        self.name = "Web"
        self.icon = "external-link-symbolic"
        search(text)

    def search(self, text):
        query = text.split()
        webbrowser.open(f"https://www.google.com/search?q={'+'.join(query)}")

class Calculator:
    def __init__(self, expression):
        """
        This class is used for calculator related integrations.
        """
        self.result = None
        self.name = "Calculator"
        self.icon = "copy-symbolic"
        return self.calculate(expression)

    def calculate(expression):
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
        self.result = None
        self.name = "Calendar"
        self.icon = "external-link-symbolic"

    def get_day_of_week(date_string):
        try:
            # Parse the input date string into a datetime object
            date_obj = datetime.strptime(date_string, "%Y-%m-%d")
            # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
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
        self.result = None
        self.name = "Files"
        self.icon = "external-link-symbolic"

    def search(self, pattern):
        if platform.system() == 'Windows':
            base_path = f'C:\Users\{getpass.getuser()}\'
        elif platform.system() == 'Linux':
            base_path = f'/home/{getpass.getuser()}/'
        for root, dirs, files in os.walk(base_path):
            try:
                for name in dirs + files:
                    if query.lower() in name.lower():
                        self.add_row(os.path.join(root.replace('&', '&amp;'), name.replace('&', '&amp;')), "File" if os.path.isfile(os.path.join(root.replace('&', '&amp;'), name.replace('&', '&amp;'))) else "Directory")
            except PermissionError:
                pass

class Settings:
    def __init__(self):
        self.result = None
        self.name = "Settings"
        self.icon = ""

    def search(self):
        pass
