from utils.utils import read_yaml
from utils.db_utils import execute_query

class CRUDMethods:
    def __init__(self, element_type):
        self.element_type = element_type
        self.config = read_yaml("/Users/nilakay/Desktop/flask2_checkpoint4/config/config.yaml")
        self.columns_str = ', '.join(column for column in self.config[self.element_type]['select']) #
        self.replacements = {"table": self.element_type, "columns":self.columns_str, "placeholders": "","set_clause": ""}

    def add_element(self, new_element):
        columns = self.config[self.element_type]['add'] #
        self.replacements["columns"] = ", ".join(columns)
        self.replacements["placeholders"] = ", ".join(["%s"] * len(new_element))
        execute_query(self.config["add_query"], self.replacements, tuple(new_element[column] for column in columns))

    def update(self, id, updates):
        self.replacements["set_clause"] = ", ".join([f"{k} = %s" for k in updates.keys()])
        values = tuple(updates.values()) + (id,)
        execute_query(self.config["update_query"], self.replacements, values)

    def delete(self, id):
        execute_query(self.config["delete_query"], self.replacements, (id,))

    def filter(self, key, value):
        self.replacements["key"] = key
        if key in self.config[self.element_type]["numerical_keys"]:
            query_template = self.config["filter_query1"]
            params = (value,)
        else:
            query_template = self.config["filter_query2"]
            like_pattern = f"%{value}%"
            params = (like_pattern,)
        return execute_query(query_template, self.replacements, params)

    def get_all_elements(self):
        return execute_query(self.config["list_query"], self.replacements, None)

