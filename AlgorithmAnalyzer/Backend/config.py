from algorithms.algorithm_manager import algorithm_manager_factory
from algorithms.tests.mocks import TEST_ALG_DICT
from algorithms.algorithms import ALG_DICT
from algorithms.background import get_status_updater_factory, JobStatusProvider
from sample_manager.SampleManager import SampleManager

# this file provides configs for Backend Flask's app (db settings, global singletons)
# Configs can be loaded like this: app.config.from_object('config.YourConfig')
# read more here: http://flask.pocoo.org/docs/1.0/config/


class BaseConfig(object):
    """
    This is a BaseConfig that is usually not used anywhere explicitly,
    but shares common variables for all other configs.
    If expanding the app, add a config option here if it is not
    testing/production/development environment specific.

    This should by default contain the safest configuration
    """

    # Debug from Flask's documentation:
    # "If you enable debug support the server will reload itself on code changes,
    #  and it will also provide you with a helpful debugger if things go wrong."
    #  (on localhost:port)
    DEBUG = False

    # Testing from Flask's documentation:
    # 'What this does is disable error catching during request handling,
    # so that you get better error reports when performing test requests
    # against the application.'
    # also allows to setup a test client to send requests using
    # werkezeug (Flask's) tools
    TESTING = False

    # directory where samples will be stored
    # SAMPLE_UPLOAD_PATH = './data'

    # available classes of samples
    ALLOWED_SAMPLE_TYPES = ['train', 'test']

    # available filetypes and corresponding allowed extensions
    ALLOWED_FILES_TO_GET = {'audio': ['wav', 'webm'],
                            'json': ['json']}

    # MongoDB database settings
    DATABASE_URL = "127.0.0.1"
    DATABASE_PORT = "27017"
    DATABASE_NAME = "samplebase"
    JOBS_DATABASE = "jobsbase"

    # sample manager
    SAMPLE_MANAGER = SampleManager(f"{DATABASE_URL}:{DATABASE_PORT}", DATABASE_NAME)

    JOB_STATUS_PROVIDER = JobStatusProvider(f"{DATABASE_URL}:{DATABASE_PORT}", JOBS_DATABASE)

    ALGORITHM_MANAGER = algorithm_manager_factory(
        ALG_DICT,
        get_status_updater_factory(f"{DATABASE_URL}:{DATABASE_PORT}", JOBS_DATABASE),
        '__base_algorithm_manager'
    )


class ProductionConfig(BaseConfig):
    """
    This is a config for Production
    """
    pass


class DevelopmentConfig(BaseConfig):
    """
    This config is used during the development of the app on localhost
    """
    DEBUG = True


class TestingConfig(BaseConfig):
    """
    This config is used during automated tests
    """
    TESTING = True
    DATABASE_NAME = f"{BaseConfig.DATABASE_NAME}_test"
    JOBS_DATABASE = "jobsbase_test"
    SAMPLE_MANAGER = SampleManager(
        f"{BaseConfig.DATABASE_URL}:{BaseConfig.DATABASE_PORT}", DATABASE_NAME, show_logs="False"
    )

    JOB_STATUS_PROVIDER = JobStatusProvider(
        f"{BaseConfig.DATABASE_URL}:{BaseConfig.DATABASE_PORT}", JOBS_DATABASE, show_logs=False
    )

    JOB_STATUS_UPDATER_FACTORY = get_status_updater_factory(
            f"{BaseConfig.DATABASE_URL}:{BaseConfig.DATABASE_PORT}", JOBS_DATABASE, show_logs=False
        )

    ALGORITHM_MANAGER = algorithm_manager_factory(
        TEST_ALG_DICT,
        JOB_STATUS_UPDATER_FACTORY,
        '__base_algorithm_manager'
    )
