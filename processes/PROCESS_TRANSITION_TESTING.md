# PROCESS Transition Testing - Testing Session Handoff Procedures
*Ultra-Concise Bullet Point Steps*

## 🧪 **TESTING TRANSITION STEPS**

### **Files to Update:**
- **G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_TESTING.md** - **REQUIRED: MUST update** testing-specific progress and deployment status
- **version.json** - **REQUIRED: MUST confirm** version reflects deployment
- **working/test_results.md** - **REQUIRED: MUST document** issues found during testing

### **Deployment Process:**
- **For deployments:** **REQUIRED: MUST read** `G:/projects/General Tools and Docs/processes/PROCESS_DEPLOYMENT.md` for complete deployment workflow
- **Always check:** **REQUIRED: MUST check** DEPLOYMENT_STEPS.md in deployment folder for special instructions

### **Git Operations (Conditional):**
- **REQUIRED: MUST assess changes:** Check if git-relevant changes were made during session
- **Git-relevant changes include:**
  - Successful production deployments
  - Version confirmations in version.json
  - Test results affecting code or deployment files
  - Deployment status changes or validation outcomes
- **If meaningful changes made:**
  - **REQUIRED: MUST see** G:/projects/General Tools and Docs/processes/PROCESS_GIT_OPERATIONS.md for detailed git commands
  - **REQUIRED: MUST use commit message:** "Testing: [version] deployment - [status]"
  - **REQUIRED: MUST tag release** for successful deployments (v0.0.4a, v0.0.5, etc.)
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

🎉 **TESTING ACCOMPLISHED:**
[List deployment results and validation status]
```

**For CODING (Option 2):**
```
🦅 **HAWKMOTH CODING Session - [Date]**
🎯 **Implementation & Development Focus - Code Changes**
⚠️ **READ G:/projects/General Tools and Docs/context/SESSION_STARTUP.md**

🎉 **TESTING ACCOMPLISHED:**
[List deployment results and validation status]
```

**For TESTING (Option 3):**
```
🦅 **HAWKMOTH TESTING Session - [Date]**
🎯 **Deployment & Validation Focus - Production Testing**
⚠️ **READ G:/projects/General Tools and Docs/context/SESSION_STARTUP.md**

🎉 **TESTING ACCOMPLISHED:**
[List deployment results and validation status]
```

**For MAINTENANCE (Option 4):**
```
🦅 **HAWKMOTH MAINTENANCE Session - [Date]**
🎯 **System Maintenance & Optimization Focus - Technical Debt Reduction**
⚠️ **READ G:/projects/General Tools and Docs/context/SESSION_STARTUP.md**

🎉 **TESTING ACCOMPLISHED:**
[List deployment results and validation status]
```

---
*Testing Transition Process - Called by SESSION_TESTING_CONTEXT.md*