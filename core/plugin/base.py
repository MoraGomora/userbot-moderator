from .register import PluginCommandRegister
from .log import PluginLog

class PluginBase(PluginLog):
    """
    Base class for all plugins.
    This class provides a common interface for loading, managing plugins and register commands.
    """

    def start(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def load(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def register(self, command: PluginCommandRegister):
        raise NotImplementedError("Subclasses should implement this method.")