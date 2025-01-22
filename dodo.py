from shutil import move, make_archive

def task_package():
    yield {
        "name": "code",
        "actions": create_code_zip(),
        "targets": ["code.zip"]
    }

def style():
    yield {

    }

def isort():
    yield {

    }

def lint():
    yield {

    }


def task_test_code():
    yield {

    }

def task_infra_deploy():
    yield {

    }


def task_infra_destroy():
    yield {

    }

def create_code_zip():
    make_archive("code", "zip", root_dir="code")
