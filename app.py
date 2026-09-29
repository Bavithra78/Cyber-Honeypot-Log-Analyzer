import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Honeypot Threat Dashboard", page_icon="🛡️", layout="wide")

st.title("🛡️ Honeypot Threat Monitoring Dashboard")
st.caption("A simple dashboard for analysing synthetic honeypot security logs.")

df = pd.read_csv("dataset/honeypot_logs.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

st.sidebar.header("Filters")
severity = st.sidebar.multiselect(
    "Severity",
    options=sorted(df["Severity"].unique()),
    default=sorted(df["Severity"].unique())
)
protocol = st.sidebar.multiselect(
    "Protocol",
    options=sorted(df["Protocol"].unique()),
    default=sorted(df["Protocol"].unique())
)

filtered = df[df["Severity"].isin(severity) & df["Protocol"].isin(protocol)]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Events", len(filtered))
c2.metric("Critical Events", int((filtered["Severity"] == "Critical").sum()))
c3.metric("Unique Source IPs", filtered["Source_IP"].nunique())
c4.metric("Blocked / Redirected", int(filtered["Action"].isin(["Blocked","Redirected"]).sum()))

st.divider()

left, right = st.columns(2)

with left:
    severity_counts = filtered["Severity"].value_counts().reset_index()
    severity_counts.columns = ["Severity", "Count"]
    fig = px.bar(severity_counts, x="Severity", y="Count", title="Threats by Severity")
    st.plotly_chart(fig, use_container_width=True)

with right:
    threat_counts = filtered["Threat_Type"].value_counts().reset_index()
    threat_counts.columns = ["Threat Type", "Count"]
    fig = px.pie(threat_counts, names="Threat Type", values="Count",
                 title="Threat Type Distribution")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("📋 Detected Events")
st.dataframe(filtered.sort_values("Timestamp", ascending=False),
             use_container_width=True, hide_index=True)

st.subheader("🔎 Key Observations")
if len(filtered):
    top_threat = filtered["Threat_Type"].value_counts().idxmax()
    top_protocol = filtered["Protocol"].value_counts().idxmax()
    st.write(f"- Most frequent threat type: **{top_threat}**")
    st.write(f"- Most observed protocol: **{top_protocol}**")
    st.write(f"- Critical events detected: **{int((filtered['Severity'] == 'Critical').sum())}**")
else:
    st.info("No events match the selected filters.")
