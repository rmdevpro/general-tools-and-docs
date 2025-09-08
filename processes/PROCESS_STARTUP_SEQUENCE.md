# PROCESS Startup Sequence - Detailed Session Initialization
*Step-by-Step Startup Procedures*
*Updated: September 7, 2025*

## 🔥 **MANDATORY COMPLIANCE FIRST** (Before Any Reading)
- **REQUIRED:** MUST follow all context files exactly without deviation
- **REQUIRED:** MUST implement context-specific requirements immediately upon reading them
- **REQUIRED:** MUST NOT proceed with general startup pattern if context files contain overriding instructions
- **REQUIRED:** MUST pause and implement behavioral requirements before continuing with procedural steps

## 📋 **PLANNING SESSION STARTUP**
1. ✅ **PLANNING** session automatically detected from chat title
2. ✅ **MUST read** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_PLANNING.md (planning-specific context)
3. ✅ **MUST load** architecture docs from docs/architecture/ and docs/components/
4. ✅ **REQUIRED:** Check chat capacity after startup completion

## ⚡ **CODING SESSION STARTUP**
1. ✅ **CODING** session automatically detected from chat title
2. ✅ **MUST read** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_CODING.md (coding-specific context)
3. ✅ **MUST load** working/ directory files and UPLOAD_TO_HF/ production files
4. ✅ **REQUIRED:** Check chat capacity after startup completion

## 🧪 **TESTING SESSION STARTUP**
1. ✅ **TESTING** session automatically detected from chat title
2. ✅ **MUST read** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_TESTING.md (testing-specific context)
3. ✅ **MUST load** UPLOAD_TO_HF/ deployment files and working/test_results.md
4. ✅ **REQUIRED:** Check chat capacity after startup completion

## 🔧 **MAINTENANCE SESSION STARTUP**
1. ✅ **MAINTENANCE** session automatically detected from chat title
2. ✅ **MUST read** G:/projects/General Tools and Docs/processes/SESSION_SUMMARY_MAINTENANCE.md (maintenance-specific context)
3. ✅ **MUST load** working/ directory, UPLOAD_TO_HF/ files, and docs/ structure for comprehensive review
4. ✅ **REQUIRED:** Check chat capacity after startup completion

## 📊 **CHAT CAPACITY MONITORING**
### **Capacity Thresholds:**
- **60%**: "Approaching mid-session capacity"
- **80%**: "⚠️ CAPACITY WARNING: Plan transition soon"
- **90%**: "🚨 IMMEDIATE ACTION: Must create handoff now"

### **Monitoring Protocol:**
- **MUST:** Check capacity after major operations
- **MUST:** Monitor proactively throughout session
- **MUST:** Alert user before reaching critical thresholds

---
*Startup Sequence Process - Called by SESSION_STARTUP.md*