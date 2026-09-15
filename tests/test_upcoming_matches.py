import pytest


@pytest.mark.smoke
def test_main_content_is_displayed(main_content):
    """
    Verify that the application's required testing scope exists.
    """

    assert main_content.is_loaded(), (
        "The #main-content section should be visible."
    )


@pytest.mark.functional
def test_upcoming_football_matches_text_is_displayed(main_content):

    content = main_content.get_content_text()

    assert "Upcoming Football Matches" in content, (
        "Expected 'Upcoming Football Matches' text to be displayed "
        "inside #main-content."
    )

@pytest.mark.functional
def test_select_date_range(main_content):
    """
    Verify that selecting a date range displays matches.
    """

    # Open date filter
    main_content.click_date_filter()

    # Verify date filter popover is displayed
    assert main_content.is_date_filter_popover_displayed(), (
        "Expected the date-filter-popover to be displayed "
        "after clicking date-filter."
    )

    # Open calendar
    main_content.click_calendar_grid()

    # Select start and end dates
    main_content.select_day_14()
    main_content.select_day_30()

    # Apply selected date range
    main_content.apply_date()

    # Verify that the match list contains content
    assert main_content.is_match_list_not_empty(), (
        "Expected match-list to contain at least one match "
        "after applying the date range."
    )




