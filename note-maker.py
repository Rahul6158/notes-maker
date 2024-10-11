import streamlit as st

# Function to generate HTML code based on input
def generate_html(headings, contents):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Structures</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Verdana;
                background-color: #f4f4f4;
                color: #333;
            }

            .sidebar {
                width: 250px;
                background-color: #3a6cf4;
                height: 100vh;
                padding-top: 20px;
                position: fixed;
                top: 0;
                left: 0;
                box-shadow: 2px 0 5px rgba(0, 0, 0, 0.2);
                overflow-y: auto;
                transition: width 0.3s ease;
            }

            .sidebar h2 {
                color: white;
                text-align: center;
                margin-bottom: 15px;
                font-size: 24px;
            }

            .sidebar ul {
                list-style: none;
                padding-left: 0;
            }

            .sidebar ul li {
                margin: 10px 0;
            }

            .sidebar ul li a {
                color: white;
                text-decoration: none;
                padding: 10px;
                display: block;
                font-size: 16px;
                transition: background-color 0.3s ease;
                border-radius: 5px;
            }

            .sidebar ul li a:hover {
                background-color: #ffffff;
                color: #3a6cf4;
            }

            .content {
                margin-left: 260px;
                padding: 30px;
                transition: margin-left 0.3s ease;
            }

            section {
                display: none;
                margin-bottom: 50px;
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }

            section.active {
                display: block;
            }

            section h2 {
                font-size: 28px;
                margin-bottom: 10px;
                color: #3a6cf4;
                text-align: center;
            }

            section p {
                font-size: 16px;
                line-height: 1.6;
                margin-top: 10px;
            }

            .navigation-buttons {
                margin-top: 20px;
                display: flex;
                justify-content: space-between;
            }

            .nav-btn {
                padding: 10px 20px;
                background-color: #3a6cf4;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }

            .nav-btn:hover {
                background-color: #2a52b5;
            }

        </style>
    </head>
    <body>
        <div class="sidebar">
            <h2>Sidebar</h2>
            <ul>
    """

    # Adding headings to the sidebar
    for i, heading in enumerate(headings):
        html_content += f'<li><a href="#" onclick="showSection(\'section{i+1}\')">{heading}</a></li>\n'

    html_content += """
            </ul>
        </div>
        <div class="content">
    """

    # Adding sections
    for i, (heading, content) in enumerate(zip(headings, contents)):
        html_content += f"""
        <section id="section{i+1}" class="{ 'active' if i == 0 else '' }">
            <h2>{heading}</h2>
            <p>{content}</p>
            <div class="navigation-buttons">
                <span class="nav-btn" onclick="showSection('section{i}')">Previous</span>
                <span class="nav-btn" onclick="showSection('section{i+2}')">Next</span>
            </div>
        </section>
        """

    html_content += """
        </div>
        <script>
            function showSection(sectionId) {
                var sections = document.querySelectorAll('section');
                sections.forEach(function(section) {
                    section.classList.remove('active');
                });
                document.getElementById(sectionId).classList.add('active');
            }
        </script>
    </body>
    </html>
    """

    return html_content


# Streamlit UI
st.title("HTML Generator for Notes")

# User input
headings_input = st.text_area("Enter headings (one per line)")
contents_input = st.text_area("Enter corresponding content (one per line)")

if st.button("Generate HTML"):
    # Process input
    headings = headings_input.split('\n')
    contents = contents_input.split('\n')

    if len(headings) != len(contents):
        st.error("The number of headings and contents should be equal.")
    else:
        html_result = generate_html(headings, contents)
        st.code(html_result, language='html')

        # Option to download the HTML file
        st.download_button(
            "Download HTML File",
            data=html_result,
            file_name="generated_notes.html",
            mime="text/html"
        )
