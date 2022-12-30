import pytest
from config.driver.driverfactory import Driver
from globals import GlobalVars as glob


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="session", autouse=True)
def before_all(request):
    request.session.url = request.config.getini('url')
    glob.mode = request.config.getini('mode')
    if request.config.getini('browser') in ["chrome", "firefox", "edge", "safari"]:
        glob.browser = request.config.getini('browser')
    else:
        glob.browser = "chrome"


@pytest.fixture(scope="function", autouse=True)
def pretest(request):
    driver_instance = Driver()
    glob.driver = driver_instance.get_driver()
    glob.driver.delete_all_cookies()

    yield

    if request.node.rep_call.failed:
        pass


@pytest.fixture(scope="session", autouse=True)
def posttest(request):
    yield glob.driver
    glob.driver.quit()


def pytest_addoption(parser):
    parser.addini('url', 'url of page')
    parser.addini('mode', 'running mode')
    parser.addini('browser', 'browser type')
