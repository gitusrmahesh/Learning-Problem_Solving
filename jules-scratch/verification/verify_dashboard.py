from playwright.sync_api import Page, expect
import os

def test_dashboard_loads(page: Page):
    """
    This test verifies that the dashboard page loads correctly.
    """
    # 1. Arrange: Go to the dashboard page.
    # Use os.getcwd() to get the current working directory
    path = "file://" + os.getcwd() + "/30_days_progress.html"
    page.goto(path)

    # 2. Assert: Check that the main heading is visible.
    heading = page.get_by_role("heading", name="Intermediate Problem Solving")
    expect(heading).to_be_visible()

    # Wait for 5 seconds to ensure everything is loaded
    page.wait_for_timeout(5000)

    # 3. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")
