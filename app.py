import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="🏮 Durga Puja Planner - Bangalore 2025",
    page_icon="🏮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS with gray background and black text
st.markdown("""
<style>
    /* Main styles with gray background and black text */
    .main, .stApp {
        background-color: #D3D3D3;
        color: #000000;
    }
    
    .main-header {
        background: linear-gradient(135deg, #C0C0C0 0%, #D3D3D3 100%);
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        border: 2px solid #A9A9A9;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .main-header h1, .main-header p {
        color: #000000 !important;
    }
    
    .pandal-card {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border-left: 5px solid #4B0082;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .pandal-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        border-left: 5px solid #6A0DAD;
    }
    
    .info-box {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #A9A9A9;
        margin: 1rem 0;
        height: 100%;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .highlight {
        color: #000000;
        font-weight: 600;
        background-color: #E6E6FA;
        padding: 0.3rem 0.6rem;
        border-radius: 6px;
        display: inline-block;
    }
    
    .section-header {
        color: #000000 !important;
        border-bottom: 2px solid #4B0082;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
        font-weight: 700;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-1y4p8pa {
        background-color: #D3D3D3;
        border-right: 2px solid #A9A9A9;
    }
    
    .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg p {
        color: #000000 !important;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #4B0082 0%, #6A0DAD 100%) !important;
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 0.7rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(75, 0, 130, 0.3);
        background: linear-gradient(135deg, #6A0DAD 0%, #8A2BE2 100%) !important;
    }
    
    /* Ensure all text is visible with good contrast */
    body, h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
        font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-weight: 700;
    }
    
    /* Custom metric boxes */
    .metric-box {
        background: linear-gradient(135deg, #FFFFFF 0%, #F5F5F5 100%);
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        margin-bottom: 1rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border: 2px solid #A9A9A9;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 800;
        color: #4B0082 !important;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #696969 !important;
        font-weight: 500;
    }
    
    /* Make sure plotly charts have appropriate colors */
    .js-plotly-plot .plotly, .js-plotly-plot .plotly text {
        color: #000000 !important;
    }
    
    /* Custom tags for highlights */
    .tag {
        display: inline-block;
        background-color: #4B0082;
        color: white !important;
        padding: 0.3rem 0.6rem;
        border-radius: 12px;
        font-size: 0.8rem;
        margin: 0.2rem;
        font-weight: 500;
    }
    
    /* Improved list styling */
    ul {
        padding-left: 1.2rem;
    }
    
    li {
        margin-bottom: 0.5rem;
        color: #000000;
    }
    
    /* Footer styling */
    .footer {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 2rem;
        border-top: 2px solid #4B0082;
    }
    
    /* Custom checkbox styling */
    .stCheckbox [data-testid="stMarkdownContainer"] p {
        color: #000000 !important;
    }
    
    /* Selectbox styling */
    .stSelectbox [data-testid="stMarkdownContainer"] {
        color: #000000 !important;
    }
    
    /* Alert boxes - Custom styling for success, warning, and info messages */
    .stAlert {
        background-color: #FFFFFF;
        border: 2px solid #A9A9A9;
        color: #000000 !important;
    }
    
    .stAlert [data-testid="stMarkdownContainer"] {
        color: #000000 !important;
    }
    
    .stAlert [data-testid="stMarkdownContainer"] p {
        color: #000000 !important;
    }
    
    .stAlert [data-testid="stMarkdownContainer"] strong {
        color: #000000 !important;
    }
    
    /* Input fields */
    .stTextInput input, .stSelectbox select, .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #A9A9A9 !important;
    }
    
    /* Plotly chart background fix */
    .js-plotly-plot .plotly .modebar {
        background: #D3D3D3 !important;
    }
    
    .js-plotly-plot .plotly .modebar-btn {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Durga Puja dates for 2025
puja_dates = {
    "Shashti": "September 28, 2025",
    "Saptami": "September 29, 2025", 
    "Ashtami": "September 30, 2025",
    "Navami": "October 1, 2025",
    "Dashami": "October 2, 2025"
}

# Pandal data
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

# Convert to DataFrame
df = pd.DataFrame(pandal_data)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🏮 Durga Puja Planner - Bangalore 2025</h1>
    <p>Plan your perfect pandal hopping experience across Namma Bengaluru!</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for filtering
st.sidebar.markdown("<h2 style='text-align: center; color: #000000;'>🗓️ Plan Your Visit</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.subheader("Select Days to Visit")
selected_days = []
for day, date in puja_dates.items():
    if st.sidebar.checkbox(f"{day} - {date}", key=day):
        selected_days.append(day)

st.sidebar.markdown("---")
st.sidebar.subheader("Filter by Zone")
zones = ["All"] + sorted(df['zone'].unique().tolist())
selected_zone = st.sidebar.selectbox("Select Zone", zones)

st.sidebar.subheader("Filter by Crowd Level")
crowd_levels = ["All", "Medium", "High", "Very High"]
selected_crowd = st.sidebar.selectbox("Select Crowd Preference", crowd_levels)

# Apply filters
filtered_df = df.copy()
if selected_zone != "All":
    filtered_df = filtered_df[filtered_df['zone'] == selected_zone]
if selected_crowd != "All":
    filtered_df = filtered_df[filtered_df['crowd_level'] == selected_crowd]

# Metrics row
st.markdown("## 📊 Overview")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-value">6</div>
        <div class="metric-label">Total Pandals</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-value">5</div>
        <div class="metric-label">Festival Days</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-value">4</div>
        <div class="metric-label">City Zones</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{len(filtered_df)}</div>
        <div class="metric-label">Filtered Pandals</div>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown("## 🎯 Recommended Pandals")
    
if filtered_df.empty:
    st.warning("No pandals match your current filters. Try adjusting your selection!")
else:
    for idx, pandal in filtered_df.iterrows():
        # Create star rating
        stars = "⭐" * int(pandal['rating'])
        if pandal['rating'] % 1 >= 0.5:
            stars += "✨"
        
        # Create highlight tags
        highlight_tags = "".join([f"<span class='tag'>{h}</span>" for h in pandal['highlights']])
        
        st.markdown(f"""
        <div class="pandal-card">
            <h3>🏛️ {pandal['name']} <span style="float: right; font-size: 1rem; color: #4B0082;">{stars} {pandal['rating']}</span></h3>
            <p><strong>📍 Location:</strong> {pandal['location']} | <strong>🏙️ Zone:</strong> {pandal['zone']}</p>
            <p><strong>🏠 Address:</strong> {pandal['address']}</p>
            <p><strong>✨ Speciality:</strong> {pandal['speciality']}</p>
            <p><strong>👥 Crowd Level:</strong> <span class="highlight">{pandal['crowd_level']}</span></p>
            <p><strong>⏰ Best Time to Visit:</strong> {pandal['best_time']}</p>
            <p><strong>🌟 Highlights:</strong> {highlight_tags}</p>
        </div>
        """, unsafe_allow_html=True)

# Visualizations and info columns
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📍 Pandal Locations")
    try:
        # Create a map visualization
        zone_coords = {
            "South Bangalore": (12.9279, 77.6271),
            "North Bangalore": (13.0350, 77.5603),
            "East Bangalore": (12.9855, 77.7363),
            "Central Bangalore": (12.9762, 77.6033),
            "South East Bangalore": (12.9121, 77.6446)
        }
        
        # Add coordinates to dataframe
        df_map = df.copy()
        df_map['lat'] = df_map['zone'].apply(lambda x: zone_coords[x][0])
        df_map['lon'] = df_map['zone'].apply(lambda x: zone_coords[x][1])
        
        # Create map
        fig_map = px.scatter_mapbox(
            df_map, 
            lat="lat", 
            lon="lon", 
            hover_name="name",
            hover_data={"zone": True, "crowd_level": True, "lat": False, "lon": False},
            color="zone",
            zoom=10,
            height=400,
            color_discrete_sequence=['#4B0082', '#6A0DAD', '#8A2BE2', '#9370DB', '#D8BFD8']
        )
        fig_map.update_layout(
            mapbox_style="light",
            plot_bgcolor='#D3D3D3',
            paper_bgcolor='#D3D3D3',
            font_color='#000000'
        )
        fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig_map, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating map: {e}")

with col2:
    st.markdown("### 📈 Crowd Distribution")
    try:
        # Create a custom pie chart with black text
        fig_crowd = go.Figure(data=[go.Pie(
            labels=df['crowd_level'].value_counts().index,
            values=df['crowd_level'].value_counts().values,
            marker=dict(colors=['#4B0082', '#6A0DAD', '#8A2BE2']),
            textfont=dict(color='#000000', size=14)
        )])
        
        fig_crowd.update_layout(
            height=300, 
            showlegend=True,
            plot_bgcolor='#D3D3D3',
            paper_bgcolor='#D3D3D3',
            font_color='#000000'
        )
        fig_crowd.update_traces(textinfo='percent+label')
        st.plotly_chart(fig_crowd, use_container_width=True)
        
        # Add a small bar chart for ratings
        st.markdown("### ⭐ Pandal Ratings")
        fig_ratings = px.bar(
            df.sort_values('rating', ascending=False),
            x='name',
            y='rating',
            color='rating',
            color_continuous_scale=['#4B0082', '#6A0DAD', '#8A2BE2']
        )
        fig_ratings.update_layout(
            height=250, 
            showlegend=False,
            plot_bgcolor='#D3D3D3',
            paper_bgcolor='#D3D3D3',
            font_color='#000000'
        )
        fig_ratings.update_xaxes(title=None, tickangle=45)
        fig_ratings.update_yaxes(title=None, range=[4, 5])
        st.plotly_chart(fig_ratings, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating charts: {e}")

# Festival information
st.markdown("## 📅 Festival Days Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-box">
        <h4 style="color: #000000;">🌅 Shashti & Saptami</h4>
        <p style="color: #000000;"><strong>September 28 - 29</strong></p>
        <p style="color: #000000;">Festival begins! Best time for photography and peaceful darshan.</p>
        <p style="color: #000000;"><strong>Recommended:</strong> Visit traditional pandals for authentic experience.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
        <h4 style="color: #000000;">🎭 Ashtami & Navami</h4>
        <p style="color: #000000;"><strong>September 30 - October 1</strong></p>
        <p style="color: #000000;">Peak celebration days! Cultural programs and maximum crowd.</p>
        <p style="color: #000000;"><strong>Recommended:</strong> Visit larger pandals for cultural events.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-box">
        <h4 style="color: #000000;">😢 Dashami</h4>
        <p style="color: #000000;"><strong>October 2</strong></p>
        <p style="color: #000000;">Farewell day with Sindoor Khela and immersion processions.</p>
        <p style="color: #000000;"><strong>Recommended:</strong> Participate in Sindoor Khela traditions.</p>
    </div>
    """, unsafe_allow_html=True)

# Planning tools
st.markdown("## 🗺️ Plan Your Route")

if st.button("🚀 Generate My Pandal Route", use_container_width=True):
    if selected_days:
        # Use custom HTML for success message to ensure black text
        st.markdown(f"""
        <div class="info-box" style="background-color: #DFF2DF; border-color: #4CAF50;">
            <h4 style="color: #000000;">✅ Great! You've selected {len(selected_days)} days to celebrate!</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Your Personalized Itinerary")
        
        for day in selected_days:
            st.markdown(f"<h4 style='color: #000000;'>{day} - {puja_dates[day]}</h4>", unsafe_allow_html=True)
            
            if day in ["Shashti", "Saptami"]:
                recommended = filtered_df[filtered_df['crowd_level'].isin(['Medium', 'High'])].head(3)
                # Custom info box with black text
                st.markdown("""
                <div class="info-box" style="background-color: #D1ECF1; border-color: #0B87C9;">
                    <p style="color: #000000;"><strong>ℹ️ Perfect for peaceful visits and photography</strong></p>
                </div>
                """, unsafe_allow_html=True)
            elif day in ["Ashtami", "Navami"]:
                recommended = filtered_df.head(4)
                # Custom warning box with black text
                st.markdown("""
                <div class="info-box" style="background-color: #FFF3CD; border-color: #FFC107;">
                    <p style="color: #000000;"><strong>⚠️ Peak days! Expect crowds but amazing cultural programs</strong></p>
                </div>
                """, unsafe_allow_html=True)
            else:  # Dashami
                recommended = filtered_df[filtered_df['crowd_level'] != 'Very High'].head(2)
                # Custom info box with black text
                st.markdown("""
                <div class="info-box" style="background-color: #D1ECF1; border-color: #0B87C9;">
                    <p style="color: #000000;"><strong>ℹ️ Last day - focus on special pandals for Sindoor Khela</strong></p>
                </div>
                """, unsafe_allow_html=True)
            
            for _, pandal in recommended.iterrows():
                st.markdown(f"""
                <p style="color: #000000;">- <strong>{pandal['name']}</strong> ({pandal['location']}) - {pandal['best_time']}</p>
                """, unsafe_allow_html=True)
            st.markdown("---")
    else:
        # Custom error box with black text
        st.markdown("""
        <div class="info-box" style="background-color: #F8D7DA; border-color: #DC3545;">
            <p style="color: #000000;"><strong>❌ Please select at least one day from the sidebar to generate your route!</strong></p>
        </div>
        """, unsafe_allow_html=True)

# Tips and recommendations
st.markdown("## 💡 Pro Tips for Pandal Hopping")

tip_cols = st.columns(2)

with tip_cols[0]:
    st.markdown("""
    <div class="info-box">
        <h4 style="color: #000000;">🚗 Transportation Tips</h4>
        <ul>
            <li style="color: #000000;">Use Metro for central pandals</li>
            <li style="color: #000000;">Book cabs in advance during peak days</li>
            <li style="color: #000000;">Two-wheelers offer best flexibility</li>
            <li style="color: #000000;">Many Koramangala pandals are within walking distance</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h4 style="color: #000000;">🍽️ Food & Shopping</h4>
        <ul>
            <li style="color: #000000;">Try authentic Bengali dishes</li>
            <li style="color: #000000;">Don't miss Kosha Mangsho and Mishti Doi</li>
            <li style="color: #000000;">Book fair stalls have great literature</li>
            <li style="color: #000000;">Traditional wear shopping available</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tip_cols[1]:
    st.markdown("""
    <div class="info-box">
        <h4 style="color: #000000;">📸 Photography & Etiquette</h4>
        <ul>
            <li style="color: #000000;">Best lighting: Early morning or golden hour</li>
            <li style="color: #000000;">Respect queue systems</li>
            <li style="color: #000000;">Remove shoes where required</li>
            <li style="color: #000000;">Avoid flash during aarti times</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h4 style="color: #000000;">⏰ Timing Strategies</h4>
        <ul>
            <li style="color: #000000;">Less Crowded: Early morning (6-9 AM)</li>
            <li style="color: #000000;">Cultural Programs: Evening (7-10 PM)</li>
            <li style="color: #000000;">Food Stalls: Peak hours (6-9 PM)</li>
            <li style="color: #000000;">Avoid: Lunch time on peak days</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Contact information
st.markdown("## 📞 Emergency Contacts")
st.markdown("""
<div class="info-box">
    <div style="display: flex; justify-content: space-between;">
        <div style="color: #000000;">
            <strong>Police:</strong> 100<br>
            <strong>Ambulance:</strong> 108<br>
        </div>
        <div style="color: #000000;">
            <strong>Fire:</strong> 101<br>
            <strong>Bangalore Traffic Police:</strong> 080-22943488
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p style="color: #000000;">🙏 Subho Bijoya! May Maa Durga bless you with happiness and prosperity! 🙏</p>
    <p style="color: #000000;"><em>Made with ❤️ for Bangalore's Bengali community</em></p>
</div>
""", unsafe_allow_html=True)
