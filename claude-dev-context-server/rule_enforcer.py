#!/usr/bin/env python3
"""
Rule Enforcer Module
Validates actions against framework compliance rules
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class RuleEnforcer:
    """Validates actions against loaded compliance rules"""
    
    def __init__(self, config_path: str):
        """Initialize with configuration"""
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self.active_rules = []
        
        # Rule patterns for different validation types
        self.permission_patterns = [
            r"MUST.*ask.*permission",
            r"REQUIRED.*permission",
            r"always ask.*before"
        ]
        
        self.file_patterns = [
            r"MUST.*work.*in.*working",
            r"working.*directory",
            r"REQUIRED.*working"
        ]
        
        self.git_patterns = [
            r"MUST.*git.*operations",
            r"commit.*required",
            r"git.*push"
        ]
    
    def _load_config(self) -> Dict:
        """Load server configuration"""
        try:
            with open(self.config_path / "data" / "config.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("Configuration file not found")
    
    def load_rules(self, rules: List[str]):
        """Load active rules for validation"""
        self.active_rules = rules
    
    def check_permission_required(self, action: str) -> bool:
        """Check if action requires user permission"""
        action_lower = action.lower()
        
        # Actions that always require permission
        permission_actions = [
            "create", "write", "modify", "delete", "update",
            "commit", "push", "deploy", "install", "uninstall"
        ]
        
        for perm_action in permission_actions:
            if perm_action in action_lower:
                return True
        
        # Check against loaded rules
        for rule in self.active_rules:
            for pattern in self.permission_patterns:
                if re.search(pattern, rule, re.IGNORECASE):
                    return True
        
        return False
    
    def validate_file_operation(self, operation: str, file_path: str) -> Dict:
        """Validate file operations against rules"""
        path = Path(file_path)
        
        # Check if working directory rule is active
        working_required = any(
            re.search(pattern, rule, re.IGNORECASE) 
            for rule in self.active_rules 
            for pattern in self.file_patterns
        )
        
        # Validate against working directory requirement
        if working_required and operation in ["create", "write", "modify"]:
            if "working" not in str(path).lower():
                return {
                    "allowed": False,
                    "requires_permission": True,
                    "file_category": "non_working_directory",
                    "rules_applied": ["REQUIRED: MUST work in working/ directory"],
                    "violation": "File operation outside working directory"
                }
        
        # Determine file category
        file_category = self._categorize_file(path)
        
        # Check if operation is allowed for file category
        allowed = self._is_operation_allowed(operation, file_category)
        
        return {
            "allowed": allowed,
            "requires_permission": self.check_permission_required(operation),
            "file_category": file_category,
            "rules_applied": self._get_applicable_rules(operation, file_path)
        }
    
    def _categorize_file(self, path: Path) -> str:
        """Categorize file based on path and name"""
        path_str = str(path).lower()
        
        if "working" in path_str:
            return "working_directory"
        elif path.name.startswith("PROCESS_"):
            return "process_file"
        elif path.name.startswith("SESSION_"):
            return "context_file"
        elif path.suffix in [".md", ".txt"]:
            return "documentation"
        elif path.suffix in [".py", ".js", ".json"]:
            return "code_file"
        else:
            return "unknown"
    
    def _is_operation_allowed(self, operation: str, file_category: str) -> bool:
        """Check if operation is allowed for file category"""
        # Rules based on file categories
        restrictions = {
            "process_file": ["read"],  # Process files are read-only
            "context_file": ["read"],  # Context files are read-only
            "documentation": ["read", "write"],  # Docs can be modified
            "code_file": ["read", "write", "create"],  # Code files fully editable
            "working_directory": ["read", "write", "create", "delete"],  # Working dir fully editable
            "unknown": ["read"]  # Unknown files read-only by default
        }
        
        allowed_ops = restrictions.get(file_category, ["read"])
        return operation in allowed_ops
    
    def _get_applicable_rules(self, operation: str, file_path: str) -> List[str]:
        """Get rules that apply to this operation/file combination"""
        applicable = []
        
        # Check permission rules
        if self.check_permission_required(operation):
            permission_rules = [
                rule for rule in self.active_rules
                if any(re.search(pattern, rule, re.IGNORECASE) for pattern in self.permission_patterns)
            ]
            applicable.extend(permission_rules)
        
        # Check file-specific rules
        if "working" not in file_path.lower():
            working_rules = [
                rule for rule in self.active_rules
                if any(re.search(pattern, rule, re.IGNORECASE) for pattern in self.file_patterns)
            ]
            applicable.extend(working_rules)
        
        return applicable[:3]  # Return top 3 most relevant rules
    
    def enforce_compliance(self, action: str, context: Dict) -> Dict:
        """Main compliance validation method"""
        action_lower = action.lower()
        
        # Initialize validation result
        result = {
            "compliant": True,
            "warnings": [],
            "required_steps": [],
            "blocked_actions": []
        }
        
        # Check permission requirement
        permission_required = self.check_permission_required(action)
        user_permission_given = context.get("user_permission", False)
        
        if permission_required and not user_permission_given:
            result["compliant"] = False
            result["required_steps"].append("Ask user permission before proceeding")
            result["blocked_actions"].append(f"Action requires user permission: {action}")
        
        # Validate file operations
        if "file" in context or "path" in context:
            file_path = context.get("file", context.get("path", ""))
            operation = self._extract_operation_from_action(action)
            
            file_validation = self.validate_file_operation(operation, file_path)
            
            if not file_validation["allowed"]:
                result["compliant"] = False
                result["blocked_actions"].append(f"File operation not allowed: {action}")
                result["warnings"].extend(file_validation.get("rules_applied", []))
        
        # Check capacity warnings and enforce critical capacity restrictions
        if "capacity" in context:
            capacity = context["capacity"]
            if isinstance(capacity, str) and "%" in capacity:
                capacity_num = int(capacity.replace("%", ""))
                thresholds = self.config["capacity_thresholds"]
                
                if capacity_num >= thresholds["immediate"]:
                    result["warnings"].append("⚠️ CRITICAL: Chat capacity at 90%+ - MUST transition immediately")
                    result["required_steps"].append("Begin immediate handoff procedures")
                    
                    # At critical capacity, block non-essential actions
                    if not self._is_transition_action(action):
                        result["compliant"] = False
                        result["blocked_actions"].append(f"Action blocked due to critical capacity: {action}")
                        
                elif capacity_num >= thresholds["critical"]:
                    result["warnings"].append("⚠️ WARNING: Chat capacity at 80%+ - Plan transition soon")
                    result["required_steps"].append("Prepare for session transition")
        
        # Session-specific validations with enforcement
        session_type = context.get("session_type")
        if session_type:
            session_warnings = self._validate_session_rules(action, session_type)
            result["warnings"].extend(session_warnings)
            
            # Enforce session rule violations for major mismatches
            if self._is_major_session_violation(action, session_type):
                result["compliant"] = False
                result["blocked_actions"].append(f"Action violates {session_type} session rules: {action}")
        
        return result
    
    def _extract_operation_from_action(self, action: str) -> str:
        """Extract operation type from action description"""
        action_lower = action.lower()
        
        if any(word in action_lower for word in ["create", "add", "new"]):
            return "create"
        elif any(word in action_lower for word in ["write", "save", "update", "modify", "edit"]):
            return "write"
        elif any(word in action_lower for word in ["delete", "remove", "unlink"]):
            return "delete"
        elif any(word in action_lower for word in ["read", "load", "open", "view"]):
            return "read"
        else:
            return "unknown"
    
    def _validate_session_rules(self, action: str, session_type: str) -> List[str]:
        """Validate action against session-specific rules"""
        warnings = []
        
        # Session-specific restrictions
        if session_type == "PLANNING":
            if "implement" in action.lower() or "code" in action.lower():
                warnings.append("Planning sessions should focus on design, not implementation")
        
        elif session_type == "TESTING":
            if "new feature" in action.lower():
                warnings.append("Testing sessions should focus on validation, not new development")
        
        elif session_type == "MAINTENANCE":
            if "major change" in action.lower():
                warnings.append("Maintenance sessions should focus on small fixes and updates")
        
        return warnings
    
    def _is_transition_action(self, action: str) -> bool:
        """Check if action is related to session transition (allowed at critical capacity)"""
        action_lower = action.lower()
        
        transition_keywords = [
            "transition", "handoff", "summary", "status", "complete", 
            "finish", "wrap up", "next session", "prepare for", "save progress"
        ]
        
        return any(keyword in action_lower for keyword in transition_keywords)
    
    def _is_major_session_violation(self, action: str, session_type: str) -> bool:
        """Check if action is a major violation of session rules"""
        action_lower = action.lower()
        
        # Major violations by session type
        violations = {
            "PLANNING": ["deploy", "production", "release", "publish"],
            "TESTING": ["deploy", "production", "release", "new project", "major refactor"],
            "MAINTENANCE": ["deploy", "production", "major rewrite", "new feature", "breaking change"],
            "CODING": ["deploy", "production"]  # Coding sessions shouldn't deploy directly
        }
        
        session_violations = violations.get(session_type, [])
        return any(violation in action_lower for violation in session_violations)
