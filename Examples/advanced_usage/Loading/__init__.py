# loading/__init__.py

from . import load_document_from_local_disc
from . import load_document_from_stream
from . import load_text_from_string

__all__ = [
    'load_document_from_local_disc', 
    'load_document_from_stream', 
    'load_text_from_string'
    ]
