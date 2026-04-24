import streamlit as st
import matplotlib.pyplot as plt
from scope_detector import detect_scope_creep
from impact_analyzer import analyze_impact
from recommendation import get_recommendation

# ---------- PAGE CONFIG ----------

st.set_page_config(
    page_title="Scope Creep Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ---------- CUSTOM UI ----------

st.markdown("""
<style>
.main {
    background-color: #0F172A;
}
.block-container {
    padding-top: 2rem;
}
h1 {
    text-align: center;
}
.card {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown("<h1>🚀 Scope Creep Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>AI-powered Project Impact Dashboard</p>", unsafe_allow_html=True)
st.divider()
st.write("Analyze feature expansion in software projects")

# ---------- INPUT SECTION ----------

col1, col2 = st.columns(2)

with col1:
    initial_features = st.text_input(
        "📌 Initial Features",
        placeholder="login, dashboard, reports"
    )

with col2:
    new_features = st.text_input(
        "✨ New Features",
        placeholder="chatbot, analytics"
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------- BUTTON ----------

if st.button("🔍 Analyze Scope Impact"):

    if initial_features.strip() == "" or new_features.strip() == "":
        st.error("Please enter both initial and new features.")

    else:
        initial_scope = [f.strip() for f in initial_features.split(",")]
        new_scope = [f.strip() for f in new_features.split(",")]

        creep, extra = detect_scope_creep(initial_scope, new_scope)

        if creep:

            st.warning("⚠ Scope Creep Detected")
            st.write("New Features:", extra)

            # ---------- IMPACT ----------
            time, cost, risk, risk_score = analyze_impact(extra)

            # ---------- KPI CARDS ----------
            st.markdown("### 📊 Analysis Overview")

            col1, col2, col3 = st.columns(3)

            col1.markdown(f"<div class='card'><h3>⏳ Time</h3><h2>{time} days</h2></div>", unsafe_allow_html=True)
            col2.markdown(f"<div class='card'><h3>💰 Cost</h3><h2>₹{cost}</h2></div>", unsafe_allow_html=True)
            col3.markdown(f"<div class='card'><h3>⚠ Risk</h3><h2>{risk_score}%</h2></div>", unsafe_allow_html=True)

            # ---------- PROJECT HEALTH ----------
            st.markdown("### 🚦 Project Health")

            if risk_score < 40:
                st.success("🟢 Project Stable - Low Scope Creep Risk")
            elif risk_score < 70:
                st.warning("🟡 Moderate Scope Creep - Monitor Carefully")
            else:
                st.error("🔴 High Scope Creep - Project At Risk")

            # ---------- RECOMMENDATION ----------
            recommendation = get_recommendation(extra)

            st.markdown("### 💡 Recommendation")
            st.info(recommendation)

            # ---------- GRAPH ----------
            st.markdown("### 📈 Impact Visualization")

            labels = ["Time (days)", "Cost (x1000)", "Risk (%)"]
            values = [time, cost / 1000, risk_score]

            fig, ax = plt.subplots()

            bars = ax.bar(labels, values, color=["#6366F1", "#06B6D4", "#F59E0B"])

            ax.set_facecolor("#1E293B")
            fig.patch.set_facecolor("#0F172A")
            ax.set_xlabel("Impact Metrics", color="white", fontsize=12)
            ax.set_ylabel("Values", color="white", fontsize=12)
            ax.set_title("Scope Creep Impact Analysis", color="white", fontsize=14)
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')

            for bar in bars:
                height = bar.get_height()
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    height,
                    f'{round(height, 2)}',
                    ha='center',
                    va='bottom',
                    color='white'
                )

            st.pyplot(fig)

        else:
            st.success("✅ No Scope Creep Detected")
