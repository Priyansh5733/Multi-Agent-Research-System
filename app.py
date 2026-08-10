import streamlit as st
from pipeline import run_research_pipeline


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔎",
    layout="wide"
)


# --------------------------------------------------
# Custom styling
# --------------------------------------------------

st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        .subtitle {
            color: #777;
            margin-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🔎 Multi-Agent Research System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Search → Read → Write → Critic</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:
    st.header("Research Pipeline")

    st.markdown(
        """
        **Agents involved:**

        1. 🔍 Search Agent
        2. 📖 Reader Agent
        3. ✍️ Writer
        4. 🧐 Critic
        """
    )

    st.divider()

    st.info(
        "Enter a research topic and run the pipeline. "
        "The complete research process is handled by pipeline.py."
    )


# --------------------------------------------------
# User input
# --------------------------------------------------

topic = st.text_input(
    "Research Topic",
    placeholder="e.g. Impact of Generative AI on Data Science"
)


# --------------------------------------------------
# Run pipeline
# --------------------------------------------------

if st.button("🚀 Start Research", type="primary", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    # Progress placeholders
    progress = st.progress(0)
    status = st.empty()

    try:
        status.info("🔍 Running Search Agent...")
        progress.progress(10)

        # Run your existing pipeline
        state = run_research_pipeline(topic.strip())

        progress.progress(100)
        status.success("✅ Research pipeline completed successfully.")

        st.divider()

        # --------------------------------------------------
        # Search results
        # --------------------------------------------------

        st.subheader("🔍 Search Results")

        search_results = state.get("search_results", "")

        if search_results:
            with st.expander("View Search Results", expanded=False):
                st.markdown(search_results)
        else:
            st.warning("No search results were returned.")

        # --------------------------------------------------
        # Scraped content
        # --------------------------------------------------

        st.subheader("📖 Scraped Content")

        scraped_content = state.get("scraped_content", "")

        if scraped_content:
            with st.expander("View Scraped Content", expanded=False):
                st.markdown(scraped_content)
        else:
            st.warning("No scraped content was returned.")

        # --------------------------------------------------
        # Final report
        # --------------------------------------------------

        st.subheader("📝 Final Research Report")

        report = state.get("report", "")

        if report:
            st.markdown(report)

            # Download report
            st.download_button(
                label="⬇️ Download Report",
                data=report,
                file_name=f"{topic.strip().replace(' ', '_')}_research_report.txt",
                mime="text/plain"
            )
        else:
            st.warning("No report was generated.")

        # --------------------------------------------------
        # Critic feedback
        # --------------------------------------------------

        st.subheader("🧐 Critic Review")

        feedback = state.get("feedback", "")

        if feedback:
            st.markdown(feedback)
        else:
            st.warning("No critic feedback was returned.")

    except Exception as e:
        progress.empty()
        status.error("❌ The research pipeline failed.")

        st.error(str(e))

        with st.expander("Technical Error"):
            st.exception(e)
