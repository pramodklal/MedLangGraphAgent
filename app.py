"""
Streamlit UI for Medical Image Analysis System
This provides a user-friendly interface for uploading medical images
and viewing comprehensive analysis results.
"""

import streamlit as st
from PIL import Image
import io
from datetime import datetime
from medagent import MedicalAnalysisAgent
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Medical Image Analysis System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        padding: 20px;
        background: linear-gradient(90deg, #e3f2fd 0%, #bbdefb 100%);
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .stAlert {
        background-color: #fff3cd;
        border: 1px solid #ffc107;
        border-radius: 5px;
        padding: 15px;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 10px 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables"""
    if 'analysis_complete' not in st.session_state:
        st.session_state.analysis_complete = False
    if 'analysis_result' not in st.session_state:
        st.session_state.analysis_result = None
    if 'agent' not in st.session_state:
        st.session_state.agent = None
    if 'last_uploaded_file' not in st.session_state:
        st.session_state.last_uploaded_file = None


@st.cache_resource
def load_agent():
    """Load and cache the medical analysis agent"""
    logger.info("Loading Medical Analysis Agent...")
    agent = MedicalAnalysisAgent()
    agent.build_graph()
    logger.info("Agent loaded successfully")
    return agent


def display_medication_card(med_data):
    """Display medication information in a formatted card"""
    st.markdown(f"""
    <div class="metric-card">
        <h4>💊 {med_data['name']}</h4>
        <p><strong>Type:</strong> {med_data['type']}</p>
        <p><strong>Dosage:</strong> {med_data['dosage']}</p>
        <p><strong>Duration:</strong> {med_data['duration']}</p>
        <p><strong>⚠️ Contraindications:</strong> {med_data['contraindications']}</p>
    </div>
    """, unsafe_allow_html=True)


def main():
    """Main application function"""
    
    # Initialize session state
    initialize_session_state()
    
    # Main header
    st.markdown('<div class="main-header">🏥 Medical Image Analysis System</div>', 
                unsafe_allow_html=True)
    
    st.markdown("""
    ### AI-Powered Diagnostic Assistant
    
    Upload medical images (X-Ray, MRI, CT Scan, ECG, Ultrasound) for comprehensive AI analysis using 
    **LangGraph** orchestration and **Google Gemini Vision** medical AI model.
    """)
    
    # Sidebar for image upload and configuration
    with st.sidebar:
        st.header("📤 Upload Medical Image")
        
        # Image type selection
        image_type = st.selectbox(
            "Select Image Type",
            ["X-Ray", "MRI", "CT Scan", "ECG", "Ultrasound"],
            help="Choose the type of medical image you're uploading"
        )
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a medical image file",
            type=["png", "jpg", "jpeg", "bmp", "tiff"],
            help="Supported formats: PNG, JPG, JPEG, BMP, TIFF"
        )
        
        # Check if a new file was uploaded (clear previous results)
        if uploaded_file is not None:
            # Generate unique identifier for uploaded file
            file_id = f"{uploaded_file.name}_{uploaded_file.size}"
            
            # If this is a different file, clear previous results
            if st.session_state.last_uploaded_file != file_id:
                st.session_state.analysis_complete = False
                st.session_state.analysis_result = None
                st.session_state.last_uploaded_file = file_id
                st.rerun()
        
        st.divider()
        
        # Analysis button
        analyze_button = st.button(
            "🔍 Analyze Image", 
            type="primary",
            use_container_width=True,
            disabled=(uploaded_file is None)
        )
        
        if uploaded_file is None:
            st.info("👆 Please upload an image to begin analysis")
        
        st.divider()
        
        # Information section
        with st.expander("ℹ️ About This System"):
            st.markdown("""
            **Technology Stack:**
            - 🤖 LangGraph for workflow orchestration
            - 🔬 Google Gemini Vision AI model
            - 📊 Multi-stage analysis pipeline
            
            **Analysis Includes:**
            1. Image preprocessing & validation
            2. Comprehensive medical analysis (quality, findings, disease identification, root cause)
            3. AI-powered medication recommendations
            4. Personalized 2-week care plan
            5. Downloadable medical report
            
            **Note:** Analysis is optimized for speed with fewer AI calls while maintaining quality.
            """)
        
        with st.expander("⚠️ Important Disclaimer"):
            st.warning("""
            This tool is for **educational and research purposes only**. 
            
            It does NOT replace professional medical advice. Always consult 
            qualified healthcare providers for diagnosis and treatment.
            """)
    
    # Main content area
    if uploaded_file is not None:
        # Create two columns for image display and info
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📸 Uploaded Image")
            
            # Load and display image
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True, caption=f"{image_type} Image")
            
            # Display image metadata
            with st.expander("📋 Image Information"):
                st.write(f"**Format:** {image.format}")
                st.write(f"**Size:** {image.size[0]} x {image.size[1]} pixels")
                st.write(f"**Mode:** {image.mode}")
                st.write(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")
        
        with col2:
            st.subheader("ℹ️ Analysis Status")
            
            if not st.session_state.analysis_complete:
                st.info("""
                **Ready for Analysis**
                
                Click the "🔍 Analyze Image" button in the sidebar to start 
                the comprehensive medical image analysis.
                
                The analysis typically takes 30-60 seconds.
                """)
            else:
                st.success("""
                **✅ Analysis Complete**
                
                Your medical image has been successfully analyzed. 
                View the results in the tabs below.
                """)
    
    # Analysis execution
    if analyze_button and uploaded_file:
        st.session_state.analysis_complete = False
        
        # Load the agent
        with st.spinner("🔄 Loading AI models..."):
            agent = load_agent()
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Load image
        image = Image.open(uploaded_file)
        
        try:
            # Stage 1: Preprocessing
            status_text.text("⚙️ Stage 1/7: Preprocessing image...")
            progress_bar.progress(14)
            
            # Stage 2: Initial Analysis
            status_text.text("🔬 Stage 2/7: Performing initial analysis...")
            progress_bar.progress(28)
            
            # Run the full analysis
            result = agent.analyze_medical_image(
                image=image,
                image_type=image_type.lower(),
                image_path=uploaded_file.name
            )
            
            # Update progress through stages
            progress_bar.progress(42)
            status_text.text("🦠 Stage 3/7: Identifying diseases...")
            
            progress_bar.progress(57)
            status_text.text("🔍 Stage 4/7: Analyzing root causes...")
            
            progress_bar.progress(71)
            status_text.text("💊 Stage 5/7: Generating medication recommendations...")
            
            progress_bar.progress(85)
            status_text.text("📅 Stage 6/7: Creating care plan...")
            
            progress_bar.progress(100)
            status_text.text("📄 Stage 7/7: Compiling final report...")
            
            # Check if analysis was successful
            if result.get("status") == "completed":
                st.session_state.analysis_result = result
                st.session_state.analysis_complete = True
                status_text.success("✅ Analysis completed successfully!")
                st.rerun()
            else:
                status_text.error(f"❌ Analysis failed: {result.get('error', 'Unknown error')}")
                
        except Exception as e:
            logger.error(f"Error during analysis: {str(e)}")
            status_text.error(f"❌ Error: {str(e)}")
            progress_bar.empty()
    
    # Display results if analysis is complete
    if st.session_state.analysis_complete and st.session_state.analysis_result:
        st.divider()
        
        result = st.session_state.analysis_result
        
        # Create tabs for different sections (optimized - merged comprehensive and full report)
        tab1, tab2, tab3, tab4 = st.tabs([
            "� Full Medical Report",
            "💊 Medications",
            "📅 Care Plan",
            "‍⚕️ Doctor Summary"
        ])
        
        # Tab 1: Full Medical Report (merged Comprehensive Analysis + Full Report)
        with tab1:
            st.subheader("📄 Comprehensive Medical Report")
            st.caption("Complete analysis including: Image Quality, Findings, Disease Identification, Root Cause, and Full Report")
            
            if "final_report" in result:
                # Display the full report (which includes comprehensive analysis)
                st.markdown(result["final_report"])
                
                # Display confidence scores if available
                if "confidence_scores" in result:
                    st.divider()
                    st.subheader("📊 Diagnostic Confidence")
                    
                    for key, value in result["confidence_scores"].items():
                        st.progress(value, text=f"{key.replace('_', ' ').title()}: {value*100:.1f}%")
                
                # Display analysis metadata
                if "analysis_id" in result:
                    st.divider()
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Analysis ID", result["analysis_id"])
                    with col2:
                        st.metric("Timestamp", result.get("timestamp", "N/A")[:19])
                
                st.divider()
                
                # Download button
                st.download_button(
                    label="📥 Download Report (Text)",
                    data=result["final_report"],
                    file_name=f"medical_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            else:
                st.warning("Report not available")
        
        # Tab 2: Medications
        with tab2:
            st.subheader("Medication Recommendations")
            
            if "recommended_medicines" in result and result["recommended_medicines"]:
                st.info("⚠️ **Important:** These are AI-generated recommendations. All medications must be prescribed by a licensed healthcare provider.")
                
                st.divider()
                
                # Display medications in a grid
                for i, med in enumerate(result["recommended_medicines"], 1):
                    display_medication_card(med)
                    
            else:
                st.warning("No medication recommendations available")
        
        # Tab 3: Care Plan
        with tab3:
            st.subheader("Two-Week Care Plan")
            
            if "two_week_plan" in result:
                st.markdown(result["two_week_plan"])
            else:
                st.warning("Care plan not available")
        
        # Tab 4: Doctor Summary (moved to rightmost position)
        with tab4:
            st.subheader("👨‍⚕️ Doctor Summary - Clinical Overview")
            st.caption("Concise clinical information for healthcare providers")
            
            if "doctor_summary" in result:
                st.markdown(result["doctor_summary"])
            else:
                st.warning("Doctor summary not available")
        
        # Action buttons at the bottom
        st.divider()
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("🔄 Analyze New Image", use_container_width=True):
                st.session_state.analysis_complete = False
                st.session_state.analysis_result = None
                st.rerun()
        
        with col2:
            if st.button("📧 Email Report", use_container_width=True, disabled=True):
                st.info("Email functionality coming soon!")
        
        with col3:
            if st.button("🖨️ Print Report", use_container_width=True, disabled=True):
                st.info("Print functionality coming soon!")
    
    # Footer
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p><strong>Medical Image Analysis System v1.0</strong></p>
        <p>Powered by LangGraph & Google Gemini Vision | For Educational & Research Purposes Only</p>
        <p style='font-size: 0.8em; margin-top: 10px;'>
            © 2025 | Always consult healthcare professionals for medical decisions
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
