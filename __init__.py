# Importando libs externas
import importlib
# Importando as funções do pacote
from .  import post_messages
# Para permitir que mudanças passem a ser usadas diretamente
importlib.reload(post_messages)