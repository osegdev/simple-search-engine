from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Document:
    id: str
    content: str
    metadata: Optional[Dict[str, str]] = None