import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="🏮 Durga Puja Planner - Bangalore 2025",
    page_icon="🏮",
    layout="wide"
)

# Consistent styling with gray background and black text
st.markdown("""
<style>
    /* Main background and text colors */
    .main, .stApp {
        background-color: #D3D3D3 !important;
        color: #000000 !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-1y4p8pa, section[data-testid="stSidebar"] {
        background-color: #D3D3D3 !important;
        color: #000000 !important;
    }
    
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg p,
    .css-1y4p8pa h1, .css-1y4p8pa h2, .css-1y4p8pa h3, .css-1y4p8pa h4, .css-1y4p8pa p {
        color: #000000 !important;
    }
    
    /* All headings and text */
    h1, h2, h3, h4, h5, h6, p, span, div, label {
        color: #000000 !important;
    }
    
    .pandal-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .pandal-card h3, .pandal-card p, .pandal-card strong {
        color: #000000 !important;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        border: 1px solid #dee2e6;
        margin: 0.5rem 0;
    }
    
    .metric-card div {
        color: #000000 !important;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #dc3545 !important;
    }
    
    .tag {
        background-color: #dc3545;
        color: white !important;
        padding: 0.2rem 0.5rem;
        border-radius: 10px;
        font-size: 0.8rem;
        margin: 0.1rem;
        display: inline-block;
    }
    
    /* Input fields */
    .stSelectbox label, .stCheckbox label, .stTextInput label {
        color: #000000 !important;
    }
    
    /* Selectbox dropdown styling - white text in dropdown */
    .stSelectbox select, .stSelectbox div[data-baseweb="select"] {
        color: #ffffff !important;
        background-color: #2c3e50 !important;
    }
    
    /* Selectbox option text */
    .stSelectbox div[data-baseweb="select"] div {
        color: #ffffff !important;
    }
    
    /* Selectbox selected value */
    .stSelectbox div[data-baseweb="select"] > div {
        color: #ffffff !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #dc3545 !important;
        color: white !important;
        border: none !important;
    }
    
    /* Ensure plotly charts have proper backgrounds */
    .js-plotly-plot .plotly {
        background-color: white !important;
    }
    
    /* Info/warning/success boxes */
    .stAlert {
        color: #000000 !important;
    }
    
    .stAlert [data-testid="stMarkdownContainer"] p {
        color: #000000 !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        color: #000000 !important;
    }
    
    /* Footer styling */
    .footer-card {
        background-color: white;
        color: #000000 !important;
        text-align: center;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .footer-card h4, .footer-card p, .footer-card em {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Data
puja_dates = {
    "Shashti": "September 28, 2025",
    "Saptami": "September 29, 2025", 
    "Ashtami": "September 30, 2025",
    "Navami": "October 1, 2025",
    "Dashami": "October 2, 2025"
}

pandal_data = [
    {
        "name": "Sarathi Socio-Cultural Trust",
        "location": "Koramangala", 
        "address": "BBMP Ground, 5th Block, Koramangala",
        "highlights": ["23rd year celebration", "Bandemonium competition", "Large crowds"],
        "speciality": "Popular pandal with impressive cultural events",
        "crowd_level": "Very High",
        "best_time": "Early morning (6-8 AM) or Late evening (9-11 PM)",
        "zone": "South Bangalore",
        "rating": 4.8
    },
    {
        "name": "Bengaluru Durga Puja Committee (BDPC)",
        "location": "Palace Grounds",
        "address": "Grand Castle, Palace Grounds, near Mekhri Circle",
        "highlights": ["Manpho Pujo", "One of largest celebrations", "Grand venue"],
        "speciality": "Largest celebration in the city with grand arrangements",
        "crowd_level": "Very High",
        "best_time": "Early morning (6-9 AM) or Late evening (10 PM-12 AM)",
        "zone": "North Bangalore",
        "rating": 4.9
    },
    {
        "name": "Whitefield Cultural Association (WCA)",
        "location": "Whitefield",
        "address": "Behind Mahaveer Tranquil, Palm Meadows, Whitefield",
        "highlights": ["Famous fairground", "Complete entertainment", "Large venue"],
        "speciality": "Most famous puja with complete fairground experience",
        "crowd_level": "Very High",
        "best_time": "Afternoon (2-5 PM) or Evening (7-10 PM)",
        "zone": "East Bangalore",
        "rating": 4.7
    },
    {
        "name": "The Bengalee Association",
        "location": "Ulsoor",
        "address": "1/a, Assaye Rd, Ulsoor",
        "highlights": ["Oldest puja in Bangalore", "Traditional celebrations", "Heritage value"],
        "speciality": "Oldest and most traditional Durga Puja celebration",
        "crowd_level": "High",
        "best_time": "Morning (8-11 AM) or Evening (6-9 PM)",
        "zone": "Central Bangalore",
        "rating": 4.6
    },
    {
        "name": "Barsha Bengali Association",
        "location": "HSR Layout/Sarjapur",
        "address": "Samskruti Pavilion, Sarjapur-Marathahalli Road",
        "highlights": ["Chitrangana theme 2025", "Large puja", "HSR area favorite"],
        "speciality": "Large celebration with unique Chitrangana theme",
        "crowd_level": "High",
        "best_time": "Afternoon (2-5 PM) or Evening (6-9 PM)",
        "zone": "South East Bangalore",
        "rating": 4.5
    },
    {
        "name": "Electronic City Cultural Association (ECCA)",
        "location": "Electronic City",
        "address": "White Feather Convention Center, Hosur Road",
        "highlights": ["Award-winning presentations", "Popular in Electronic City", "Quality decorations"],
        "speciality": "Award-winning pandal known for excellent presentations",
        "crowd_level": "Medium",
        "best_time": "Evening (5-8 PM)",
        "zone": "South Bangalore",
        "rating": 4.4
    }
]

# Header
st.title("🏮 Durga Puja Planner - Bangalore 2025")
st.markdown("Plan your perfect pandal hopping experience across Namma Bengaluru!")
st.divider()

# Sidebar filters
with st.sidebar:
    st.header("🗓️ Plan Your Visit")
    
    # Date selection
    st.subheader("Select Days")
    selected_days = []
    for day, date in puja_dates.items():
        if st.checkbox(f"{day} - {date}"):
            selected_days.append(day)
    
    st.divider()
    
    # Zone filter
    zones = ["All"] + sorted(list(set([p["zone"] for p in pandal_data])))
    selected_zone = st.selectbox("Filter by Zone", zones)
    
    # Crowd filter
    crowd_levels = ["All", "Medium", "High", "Very High"]
    selected_crowd = st.selectbox("Filter by Crowd Level", crowd_levels)

# Apply filters
filtered_pandals = pandal_data.copy()
if selected_zone != "All":
    filtered_pandals = [p for p in filtered_pandals if p["zone"] == selected_zone]
if selected_crowd != "All":
    filtered_pandals = [p for p in filtered_pandals if p["crowd_level"] == selected_crowd]

# Metrics
st.subheader("📊 Overview")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">6</div>
        <div>Total Pandals</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">5</div>
        <div>Festival Days</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">4</div>
        <div>City Zones</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{len(filtered_pandals)}</div>
        <div>Filtered Results</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Pandal listings
st.subheader("🎯 Recommended Pandals")

if not filtered_pandals:
    st.warning("No pandals match your filters. Try adjusting your selection!")
else:
    for pandal in filtered_pandals:
        # Star rating
        stars = "⭐" * int(pandal['rating'])
        
        # Highlight tags
        highlight_tags = "".join([f"<span class='tag'>{h}</span>" for h in pandal['highlights']])
        
        st.markdown(f"""
        <div class="pandal-card">
            <h3>🏛️ {pandal['name']} 
                <span style="float: right; color: #dc3545;">{stars} {pandal['rating']}</span>
            </h3>
            <p><strong>📍 Location:</strong> {pandal['location']} | <strong>Zone:</strong> {pandal['zone']}</p>
            <p><strong>🏠 Address:</strong> {pandal['address']}</p>
            <p><strong>✨ Speciality:</strong> {pandal['speciality']}</p>
            <p><strong>👥 Crowd Level:</strong> <span style="background: #fff3cd; padding: 0.2rem 0.5rem; border-radius: 5px;">{pandal['crowd_level']}</span></p>
            <p><strong>⏰ Best Time:</strong> {pandal['best_time']}</p>
            <p><strong>🌟 Highlights:</strong> {highlight_tags}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# Charts section
col1, col2 = st.columns(2)

with col1:
    st.subheader("📍 Zone Distribution")
    zone_counts = {}
    for pandal in pandal_data:
        zone = pandal["zone"]
        zone_counts[zone] = zone_counts.get(zone, 0) + 1
    
    try:
        fig_zones = go.Figure(data=[go.Pie(
            labels=list(zone_counts.keys()),
            values=list(zone_counts.values()),
            hole=0.3,
            marker=dict(colors=['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57']),
            textfont=dict(color='#000000', size=12)
        )])
        
        fig_zones.update_layout(
            title="Pandals by Zone",
            height=400,
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#000000'),
            showlegend=True
        )
        st.plotly_chart(fig_zones, use_container_width=True)
    except Exception as e:
        st.error(f"Chart loading error. Showing data instead:")
        for zone, count in zone_counts.items():
            st.write(f"• {zone}: {count} pandals")

with col2:
    st.subheader("⭐ Pandal Ratings")
    sorted_pandals = sorted(pandal_data, key=lambda x: x["rating"], reverse=True)
    
    try:
        fig_ratings = go.Figure(data=[go.Bar(
            x=[p["rating"] for p in sorted_pandals],
            y=[p["name"] for p in sorted_pandals],
            orientation='h',
            marker=dict(color=[p["rating"] for p in sorted_pandals],
                       colorscale='Reds',
                       showscale=True),
            text=[f"{p['rating']}" for p in sorted_pandals],
            textposition='auto'
        )])
        
        fig_ratings.update_layout(
            title="Ratings Comparison",
            height=400,
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#000000'),
            yaxis=dict(categoryorder='total ascending'),
            xaxis=dict(range=[4, 5])
        )
        st.plotly_chart(fig_ratings, use_container_width=True)
    except Exception as e:
        st.error(f"Chart loading error. Showing data instead:")
        for pandal in sorted_pandals:
            st.write(f"• {pandal['name']}: ⭐ {pandal['rating']}")

st.divider()

# Festival timeline
st.subheader("📅 Festival Timeline")

timeline_data = [
    {"day": "Shashti", "date": "Sep 28", "description": "Festival begins! Perfect for photography"},
    {"day": "Saptami", "date": "Sep 29", "description": "Peaceful visits and authentic experience"},
    {"day": "Ashtami", "date": "Sep 30", "description": "Peak day! Cultural programs and crowds"},
    {"day": "Navami", "date": "Oct 1", "description": "Maximum celebrations and entertainment"},
    {"day": "Dashami", "date": "Oct 2", "description": "Farewell with Sindoor Khela"}
]

for item in timeline_data:
    st.info(f"**{item['day']} ({item['date']})**: {item['description']}")

st.divider()

# Route planner
st.subheader("🗺️ Plan Your Route")

if st.button("🚀 Generate My Pandal Route", type="primary", use_container_width=True):
    if selected_days:
        st.success(f"Great! You've selected {len(selected_days)} days to celebrate!")
        
        for day in selected_days:
            st.markdown(f"### {day} - {puja_dates[day]}")
            
            # Recommend different pandals based on the day
            if day in ["Shashti", "Saptami"]:
                recommended = [p for p in filtered_pandals if p["crowd_level"] in ["Medium", "High"]][:3]
                st.info("Perfect for peaceful visits and photography")
            elif day in ["Ashtami", "Navami"]:
                recommended = filtered_pandals[:3]
                st.warning("Peak days! Expect crowds but amazing cultural programs")
            else:  # Dashami
                recommended = [p for p in filtered_pandals if p["crowd_level"] != "Very High"][:2]
                st.info("Last day - focus on special pandals for Sindoor Khela")
            
            for i, pandal in enumerate(recommended, 1):
                st.write(f"{i}. **{pandal['name']}** ({pandal['location']}) - {pandal['best_time']}")
            
            st.divider()
    else:
        st.error("Please select at least one day from the sidebar!")

# Quick tips
with st.expander("💡 Pro Tips for Pandal Hopping"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🚗 Transportation**
        - Use Metro for central pandals
        - Book cabs in advance during peak days
        - Two-wheelers offer best flexibility
        
        **🍽️ Food & Culture**
        - Try authentic Bengali dishes
        - Don't miss Kosha Mangsho and Mishti Doi
        - Enjoy cultural programs in the evening
        """)
    
    with col2:
        st.markdown("""
        **📸 Photography**
        - Best lighting: Early morning or golden hour
        - Respect queue systems and traditions
        - Remove shoes where required
        
        **⏰ Timing**
        - Less crowded: Early morning (6-9 AM)
        - Cultural programs: Evening (7-10 PM)
        - Avoid lunch time on peak days
        """)

# Footer
st.divider()
st.markdown("""
<div class="footer-card">
    <h4>🙏 Subho Bijoya! 🙏</h4>
    <p>May Maa Durga bless you with happiness and prosperity!</p>
    <p><em>Made with ❤️ for Bangalore's Bengali community</em></p>
</div>
""", unsafe_allow_html=True)