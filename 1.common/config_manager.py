# Managing configuration settings for simulations

import json
import os

class ConfigManager:
    def __init__(self, config_file_path='config.json'):
        self.config_file_path = config_file_path
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from a JSON file."""
        if not os.path.exists(self.config_file_path):
            return {}

        with open(self.config_file_path, 'r') as file:
            return json.load(file)

    def save_config(self):
        """Save the current configuration to a JSON file."""
        with open(self.config_file_path, 'w') as file:
            json.dump(self.config, file, indent=4)

    def get_config(self, key, default=None):
        """Retrieve a configuration value."""
        return self.config.get(key, default)

    def set_config(self, key, value):
        """Set a configuration value."""
        self.config[key] = value
        self.save_config()

    def update_config(self, updates):
        """Update multiple configuration values."""
        self.config.update(updates)
        self.save_config()
