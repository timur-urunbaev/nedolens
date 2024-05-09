# import requests
import platform
import getpass
import math
import os
import re
import webbrowser
from datetime import datetime

class Web:
    def __init__(self):
        """
        This class is used for websearch related integrations.
        """
        self.name = "Web"
        self.icon = "edit-copy"

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
        self.icon = "copy-symbolic"
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

    def create_index_db(self):
        if os.path.exists(self.db_name):
            self.conn = sqlite3.connect(self.db_name)
            c = self.conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS files
                         (id INTEGER PRIMARY KEY, path TEXT, size INTEGER)''')
            self.conn.commit()
            self.conn.close()

    def index_filesystem(self, root_dir, db_file):
        self.conn = sqlite3.connect(db_file)
        c = conn.cursor()

        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                size = os.path.getsize(filepath)
                c.execute("INSERT INTO files (path, size) VALUES (?, ?)", (filepath, size))

        conn.commit()
        conn.close()

    def connect_to_db(db_file):
        conn = sqlite3.connect(db_file)
        return conn.cursor()

    def search_files(prefix, cursor):
        cursor.execute("SELECT * FROM files WHERE path LIKE ?", (prefix + '%',))
        return cursor.fetchall()

class Settings:
    def __init__(self):
        self.result = None
        self.name = "Settings"
        self.icon = ""

    def search(self):
        pass
