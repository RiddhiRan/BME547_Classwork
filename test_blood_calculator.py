import pytest
# Normal


@pytest.mark.parametrize("HDL_input, expected",
                         [(65, "Normal"),
                          (45, "Borderline Low"),
                          (20, "Low")
                          ])
def test_HDL_analysis(HDL_input, expected):
    from blood_calculator import HDL_analysis
    # Arrange
    # HDL_input = 65
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == expected


@pytest.mark.parametrize("LDL_input, expected",
                         [(120, "Normal"),
                          (145, "Borderline High"),
                          (170, "High"),
                          (200, "Very High")
                          ])
def test_LDL_analysis(LDL_input, expected):
    from blood_calculator import LDL_analysis
    # Arrange
    # HDL_input = 65
    # Act
    answer = LDL_analysis(LDL_input)
    # Assert
    assert answer == expected


"""
#testing for borderline low
def test_HDL_analysis_Borderline_Low():
    from blood_calculator import HDL_analysis
    # Arrange
    HDL_input = 41
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Borderline Low"

def test_HDL_analysis_Low():
    from blood_calculator import HDL_analysis
    # Arrange
    HDL_input = 23
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Low"

#test for low """
