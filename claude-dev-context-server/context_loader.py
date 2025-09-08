#!/usr/bin/env python3
"""
Context Loader Module
Handles loading and caching of framework context files
"""

import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class ContextLoader:
    """Manages loading and caching of context files"""
    
    def __init__(self, config_path: str):
        """Initialize with configuration"""
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self.context_dir = Path(self.config["context_directory"])
        self.cache_file = self.config_path.parent / "data" / "context_cache.json"
        self.cache = self._load_cache()
    
    def _load_config(self) -> Dict:
        """Load server configuration"""
        try:
            with open(self.config_path / "data" / "config.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("Configuration file not found")
    
    def _load_cache(self) -> Dict:
        """Load context cache"""
        try:
            with open(self.cache_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"cached_files": {}, "cache_updated": None}
    
    def _save_cache(self):
        """Persist cache to disk"""
        self.cache["cache_updated"] = datetime.now().isoformat()
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f, indent=2)
    
    def _get_file_hash(self, file_path: Path) -> str:
        """Calculate file content hash"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return hashlib.md5(content.encode()).hexdigest()
        except Exception:
            return ""
    
    def _is_cached_valid(self, file_path: Path, relative_path: str) -> bool:
        """Check if cached version is still valid"""
        if relative_path not in self.cache["cached_files"]:
            return False
        
        cached_entry = self.cache["cached_files"][relative_path]
        current_hash = self._get_file_hash(file_path)
        
        return cached_entry.get("file_hash") == current_hash
    
    def load_context_file(self, relative_path: str) -> Tuple[str, bool]:
        """
        Load context file with caching
        Returns: (content, from_cache)
        """
        file_path = self.context_dir / relative_path
        
        # Check cache validity
        if self._is_cached_valid(file_path, relative_path):
            return self.cache["cached_files"][relative_path]["content"], True
        
        # Load fresh content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update cache
            file_stat = file_path.stat()
            self.cache["cached_files"][relative_path] = {
                "content": content,
                "last_modified": datetime.fromtimestamp(file_stat.st_mtime).isoformat(),
                "file_hash": self._get_file_hash(file_path)
            }
            self._save_cache()
            
            return content, False
            
        except FileNotFoundError:
            # Return cached version with warning if available
            if relative_path in self.cache["cached_files"]:
                return self.cache["cached_files"][relative_path]["content"], True
            raise FileNotFoundError(f"Context file not found: {relative_path}")
    
    def load_session_context(self, session_type: str) -> Dict:
        """Load context for specific session type"""
        if session_type not in self.config["context_files"]:
            raise ValueError(f"Unknown session type: {session_type}")
        
        context_file = self.config["context_files"][session_type]
        content, from_cache = self.load_context_file(context_file)
        
        # Also load startup process
        startup_content, startup_cached = self.load_context_file(
            self.config["startup_process"]
        )
        
        return {
            "session_type": session_type,
            "context_content": content,
            "startup_content": startup_content,
            "loaded_files": [context_file, self.config["startup_process"]],
            "from_cache": from_cache and startup_cached
        }
    
    def load_process_file(self, process_name: str) -> Dict:
        """Load specific process file"""
        process_file = f"processes/PROCESS_{process_name.upper()}.md"
        
        try:
            content, from_cache = self.load_context_file(process_file)
            return {
                "process_file": process_file,
                "content": content,
                "from_cache": from_cache
            }
        except FileNotFoundError:
            raise FileNotFoundError(f"Process file not found: {process_file}")
    
    def get_cached_files(self) -> List[str]:
        """Get list of currently cached files"""
        return list(self.cache["cached_files"].keys())
    
    def clear_cache(self):
        """Clear all cached content"""
        self.cache = {"cached_files": {}, "cache_updated": None}
        self._save_cache()
