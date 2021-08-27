# project/server/config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    APP_NAME = os.getenv("APP_NAME", "app")
    SERVER_NAME = os.getenv("SERVER_NAME", None)

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///{0}".format(os.path.join(basedir, "dev.db"))
    )

class TestingConfig(BaseConfig):
    """Testing configuration."""

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///{0}".format(os.path.join(basedir, "testing.db"))
    )
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration."""
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///{0}".format(os.path.join(basedir, "prod.db")),
    )
    APP_SECRET = "54e783cd42b34f4bbea9155d6a66fdc4"
    SECRET_KEY = "8074aff47a024be190750eb5d17349fd"
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "a284ab2ef65b477ca0e3e8d65baba52c"