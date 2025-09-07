# PROCESS Transition Coding - Coding Session Handoff Procedures
*Ultra-Concise Bullet Point Steps*

## ⚡ **CODING TRANSITION STEPS**

### **Files to Update:**
- **G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_CODING.md** - **REQUIRED: MUST update** coding-specific progress and technical status
- **version.json** - **REQUIRED: MUST increment** for milestone completion
- **working/[COMPONENT]_SUMMARY.md** - **REQUIRED: MUST create** for major changes
- **UPLOAD_TO_HF/** - **REQUIRED: MUST update** production files when components are tested

### **Git Operations (Conditional):**
- **REQUIRED: MUST assess changes:** Check if git-relevant changes were made during session
- **Git-relevant changes include:**
  - Code changes in working/, UPLOAD_TO_HF/, or production files
  - Version increments in version.json
  - Component implementation or major feature additions
  - Production-ready code or deployment packages
- **If meaningful changes made:**
  - **REQUIRED: MUST see** G:/projects/General Tools and Docs/processes/PROCESS_GIT_OPERATIONS.md for detailed git commands
  - **REQUIRED: MUST use commit message:** "Coding: [feature] - [description]"
  - **REQUIRED: MUST tag release** for version milestones (v0.0.5, v0.1.0, etc.)
  - **REQUIRED: MUST push changes** to sync
- **If only summary updates:**
  - **REQUIRED: MUST skip git operations**
  - **REQUIRED: MUST inform user:** "No git commit needed - only session summary updated"

### **Handoff Process:**
1. **MUST ask user:** "What type of session should we transition to?"
   ```
   1. **PLANNING** - Architecture & Design Focus
   2. **CODING** - Implementation & Development Focus  
   3. **TESTING** - Deployment & Validation Focus
   4. **MAINTENANCE** - System & Documentation Maintenance Focus
   ```
2. **MUST generate specific handoff header based on user's choice:**

**For PLANNING (Option 1):**
```
🦅 **HAWKMOTH PLANNING Session - [Date]**
🎯 **Architecture & Design Focus - Component Planning**
⚠️ **READ G:/projects/General Tools and Docs/context/SESSION_STARTUP.md**

🎉 **CODING ACCOMPLISHED:**
[List implementation work completed]
```

**For CODING (Option 2):**
```
🦅 **HAWKMOTH CODING Session - [Date]**
🎯 **Implementation & Development Focus - Code Changes**
⚠️ **READ G:/projects/General Tools and Docs/context/SESSION_STARTUP.md**

🎉 **CODING ACCOMPLISHED:**
[List implementation work completed]
```

**For TESTING (Option 3):**
```
🦅 **HAWKMOTH TESTING Session - [Date]**
🎯 **Deployment & Validation Focus - Production Testing**
⚠️ **READ G:/projects/General Tools and Docs/context/SESSION_STARTUP.md**

🎉 **CODING ACCOMPLISHED:**
[List implementation work completed]
```

**For MAINTENANCE (Option 4):**
```
🦅 **HAWKMOTH MAINTENANCE Session - [Date]**
🎯 **System Maintenance & Optimization Focus - Technical Debt Reduction**
⚠️ **READ G:/projects/General Tools and Docs/context/SESSION_STARTUP.md**

🎉 **CODING ACCOMPLISHED:**
[List implementation work completed]
```

---
*Coding Transition Process - Called by SESSION_CODING_CONTEXT.md*