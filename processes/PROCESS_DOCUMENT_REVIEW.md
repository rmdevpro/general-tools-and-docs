# PROCESS Document Review - Documentation Audit & Cleanup
*Step-by-Step Document Maintenance Procedures*
*Updated: September 7, 2025*

## 📋 **DOCUMENT REVIEW WORKFLOW**

### **STEP 1: Review Scope Selection**
1. **REQUIRED: MUST ask user for review target:**
   "What documents do you want to review?"

2. **REQUIRED: MUST execute targeted discovery based on user selection:**
   - **REQUIRED: MUST scan selected directories/files only**
   - **REQUIRED: MUST create focused document inventory:**
     - File type classification (.md, .txt, .json, etc.)
     - Last modified dates
     - File sizes and complexity
     - Purpose classification (user-facing, technical, process)
   - **REQUIRED: MUST identify document relationships within scope:**
     - Cross-references between selected documents
     - Dependencies on documents outside scope (note for user)
     - Circular or conflicting references

3. **Options menu (if user requests guidance):**
   ```
   📋 **REVIEW OPTIONS:**
   1. **Full Project Review** - Complete documentation audit across all areas
   2. **Session Framework docs** - Just the session context and process files  
   3. **Project Documentation** - Main project docs and READMEs
   4. **Recent Changes** - Documents modified in the last week/month
   5. **Specific Files** - Tell me exactly which documents you want reviewed
   6. **Problem Area** - Focus on docs you know need attention
   ```

### **STEP 2: Content Quality Assessment**
1. **REQUIRED: MUST perform usability evaluation:**
   - Clear purpose and audience
   - Logical structure and navigation
   - Actionable content vs theory
   - Examples and practical guidance
2. **REQUIRED: MUST perform accuracy check:**
   - Current vs outdated information
   - Broken or invalid references
   - Consistency with actual implementation
   - Version alignment with code/systems
3. **REQUIRED: MUST perform complexity analysis:**
   - Information density (too verbose/too brief)
   - Technical jargon appropriate to audience
   - Clear headings and sections
   - Scannable format with bullet points/lists

### **STEP 3: Document Classification**
**Categories for each document:**
- **🟢 EXCELLENT** - Well-structured, current, useful
- **🟡 GOOD** - Minor issues, needs small updates
- **🟠 FAIR** - Significant issues, needs major revision
- **🔴 POOR** - Outdated, confusing, or incorrect
- **⚫ OBSOLETE** - No longer relevant, candidate for removal

### **STEP 4: Cleanup Actions**
1. **REQUIRED: MUST handle excellent/Good documents:**
   - Minor formatting improvements
   - Add missing cross-references
   - Update timestamps
2. **REQUIRED: MUST handle fair documents:**
   - Major restructuring for clarity
   - Content updates and corrections
   - Simplification of complex sections
3. **REQUIRED: MUST handle poor documents:**
   - Complete rewrite or merge with other docs
   - Break up overly complex documents
   - Add missing practical examples
4. **REQUIRED: MUST handle obsolete documents:**
   - Archive with .archived extension
   - Update references to point to current alternatives
   - Document removal rationale

### **STEP 5: Documentation Standards Enforcement**
1. **REQUIRED: MUST enforce formatting consistency:**
   - Markdown syntax standardization
   - Heading hierarchy compliance
   - Code block formatting
   - Link format standardization
2. **REQUIRED: MUST enforce naming conventions:**
   - File naming patterns
   - Consistent terminology usage
   - Version notation standards
3. **REQUIRED: MUST enforce content standards:**
   - Required sections (purpose, audience, examples)
   - Cross-reference requirements
   - Update date maintenance

## 🔍 **REVIEW CHECKLIST**

### **For Each Document:**
- [ ] Clear purpose stated
- [ ] Target audience identified
- [ ] Current and accurate content
- [ ] Logical structure and flow
- [ ] Actionable information provided
- [ ] Appropriate complexity level
- [ ] Valid cross-references
- [ ] Consistent formatting
- [ ] Recent update timestamp

### **For Document Set:**
- [ ] No duplicate content
- [ ] No orphaned documents
- [ ] Clear navigation between related docs
- [ ] Consistent terminology
- [ ] Complete coverage of topics
- [ ] Appropriate document hierarchy

## 📊 **REVIEW REPORTING**

### **Document Review Summary:**
```
📋 **DOCUMENT REVIEW COMPLETE**
📁 **Scope:** [directory/project area]
📊 **Inventory:** [total files] documents reviewed
📈 **Quality Distribution:**
   🟢 Excellent: [count] ([%])
   🟡 Good: [count] ([%])
   🟠 Fair: [count] ([%])
   🔴 Poor: [count] ([%])
   ⚫ Obsolete: [count] ([%])

🔧 **Actions Taken:**
   - [count] documents updated
   - [count] documents merged
   - [count] documents archived
   - [count] new documents created

⚠️ **Issues Found:**
   - [list critical issues]
   - [recommended follow-up actions]
```

---
*Document Review Process - Called by SESSION_MAINTENANCE_CONTEXT.md*