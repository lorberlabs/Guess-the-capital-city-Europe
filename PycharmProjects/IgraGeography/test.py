from GeographyGame import check_guess

def test_check_guess():
    assert check_guess("Ljubljana", "Slovenija", {"Slovenija":"Ljubljana"})

test_check_guess()