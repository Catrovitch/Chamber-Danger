from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/generate_dungeon.py", pty=True)

def starto(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)


@task
def format(ctx):  # pylint: disable=redefined-builtin
    ctx.run("autopep8 --in-place --recursive src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverageReport(ctx):
    ctx.run("coverage html", pty=True)

@task
def BSPDungeonPerformanceTest(ctx):
    ctx.run("python3 src/performance_BSPDungeon.py", pty=True)

@task
def OrganicDungeonPerformanceTest(ctx):
    ctx.run("python3 src/performance_OrganicBSPDungeon.py", pty=True)
