"Noxfile"
import nox

REQUIREMENTS = "requirements.txt"


@nox.session
def pytest(session):
    "test"
    session.install("-r", REQUIREMENTS)
    session.run("pytest", ".")


@nox.session
def lint(session):
    "test"
    session.install("-r", REQUIREMENTS)
    session.run("pylint", "--recursive=y", "beetus.py", "beetusapp", "tests")


@nox.session
def flake8(session):
    "test"
    session.install("flake8")
    session.run("flake8", "beetus.py", "beetusapp", "tests")


@nox.session
def black(session):
    "test"
    session.install("-r", REQUIREMENTS)
    session.run("black", ".")


@nox.session
def coverage(session):
    "test"
    session.install("coverage")
    session.install("-r", REQUIREMENTS)
    session.run("coverage", "run", "--source=.", "-m", "pytest")
    session.run("coverage", "report", "-m")
