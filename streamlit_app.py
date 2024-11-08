import streamlit as st
import base64
from pathlib import Path
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Set page config
st.set_page_config(page_title="Interest Calculator", layout="wide")
ocbc_logo = get_image_base64("ocbc_logo.png")

st.markdown("""
    <style>
    /* Hide default Streamlit header */
    [data-testid="stHeader"] {
        display: none;
    }

    /* Main container padding to account for fixed navbar */
    .main {
        padding-top: 60px;
    }

    /* Navigation styles */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: white;
        border-bottom: 1px solid #eee;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
    }

    .nav-left {
        display: flex;
        align-items: center;
        gap: 2rem;
    }

    .nav-center {
        display: flex;
        gap: 2rem;
    }

    .nav-right {
        display: flex;
        gap: 2rem;
        align-items: center;
    }

    .nav-item {
        color: #666;
        text-decoration: none;
        font-size: 0.9rem;
        cursor: pointer;
    }

    .nav-item:hover {
        color: #EE2E24;
    }

    .login-btn {
        color: #EE2E24;
        font-weight: 500;
    }

    /* Breadcrumb styles */
    .breadcrumb {
        display: flex;
        gap: 0.5rem;
        padding: 1rem 2rem;
        background-color: #f5f5f5;
        margin-top: 0rem;
        font-size: 0.9rem;
    }

    .breadcrumb-item {
        color: #6c757d;
    }

    .breadcrumb-item.active {
        color: #0066b3;
    }

    /* Calculator form styles */
    .calculator-container {
        padding: 2rem;
    }

    .stButton > button {
        background-color: #EE2E24;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        width: 100%;
        margin-bottom: 0.5rem;
    }
    
    .stButton > button:hover {
        background-color: #D41E24;
    }
    
    .result-box {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .small-text {
        font-size: 0.8rem;
        color: #6c757d;
    }
    
    .dollar-amount {
        font-size: 2.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #333;
    }

    /* Help button styles */
    .help-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #6c757d;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 20px;
        cursor: pointer;
    }

    .help-button:hover {
        background-color: #5a6268;
    }

    /* Input field styles */
    .stSelectbox [data-testid="stMarkdown"] {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 0.5rem;
    }

    .stNumberInput [data-testid="stMarkdown"] {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown(f"""
    <div class="navbar">
        <div class="nav-left">
            <img src="data:ocbc_logo.png;base64,{ocbc_logo}" alt="OCBC Logo" style="height: 30px;"/>
        </div>
        <div class="nav-center">
            <div class="nav-item">Premier Banking</div>
            <div class="nav-item">Digital Banking</div>
            <div class="nav-item">Security</div>
            <div class="nav-item">Branches & ATMs</div>
            <div class="nav-item">Get help</div>
        </div>
        <div class="nav-right">
            <div class="nav-item login-btn">Login</div>
        </div>
    </div>

    <div class="breadcrumb">
        <span class="breadcrumb-item">Personal Banking</span>
        <span>›</span>
        <span class="breadcrumb-item">Accounts</span>
        <span>›</span>
        <span class="breadcrumb-item">360 Account</span>
        <span>›</span>
        <span class="breadcrumb-item active">Rate Calculator</span>
    </div>
""", unsafe_allow_html=True)

# Main title
st.title("Interest Calculator")
st.markdown("""
    Please fill in the inputs below to find out the rates you are entitled to in the OCBC 360 Account!<br>
    """, unsafe_allow_html=True)
st.caption("*Indicates a required field.")

# Create columns for the main layout
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.markdown("My account balance in S$: *")
    # balance = st.number_input("", min_value=0, value=100000,step=5000, label_visibility="collapsed")
    balance = st.select_slider("", options=list(range(1000, 200001, 500)))
    
    # Salary dropdown
    st.markdown("SALARY: I credit a salary of at least S$1800 each month via the following options: *")
    salary_option = st.selectbox(
        "",
        ["GIRO", "FAST", "PayNow via GIRO","PayNow via FAST", "None of the above"],
        label_visibility="collapsed"
    )

    # Save amount dropdown
    st.markdown("SAVE: Do you at least have 500$ more in your account this month compared to last month on average? *")
    save_amount = st.toggle("")
    
    st.markdown("SPEND: I spend the following amount on my OCBC 365, OCBC INFINITY, OCBC NXT, OCBC 90°N or OCBC Rewards Card in a month (in S$): *")
    spend_amount = st.select_slider("Spending Amount:", options= list(range(0, 10000, 50)))

    st.markdown("INSURE+INVEST: I have/plan to purchase(d) the following products with a min. investment of S$20,000: ")
    insure_invest_options = st.multiselect(
        "Select your investment options:",
        ["Autowise", "Great EV Protect", "Great CareShield", "GreatLife Endowment Insurance 3", "CPFIA", "OCBC RoboInvest"]
    )


insure_products = ["Great CareShield", "GreatLife Endowment Insurance 3", "CPFIA"]
invest_products = ["Autowise","Great EV Protect","OCBC RoboInvest"]

# SALARY, SAVE, SPEND, INSURE, INVEST, GROW
def calculate_interest_rate(balance, SALARY, SAVE, SPEND, INSURE, INVEST):
    # Initialize interest rates
    first_75k_rate = 0
    next_25k_rate = 0
    base_rate = 0.05
    eir_rate = 0
    
    # Check conditions for "Salary"
    if SALARY != "None of the above":
        first_75k_rate += 2.00
        next_25k_rate += 4.00

    # Check conditions for "Save"
    if SAVE:
        first_75k_rate += 1.20
        next_25k_rate += 2.40

    # Check conditions for "Spend"
    if SPEND >= 500:
        first_75k_rate += 0.60
        next_25k_rate += 0.60

    # Check conditions for "Insure"
    if INSURE:
        first_75k_rate += 1.20
        next_25k_rate += 2.40

    # Check conditions for "Invest"
    if INVEST:
        first_75k_rate += 1.20
        next_25k_rate += 2.40

    # Check conditions for "Grow"
    if balance >= 200000:
        first_75k_rate += 2.40
        next_25k_rate += 2.40

    # Calculate EIR (Effective Interest Rate)
    eir_rate = (3/4 * first_75k_rate + 1/4 * next_25k_rate) + base_rate
    return first_75k_rate, next_25k_rate, eir_rate

def bool_insure_invest(insure_invest_ls, insure_pdts_ls, invest_pdts_ls):
    INSURE = False
    INVEST = False
    for pdt in insure_invest_ls:
        if pdt in insure_pdts_ls:
            INSURE = True
        elif pdt in invest_pdts_ls:
            INVEST = True
    return INSURE, INVEST

INSURE, INVEST = bool_insure_invest(insure_invest_options, insure_products, invest_products)
first_75k_rate, next_25k_rate, eir_rate = calculate_interest_rate(balance, salary_option, save_amount, spend_amount, INSURE, INVEST)


if balance <= 100000:
    int_amount = balance*(eir_rate/100/12)
else:
    int_amount = 100000*eir_rate/100/12 + ((balance-100000) * 0.05/100/12)

with col3:
    # Result box with styled dollar amount
    # st.markdown(f"""
    #     <div class='result-box'>
    #         <div class='dollar-amount'>$ {int_amount}</div>
    #         <p>Dollars earned with 360/month</p>
    #         <p>{int_perc}% interest earned with 360/month</p>
    #     </div>
    # """, unsafe_allow_html=True)
    st.metric(label="Total Interest Earned per Month", value=f"S$ {int_amount:.2f}")
    st.metric(label="Annual Interest Earned in %", value=f"{eir_rate:.2f}%")
    # st.write(f"{first_75k_rate=}")
    # st.write(f"{next_25k_rate=}")
    # Action buttons
    st.button("Apply Now!", type="primary")
    st.button("Tell me more!", type="primary")

# Help button at bottom right
st.markdown("""
    <div class='help-button'>
        Need help?
    </div>
""", unsafe_allow_html=True)



