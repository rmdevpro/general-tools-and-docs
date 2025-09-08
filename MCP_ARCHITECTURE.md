# MCP Server Architecture & Tool Specifications
*Claude Development Framework MCP Server Design*
*Created: September 8, 2025*

## 🏗️ **ARCHITECTURE OVERVIEW**

### **Server Components**
```
claude-dev-context-server/
├── server.py                 # Main MCP server (FastMCP)
├── session_manager.py        # Session detection & management
├── context_loader.py         # File loading & caching
├── rule_enforcer.py          # Compliance validation
├── capacity_monitor.py       # Chat usage tracking
├── data/
│   ├── session_state.json    # Current session state
│   ├── context_cache.json    # Cached file contents
│   └── config.json           # Server configuration
├── requirements.txt          # Dependencies: fastmcp, watchdog
└── README.md                # Setup instructions
```

## 🔧 **MCP TOOLS SPECIFICATION**

### **1. session_startup(chat_title: str)**
**Purpose:** Auto-detect session type and load appropriate context
**Input:** Chat title or session type
**Process:**
- Parse title for keywords (Planning/Coding/Testing/Maintenance)
- Load SESSION_*_CONTEXT.md file
- Load PROCESS_STARTUP_SEQUENCE.md
- Initialize session state
- Return loaded context and next steps

**Output:**
```json
{
  "session_type": "CODING",
  "loaded_contexts": ["SESSION_CODING_CONTEXT.md", "PROCESS_STARTUP_SEQUENCE.md"],
  "mandatory_rules": ["Always ask permission", "Monitor capacity"],
  "next_steps": ["Load working directory", "Check capacity"]
}
```

### **2. get_session_context()**
**Purpose:** Return current session context and rules
**Process:**
- Return cached context files
- List active compliance rules
- Show current session progress

**Output:**
```json
{
  "session_type": "CODING",
  "context_content": "# Session Coding Context...",
  "active_rules": ["REQUIRED: MUST ask permission...", "REQUIRED: MUST work in working/..."],
  "session_progress": "startup_complete"
}
```

### **3. get_active_processes(process_type: str)**
**Purpose:** Load specific process workflow files
**Input:** Process type (startup, transition, git, deployment, etc.)
**Process:**
- Load requested PROCESS_*.md file
- Cache content for session
- Return structured process steps

**Output:**
```json
{
  "process_file": "PROCESS_TRANSITION_CODING.md",
  "process_steps": ["Files to Update", "Git Operations", "Handoff Process"],
  "mandatory_actions": ["REQUIRED: MUST update SESSION_SUMMARY_CODING.md"],
  "conditional_actions": ["Git operations if changes made"]
}
```

### **4. enforce_compliance(action: str, context: dict)**
**Purpose:** Validate planned actions against framework rules
**Input:** Proposed action and current context
**Process:**
- Check action against loaded rules
- Validate against session type requirements
- Return compliance status and warnings

**Output:**
```json
{
  "compliant": true,
  "warnings": [],
  "required_steps": ["Ask user permission before proceeding"],
  "blocked_actions": []
}
```

### **5. monitor_capacity(current_usage: int)**
**Purpose:** Track chat capacity and provide alerts
**Input:** Current conversation length or percentage
**Process:**
- Compare against thresholds (60%, 80%, 90%)
- Generate appropriate warnings
- Suggest transition actions if needed

**Output:**
```json
{
  "capacity_status": "80%",
  "alert_level": "WARNING",
  "message": "⚠️ CAPACITY WARNING: Plan transition soon",
  "recommended_action": "Begin handoff procedures"
}
```

### **6. update_session_state(updates: dict)**
**Purpose:** Persist session progress and decisions
**Input:** State updates (completed steps, current focus, etc.)
**Process:**
- Update session_state.json
- Log important decisions
- Track workflow progress

**Output:**
```json
{
  "updated": true,
  "current_state": {
    "session_type": "CODING",
    "completed_steps": ["startup", "context_loaded"],
    "current_focus": "implementation_work",
    "last_updated": "2025-09-08T10:30:00Z"
  }
}
```

### **7. get_transition_options(current_session: str)**
**Purpose:** Provide structured handoff procedures
**Input:** Current session type
**Process:**
- Load PROCESS_TRANSITION_*.md file
- Generate handoff blocks for each session type
- Format as copyable code blocks

**Output:**
```json
{
  "current_session": "CODING",
  "transition_file": "PROCESS_TRANSITION_CODING.md",
  "available_transitions": ["PLANNING", "CODING", "TESTING", "MAINTENANCE"],
  "handoff_blocks": {
    "PLANNING": "🆕 **New Chat Session Startup - New Chat Session for PLANNING...",
    "TESTING": "🆕 **New Chat Session Startup - New Chat Session for TESTING..."
  }
}
```

### **8. validate_file_operation(operation: str, file_path: str)**
**Purpose:** Ensure file operations follow framework rules
**Input:** Operation type and target file
**Process:**
- Check against session-specific file rules
- Validate permissions and patterns
- Ensure working/ vs production file rules

**Output:**
```json
{
  "allowed": true,
  "requires_permission": true,
  "file_category": "working_directory",
  "rules_applied": ["REQUIRED: MUST work in working/ directory"]
}
```

## 🗄️ **DATA PERSISTENCE**

### **session_state.json**
```json
{
  "current_session": {
    "type": "CODING",
    "start_time": "2025-09-08T10:00:00Z",
    "chat_title": "CODING Session - Feature Implementation",
    "capacity_used": "45%",
    "status": "active"
  },
  "loaded_contexts": [
    {
      "file": "SESSION_CODING_CONTEXT.md",
      "loaded_at": "2025-09-08T10:00:15Z",
      "content_hash": "abc123"
    }
  ],
  "active_rules": [
    "REQUIRED: MUST always ask permission before any file changes",
    "REQUIRED: MUST work in working/ directory for iterations"
  ],
  "session_progress": {
    "completed_steps": ["startup", "context_loaded"],
    "current_step": "implementation_work",
    "next_actions": ["test_changes", "update_docs"]
  },
  "decisions_log": [
    {
      "timestamp": "2025-09-08T10:15:00Z",
      "decision": "Use existing patterns for new feature",
      "rationale": "Maintains consistency with framework"
    }
  ]
}
```

### **context_cache.json**
```json
{
  "cached_files": {
    "SESSION_CODING_CONTEXT.md": {
      "content": "# Session Coding Context...",
      "last_modified": "2025-09-07T00:00:00Z",
      "file_hash": "def456"
    },
    "PROCESS_STARTUP_SEQUENCE.md": {
      "content": "# PROCESS Startup Sequence...",
      "last_modified": "2025-09-07T00:00:00Z", 
      "file_hash": "ghi789"
    }
  },
  "cache_updated": "2025-09-08T10:00:00Z"
}
```

## 🔄 **WORKFLOW INTEGRATION**

### **Session Startup Flow**
1. **session_startup()** called with chat title
2. Session type detected from keywords
3. Appropriate context files loaded automatically
4. Rules extracted and activated
5. Session state initialized
6. User presented with loaded context and next steps

### **During Session Flow**
1. **get_session_context()** provides current rules/context
2. **enforce_compliance()** validates all proposed actions
3. **monitor_capacity()** tracks chat usage proactively
4. **update_session_state()** logs progress and decisions

### **Session Transition Flow**
1. **get_transition_options()** provides handoff procedures
2. **update_session_state()** logs session completion
3. Handoff blocks generated for next session
4. State persisted for continuity

## 🛠️ **IMPLEMENTATION DETAILS**

### **Dependencies**
- **fastmcp**: MCP server framework
- **watchdog**: File system monitoring
- **json**: Data persistence
- **pathlib**: File operations
- **datetime**: Timestamp management

### **Configuration**
```json
{
  "context_directory": "G:/projects/General Tools and Docs",
  "session_detection": {
    "PLANNING": ["Planning", "Architecture", "Design"],
    "CODING": ["Coding", "Implementation", "Development"], 
    "TESTING": ["Testing", "Deployment", "Validation"],
    "MAINTENANCE": ["Maintenance", "Review", "Audit", "Health"]
  },
  "capacity_thresholds": {
    "warning": 60,
    "critical": 80,
    "immediate": 90
  }
}
```

### **Error Handling**
- File not found: Return cached version with warning
- Invalid session type: Default to MAINTENANCE mode
- Capacity overflow: Force transition procedures
- Rule violation: Block action with explanation

---

**Architecture Status:** Design Complete ✅  
**Next Phase:** Core MCP Server Development  
**Integration Point:** Claude Desktop MCP configuration  
**Framework Compatibility:** 100% with existing structure
