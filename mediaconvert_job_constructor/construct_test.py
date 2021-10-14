import random
import string
import json

import pytest

from .job_constructor import MediaConvertJobConstructor

# generate a random string of n length
def random_string(n):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n))


def test_construction():
    ROLE_ARN = 'arn:aws:iam::123456789012:role/mediaconvert-role'
    QUEUE_ARN = 'arn:aws:mediaconvert:us-east-1:123456789012:queues/mediaconvert-queue'
    constructor = MediaConvertJobConstructor(QUEUE_ARN, ROLE_ARN)

    constructor.add_task_token(random_string(768))
    overlay_location = "https://pillaroverlays.s3.amazonaws.com/watermark.png"
    constructor.add_overlay(overlay_location, 0, 900, 350, 100)

    constructor.add_input("s3://chandlertestbucket/input.mp4")
    constructor.add_input("s3://chandlertestbucket/input.mp4")
    constructor.add_input("s3://chandlertestbucket/input.mp4")

    constructor.add_output("s3://chandlertestbucket", 'output', 1920, 1080)

    job = constructor.create()

    assert job['Queue'] == QUEUE_ARN
    assert job['Role'] == ROLE_ARN

    assert len(job['UserMetadata']['TaskToken1']) == 256
    assert len(job['UserMetadata']['TaskToken2']) == 256
    assert len(job['UserMetadata']['TaskToken3']) == 256

    assert len(job['Settings']['Inputs']) == 3
    assert len(job['Settings']['OutputGroups']) == 1

    # output job to a json file
    with open('job2.json', 'w') as f:
        json.dump(job, f, indent=4)



    