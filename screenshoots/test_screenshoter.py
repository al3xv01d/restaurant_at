from screenshoots.make_screen import *

def test_make_screenshots_1920(app):
    init_size(1024)
    make_folder_for_todays_date()
    #screen_all(app)

    checkout_page_1_ms(app)

# def test_make_screenshots_1024(app):
#     init_size(1024)
#     screen_all(app)
#
# def test_make_screenshots_768(app):
#     init_size(768)
#     screen_all(app)
#
