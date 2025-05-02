import streamlit as st
import _pages.vessel_input as vessel_input
import _pages.speed_optimization as speed_optimization
import _pages.route_optimization as route_optimization
import _pages.cost_benefit as cost_benefit
import _pages.emissions as emissions
import _pages.dashboard as dashboard


# Configure the Streamlit app
def configure_app():
    st.set_page_config(
        page_title="Maritime Slow Steaming Optimization",
        page_icon="🚢",
        layout="wide",
        initial_sidebar_state="expanded",
    )


# Initialize session state variables
def initialize_session_state():
    session_defaults = {
        "vessel_data": None,
        "route_data": None,
        "weather_data": None,
        "optimization_results": None,
        "emissions_data": None,
    }
    for key, default_value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value


# Define the pages
def get_pages():
    return {
        "Vessel Input": vessel_input,
        "Route Optimization": route_optimization,
        "Speed Optimization": speed_optimization,
        "Cost-Benefit Analysis": cost_benefit,
        "Emissions Calculator": emissions,
        "Performance Dashboard": dashboard,
    }


# Render the sidebar
def render_sidebar(pages):
    st.sidebar.title("Maritime Slow Steaming Optimization")
    st.sidebar.image(
        "https://cdn.jsdelivr.net/npm/feather-icons/dist/icons/anchor.svg", width=50
    )

    selection = st.sidebar.radio("Navigate to", list(pages.keys()))

    with st.sidebar.expander("About the Application"):
        st.write(
            """
        This application helps maritime operators optimize vessel operations through slow steaming practices.
        It processes vessel data to generate recommendations that balance economic and environmental objectives.
        """
        )

    with st.sidebar.expander("How to Use"):
        st.write(
            """
        1. Start by entering vessel specifications in the Vessel Input page
        2. Navigate through the pages to explore different optimization scenarios
        3. Review recommendations on the Performance Dashboard
        """
        )

    st.sidebar.markdown("---")
    st.sidebar.caption("© 2023 Maritime Optimization Solutions")

    return selection


# Main function
def main():
    configure_app()
    # initialize_session_state()
    pages = get_pages()
    selection = render_sidebar(pages)

    # Display the selected page
    selected_page = pages[selection]
    selected_page()


if __name__ == "__main__":
    main()
