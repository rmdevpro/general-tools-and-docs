# PROCESS Git Operations - Version Control Procedures
*Detailed Git Command Sequences*
*Updated: September 7, 2025*

## 🔗 **GIT COMMAND REFERENCE**
**Full command reference:** See `G:\projects\Windows-MCP-Git-Solution.md`

## 📝 **COMMIT MESSAGE PATTERNS**

### **Planning Sessions:**
```
"Planning: [brief description]"
"Planning: Component 99 architecture design"
"Planning: HAWKMOTH distributed architecture"
```

### **Coding Sessions:**
```
"Coding: [feature] - [description]"
"Coding: JWT auth - Component 99 security foundation"
"Coding: FastAPI endpoints - Phase 2 implementation"
```

### **Testing Sessions:**
```
"Testing: [version] deployment - [status]"
"Testing: v0.0.4a deployment - successful"
"Testing: Component 99 - HuggingFace validation complete"
```

## 🏷️ **TAGGING PROCEDURES**

### **Version Milestones:**
- **Development versions:** `v0.0.4b-dev`, `v0.0.5-dev`
- **Release candidates:** `v0.0.5-rc1`, `v0.1.0-rc1`
- **Production releases:** `v0.0.5`, `v0.1.0`, `v1.0.0`

### **Tag Commands:**
```bash
git tag -a v0.0.5 -m "Component 99 Phase 2 Complete"
git push origin v0.0.5
```

## 🔄 **STANDARD WORKFLOW**
1. **Commit changes:** `git add . && git commit -m "[message]"`
2. **Tag if milestone:** `git tag -a [version] -m "[description]"`
3. **Push all:** `git push && git push --tags`

---
*Git Operations Process - Referenced by all transition processes*