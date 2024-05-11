from streamlit.testing.v1 import AppTest

def test_sidebar_init():
    at = AppTest.from_file("app.py").run()

    print(at.sidebar.success[0].value)
    assert at.sidebar.success[0].value == "Check your favorite articles."