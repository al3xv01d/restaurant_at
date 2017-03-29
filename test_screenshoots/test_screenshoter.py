
def test_make_screenshots_1920(app):
    app.screenshooter.generate_folders()
    app.screenshooter.init_size(1920)
    app.screenshooter.screen_all(app)

def test_make_screenshots_1024(app):
    app.screenshooter.init_size(1024)
    app.screenshooter.screen_all(app)

def test_make_screenshots_768(app):
    app.screenshooter.init_size(768)
    app.screenshooter.screen_all(app)


