import pytest
from project import count_occurrences,letter_replacement,top_words_from
from unittest.mock import patch


def test_count_occurrences():
    test_list = ["Cybersecurity","APT","Worm","RAT","Cybersecurity"]
    min_length = 4
    expected_results = {"Cybersecurity":2, "Worm":1}
    assert count_occurrences(test_list,min_length) == expected_results

def test_letter_replacement():
    test_list = ["Cybersecurity","APT","Worm","RAT","Cybersecurity"]
    expected_results = ['Cyb3r$3cur!7y', 'APT', 'Worm', 'RAT', 'Cyb3r$3cur!7y']
    assert letter_replacement(test_list) == expected_results

@patch("project.count_occurrences")
def test_top_words_from(mock_count_occurrences):
    mock_count_occurrences.return_value = {"Cybersecurity":2, "Worm":1}
    url = "http://example.com"
    min_length = 3
    expected_output = [("Cybersecurity",2), ("Worm",1)]
    assert top_words_from(url, min_length) == expected_output




