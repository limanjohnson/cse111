from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("232 Maple, Rexburg, Idaho 87440") == "Rexburg"
    assert extract_city("232 Maple, Provo, Utah 84602") == "Provo"

def test_extract_state():
    assert extract_state("232 Maple, Rexburg, Idaho 87440") == "Idaho"
    assert extract_state("232 Maple, Provo, Utah 84602") == "Utah"

def test_extract_zipcode():
    assert extract_zipcode("232 Maple, Rexburg, Idaho 87440") == "87440"
    assert extract_zipcode("232 Maple, Provo, Utah 84602") == "84602"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])