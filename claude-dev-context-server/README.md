# Claude Development Framework MCP Server

A Model Context Protocol (MCP) server that provides automated session management, context loading, and compliance enforcement for Claude development workflows.

## 🚀 Features

- **Automatic Session Detection**: Detects session type from chat titles (Planning, Coding, Testing, Maintenance)
- **Context Management**: Loads appropriate framework files and rules automatically
- **Compliance Enforcement**: Validates actions against framework requirements
- **Capacity Monitoring**: Tracks chat usage and provides transition alerts
- **Session State Persistence**: Maintains progress and decisions across interactions
- **Transition Management**: Provides structured handoff procedures between sessions

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Claude Desktop application

### Setup Steps

1. **Install Dependencies**
   ```bash
   cd claude-dev-context-server
   pip install -r requirements.txt
   ```

2. **Configure Claude Desktop**
   
   Add the following to your Claude Desktop MCP settings (`claude_desktop_config.json`):
   ```json
   {
     "mcpServers": {
       "claude-dev-framework": {
         "command": "python",
         "args": ["G:/projects/General Tools and Docs/claude-dev-context-server/server.py"]
       }
     }
   }
   ```

3. **Test Installation**
   ```bash
   python server.py
   ```

## 🔧 MCP Tools

The server provides 8 core MCP tools:

### 1. `session_startup(chat_title)`
Auto-detects session type and loads appropriate context files.

**Example:**
```
session_startup("CODING Session - Feature Implementation")
```

### 2. `get_session_context()`
Returns current session context, rules, and progress.

### 3. `get_active_processes(process_type)`
Loads specific process workflow files.

**Example:**
```
get_active_processes("git")
get_active_processes("transition")
```

### 4. `enforce_compliance(action, context)`
Validates planned actions against framework rules.

**Example:**
```
enforce_compliance("create new file", {"file": "working/new_feature.py"})
```

### 5. `monitor_capacity(current_usage)`
Tracks chat capacity and provides transition alerts.

**Example:**
```
monitor_capacity(75)  # 75% capacity
```

### 6. `update_session_state(updates)`
Persists session progress and decisions.

**Example:**
```
update_session_state({
  "completed_steps": ["implementation"],
  "current_step": "testing",
  "decision": "Use existing API pattern"
})
```

### 7. `get_transition_options(current_session)`
Provides structured handoff procedures for session transitions.

**Example:**
```
get_transition_options("CODING")
```

### 8. `validate_file_operation(operation, file_path)`
Ensures file operations follow framework rules.

**Example:**
```
validate_file_operation("write", "working/new_file.py")
```

## 📁 Directory Structure

```
claude-dev-context-server/
├── server.py                 # Main MCP server
├── session_manager.py        # Session detection & management
├── context_loader.py         # File loading & caching
├── rule_enforcer.py          # Compliance validation
├── capacity_monitor.py       # Chat usage tracking
├── data/
│   ├── session_state.json    # Current session state
│   ├── context_cache.json    # Cached file contents
│   └── config.json           # Server configuration
├── requirements.txt          # Dependencies
└── README.md                # This file
```

## 🎯 Usage Examples

### Starting a New Session
```python
# Claude will automatically call this when detecting session keywords in chat title
result = session_startup("CODING Session - API Integration")
# Returns loaded context, rules, and next steps
```

### Checking Compliance
```python
# Before making file changes
compliance = enforce_compliance(
    "create new Python module",
    {"file": "working/api_client.py", "session_type": "CODING"}
)
# Returns validation results and required permissions
```

### Monitoring Capacity
```python
# Track conversation length
capacity = monitor_capacity(82)  # 82% capacity used
# Returns alerts and transition recommendations
```

### Session Transitions
```python
# When approaching capacity limits
options = get_transition_options("CODING")
# Returns handoff blocks for next session types
```

## ⚙️ Configuration

### Session Detection Keywords
- **PLANNING**: Planning, Architecture, Design
- **CODING**: Coding, Implementation, Development
- **TESTING**: Testing, Deployment, Validation  
- **MAINTENANCE**: Maintenance, Review, Audit, Health

### Capacity Thresholds
- **Warning**: 60% - Start monitoring
- **Critical**: 80% - Plan transition
- **Immediate**: 90% - Transition required

### Context Files
The server automatically loads context files from:
- `context/SESSION_*_CONTEXT.md` - Session-specific context
- `processes/PROCESS_*.md` - Workflow procedures

## 🔍 Troubleshooting

### Server Won't Start
1. Check Python version: `python --version` (requires 3.8+)
2. Verify dependencies: `pip install -r requirements.txt`
3. Check file paths in config.json

### Tools Not Available in Claude
1. Restart Claude Desktop after configuration changes
2. Verify MCP server configuration in Claude Desktop settings
3. Check server logs for errors

### Context Files Not Loading
1. Verify context directory path in `data/config.json`
2. Check file permissions
3. Use `server_health()` tool to test components

## 📊 Health Monitoring

Use the `server_health()` tool to check server status:
```python
health = server_health()
# Returns component status and active session info
```

## 🔄 Development Workflow Integration

The MCP server integrates with the Claude Development Framework workflow:

1. **Session Startup**: Auto-loads context based on chat title keywords
2. **Rule Enforcement**: Validates all actions against framework requirements  
3. **Progress Tracking**: Maintains session state and decisions
4. **Capacity Management**: Proactively manages chat transitions
5. **Handoff Procedures**: Provides structured session transitions

## 📝 License

This MCP server is part of the Claude Development Framework project.

## 🤝 Contributing

For framework updates and modifications, follow the standard Claude Development Framework procedures for planning, coding, testing, and maintenance sessions.

---

**MCP Server Version**: 1.0.0  
**Framework Compatibility**: Claude Development Framework v1.0  
**Last Updated**: September 8, 2025
