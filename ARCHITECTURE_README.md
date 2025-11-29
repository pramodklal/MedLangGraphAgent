# MedARPR Architecture Diagram - Implementation Guide

## 📁 Files Created

1. **architecture_diagram.drawio** - Draw.io format (recommended)
2. **architecture_diagram.vsdx.xml** - Microsoft Visio XML format
3. **ARCHITECTURE_README.md** - This guide

---

## 🎨 How to Use the Architecture Diagrams

### Option 1: Draw.io (Recommended - FREE)

**Steps:**
1. Go to https://app.diagrams.net/ (or download the desktop app)
2. Click **File → Open**
3. Select `architecture_diagram.drawio`
4. The complete architecture diagram will load
5. You can:
   - Edit any component
   - Change colors and styles
   - Export to PNG, SVG, PDF, or Visio format
   - Add more details

**Benefits:**
- ✅ Free and open-source
- ✅ Works in browser or desktop
- ✅ Can export to Visio, PNG, PDF, SVG
- ✅ Easy to customize

### Option 2: Microsoft Visio

**Steps:**
1. Open Microsoft Visio
2. Click **File → Import → XML**
3. Select `architecture_diagram.vsdx.xml`
4. The diagram will import with all shapes and connections
5. You may need to adjust positioning slightly

**Note:** The XML format is a simplified representation. You may need to:
- Adjust shape positions
- Reconnect some arrows
- Reapply some formatting

### Option 3: Lucidchart

**Steps:**
1. Go to https://www.lucidchart.com/
2. Click **Import → Visio** or **Import → Draw.io**
3. Select `architecture_diagram.drawio`
4. Edit and export as needed

### Option 4: Create from Scratch (Manual)

Use the architecture specifications below to recreate in any tool.

---

## 📐 Architecture Diagram Specifications

### **Layout Structure**

```
┌─────────────────────────────────────────────────────────────┐
│                          TITLE                              │  (Top)
├─────────────────────────────────────────────────────────────┤
│                        END USER                             │  (Actor Icon)
├─────────────────────────────────────────────────────────────┤
│                   PRESENTATION LAYER                        │  (Purple)
│  [Streamlit] [Sidebar] [Main Area] [Result Tabs]           │
├─────────────────────────────────────────────────────────────┤
│              ORCHESTRATION LAYER (Multi-Agent)              │  (Yellow)
│  [Agent1] → [Agent2] → [Agent3] → [Agent4] → [Agent5]      │
│            → [Agent6] → [Agent7]                            │
│  [State Management TypedDict]                               │
├─────────────────────────────────────────────────────────────┤
│                     AI MODEL LAYER                          │  (Gray)
│       [Gemini Vision API]    [Gemini Text API]              │
└─────────────────────────────────────────────────────────────┘
│  [Legend]  [Performance Metrics]  [Tech Stack]              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎨 Color Scheme

| Component Type | Fill Color | Border Color | Hex Codes |
|---------------|------------|--------------|-----------|
| **UI Components** | Light Blue | Blue | Fill: #DAE8FC, Border: #6C8EBF |
| **Processing Agents** | Light Green | Green | Fill: #D5E8D4, Border: #82B366 |
| **AI API Calls** | Light Orange | Orange | Fill: #FFE6CC, Border: #D79B00 |
| **State/Data** | Light Red | Red | Fill: #F8CECC, Border: #B85450 |
| **Presentation Layer** | Light Purple | Purple | Fill: #E1D5E7, Border: #9673A6 |
| **Orchestration Layer** | Light Yellow | Yellow | Fill: #FFF2CC, Border: #D6B656 |
| **AI Model Layer** | Light Gray | Gray | Fill: #F5F5F5, Border: #666666 |

---

## 📦 Component Details

### **1. Presentation Layer (Purple Container)**

**Components:**
- **Streamlit Web App (app.py)** - Main application
  - Size: 140x70px
  - Color: Light Blue
  
- **Sidebar** - Upload & controls
  - Content: Upload Image, Select Type, Analyze Button
  - Size: 130x70px
  - Color: Light Green
  
- **Main Area** - Display & progress
  - Content: Image Display, Progress Bar, Status Panel
  - Size: 130x70px
  - Color: Light Green
  
- **Result Tabs** - Output display
  - Content: Full Report, Medications, Care Plan, Doctor Summary
  - Size: 130x70px
  - Color: Light Green

### **2. Orchestration Layer (Yellow Container)**

**7 Agent Nodes (Sequential Flow):**

1. **Agent 1: Image Preprocessing**
   - Size: 90x60px
   - Color: Light Green
   - Function: Validate, Convert, Resize

2. **Agent 2: Vision Analysis** ⚠️ **API CALL #1**
   - Size: 90x60px
   - Color: Light Orange (highlights API call)
   - Function: analyze_image() method
   - Border: Bold (2pt)

3. **Agent 3: Disease Identification**
   - Size: 90x60px
   - Color: Light Green
   - Function: Extract diseases & confidence

4. **Agent 4: Root Cause Analysis**
   - Size: 90x60px
   - Color: Light Green
   - Function: Extract root causes

5. **Agent 5: Medication Orchestration**
   - Size: 90x60px
   - Color: Light Green
   - Function: Coordinate treatment planning

6. **Agent 6: Combined Treatment** ⚠️ **API CALL #2**
   - Size: 90x60px
   - Color: Light Orange (highlights API call)
   - Function: generate_text_response() method
   - Border: Bold (2pt)

7. **Agent 7: Report Compilation**
   - Size: 90x60px
   - Color: Light Green
   - Function: Format final report

**State Management:**
- Size: 190x60px
- Color: Light Red
- Content: MedicalAnalysisState (TypedDict) with all state fields

### **3. AI Model Layer (Gray Container)**

**Components:**
- **Vision API** - Multimodal Image Analysis
  - Size: 180x40px
  - Color: Light Orange
  
- **Text API** - Treatment Generation
  - Size: 180x40px
  - Color: Light Orange

### **4. Information Panels (Right Side)**

**Performance Metrics:**
- Size: 140x100px
- Color: Light Purple
- Content:
  - ⏱️ Processing: 50-60s
  - 📞 API Calls: 2
  - 🎯 Optimization: 60%

**Tech Stack:**
- Size: 140x100px
- Color: Light Yellow
- Content:
  - LangGraph 1.0.3
  - Gemini 2.5 Flash
  - Streamlit 1.40.2
  - Python 3.11

**Legend:**
- Size: 140x180px
- White background
- Shows all color codes and their meanings

---

## 🔗 Connection/Arrow Specifications

### **Arrow Types:**

1. **Solid Blue Arrows** (User Flow)
   - Width: 2pt
   - Color: #6C8EBF
   - Connections: User → Streamlit → Agents → UI

2. **Solid Green Arrows** (Agent Flow)
   - Width: 2pt
   - Color: #82B366
   - Connections: Agent1 → Agent2 → ... → Agent7

3. **Dashed Orange Arrows** (API Calls)
   - Width: 2pt
   - Color: #D79B00
   - Style: Dashed
   - Connections: Agent2 → Vision API, Agent6 → Text API

### **Connection Points:**

```
User (Bottom) → Streamlit (Top)
Streamlit (Bottom) → Agent1 (Top)
Agent1 (Right) → Agent2 (Left)
Agent2 (Right) → Agent3 (Left)
Agent3 (Right) → Agent4 (Left)
Agent4 (Right) → Agent5 (Left)
Agent5 (Right) → Agent6 (Left)
Agent6 (Bottom) → Agent7 (Top)
Agent7 (Top) → Result Tabs (Bottom)

API Connections (Dashed):
Agent2 (Bottom) → Vision API (Top)
Agent6 (Bottom) → Text API (Top)
```

---

## 📊 Diagram Dimensions

**Page Size:** 11" x 8.5" (Letter, Landscape)

**Margins:**
- Top: 0.5"
- Bottom: 0.5"
- Left: 0.5"
- Right: 0.5"

**Layer Heights:**
- Title: 40px
- User: 60px
- Presentation Layer: 140px
- Orchestration Layer: 280px
- AI Model Layer: 100px
- Info Panels: 100-180px

---

## 🛠️ Customization Tips

### **For Presentations:**
1. Increase font sizes (16-20pt for titles)
2. Use bold borders (3-4pt) for key components
3. Add drop shadows for depth
4. Export as high-res PNG (300 DPI)

### **For Documentation:**
1. Keep current font sizes (10-14pt)
2. Add detailed annotations
3. Include version numbers
4. Export as SVG for scalability

### **For Technical Reviews:**
1. Add line numbers to code references
2. Include latency measurements
3. Show data sizes/formats
4. Add technology version badges

---

## 📤 Export Options

### **From Draw.io:**
- **PNG**: High resolution for presentations (300 DPI)
- **SVG**: Scalable for web/documentation
- **PDF**: Print-ready format
- **VSDX**: Import into Visio
- **HTML**: Interactive web version

### **From Visio:**
- **VSDX**: Native Visio format
- **PDF**: Print and share
- **PNG/JPG**: Presentations
- **SVG**: Web embedding

---

## 🎯 Quick Start Recommendations

### **Best Option for Most Users:**
1. Open https://app.diagrams.net/
2. Open `architecture_diagram.drawio`
3. Customize as needed
4. Export to PNG or PDF

### **For Microsoft Visio Users:**
1. Import `architecture_diagram.vsdx.xml`
2. Adjust layout (may need minor tweaks)
3. Apply Visio themes if desired
4. Export to your preferred format

---

## 📝 Additional Diagram Ideas

You can create additional diagrams from this architecture:

1. **Sequence Diagram** - Show time-based flow of operations
2. **Data Flow Diagram** - Focus on data transformations
3. **Deployment Diagram** - Show infrastructure and hosting
4. **Component Diagram** - Detailed class/module relationships
5. **State Machine Diagram** - Agent state transitions

---

## 🔧 Troubleshooting

### **Draw.io Issues:**
- File won't open → Clear browser cache, try desktop app
- Missing shapes → Use built-in shape libraries
- Export quality low → Set DPI to 300 in export settings

### **Visio Issues:**
- XML import errors → Use "Import XML" not "Open"
- Arrows disconnected → Manually reconnect using connector tool
- Colors wrong → Reapply fill colors manually

---

## 📞 Support

If you need help creating or customizing the architecture diagram:
1. Check Draw.io documentation: https://desk.draw.io/
2. Visio help: https://support.microsoft.com/visio
3. Refer to this README for specifications

---

**Created for:** MedARPR Medical Image Analysis System  
**Version:** 1.0  
**Date:** November 28, 2025  
**Format:** Multi-tool compatible (Draw.io, Visio, Lucidchart)
