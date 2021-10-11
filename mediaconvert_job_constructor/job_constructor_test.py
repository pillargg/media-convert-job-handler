from mediaconvert_job_constructor import job_constructor
import pytest

ROLE_ARN = 'arn:aws:iam::123456789012:role/mediaconvert-role'
QUEUE_ARN = 'arn:aws:mediaconvert:us-east-1:123456789012:queues/mediaconvert-queue'

class Test_Job_constructor_MediaConvertJobConstructor_Create_crop:
    def test_create_crop_1(self):
        job_constructor.MediaConvertJobConstructor.create_crop(350, 70, 120, 320)

    def test_create_crop_2(self):
        job_constructor.MediaConvertJobConstructor.create_crop(90, 1, 544, 1080)

    def test_create_crop_3(self):
        job_constructor.MediaConvertJobConstructor.create_crop(550, 410, 1.5, 10)

    def test_create_crop_4(self):
        job_constructor.MediaConvertJobConstructor.create_crop(4, 90, 1080, 24)

    def test_create_crop_5(self):
        job_constructor.MediaConvertJobConstructor.create_crop(1, 30, 720, 120)

    def test_create_crop_6(self):
        job_constructor.MediaConvertJobConstructor.create_crop(0, 0, 0, 0)


class Test_Mediaconvertjobconstructor_Add_task_token:
    
    @pytest.fixture()
    def mediaconvertjobconstructor(self):
        return job_constructor.MediaConvertJobConstructor(QUEUE_ARN, ROLE_ARN)
    

    def test_add_task_token_1(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_task_token(" ")

    def test_add_task_token_2(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_task_token("")


class Test_Mediaconvertjobconstructor_Add_input:
    
    @pytest.fixture()
    def mediaconvertjobconstructor(self):
        return job_constructor.MediaConvertJobConstructor(QUEUE_ARN, ROLE_ARN)
    

    def test_add_input_1(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_input("Michael")

    def test_add_input_2(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_input("Pierre Edouard")

    def test_add_input_3(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_input("George")

    def test_add_input_4(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_input("Edmond")

    def test_add_input_5(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_input("Anas")

    def test_add_input_6(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_input("")


class Test_Mediaconvertjobconstructor_Add_overlay:
    
    @pytest.fixture()
    def mediaconvertjobconstructor(self):
        return job_constructor.MediaConvertJobConstructor(QUEUE_ARN, ROLE_ARN)
    

    def test_add_overlay_1(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_overlay("https://api.telegram.org/bot", 70, 4, 380, "hsl(10%,20%,40%)", 1, 50)

    def test_add_overlay_2(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_overlay("https://api.telegram.org/bot", 50, 100, 70, "#FF00FF", 0, 50)

    def test_add_overlay_3(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_overlay("ponicode.com", 100, 30, 320, "rgb(0.1,0.2,0.3)", 2, 1.5)

    def test_add_overlay_4(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_overlay("https://accounts.google.com/o/oauth2/revoke?token=%s", 100, 1, 90, "#F00", 2, "hsl(10%,20%,40%)")

    def test_add_overlay_5(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_overlay("https://croplands.org/app/a/confirm?t=", 50, 100, 550, "rgb(20%,10%,30%)", 0, "#F00")

    def test_add_overlay_6(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_overlay("", 0.0, 0.0, 0.0, "", 0.0, 0.0)


class Test_Mediaconvertjobconstructor_Add_output:
    
    @pytest.fixture()
    def mediaconvertjobconstructor(self):
        return job_constructor.MediaConvertJobConstructor(QUEUE_ARN, ROLE_ARN)
    

    def test_add_output_1(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_output("data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%3Ctext%20x%3D%22NaN%22%20y%3D%22NaN%22%20font-size%3D%2220%22%20alignment-baseline%3D%22middle%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%3C%2Fsvg%3E", "Pierre Edouard", 1080, 2, "^5.0.0", None)

    def test_add_output_2(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_output("data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%3Ctext%20x%3D%22NaN%22%20y%3D%22NaN%22%20font-size%3D%2220%22%20alignment-baseline%3D%22middle%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%3C%2Fsvg%3E", "Jean-Philippe", 150, 80.0, "1.0.0", True)

    def test_add_output_3(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_output("data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%3Ctext%20x%3D%22NaN%22%20y%3D%22NaN%22%20font-size%3D%2220%22%20alignment-baseline%3D%22middle%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%3C%2Fsvg%3E", "Edmond", 390, 680, "v1.2.4", True)

    def test_add_output_4(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_output("data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%3Ctext%20x%3D%22NaN%22%20y%3D%22NaN%22%20font-size%3D%2220%22%20alignment-baseline%3D%22middle%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%3C%2Fsvg%3E", "George", 0, 480, "1.0.0", False)

    def test_add_output_5(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_output("data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%3Ctext%20x%3D%22NaN%22%20y%3D%22NaN%22%20font-size%3D%2220%22%20alignment-baseline%3D%22middle%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%3C%2Fsvg%3E", "Edmond", 9, 2, "4.0.0-beta1\t", True)

    def test_add_output_6(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.add_output("", "", 0.0, 0.0, 0.0, False)


class Test_Mediaconvertjobconstructor__construct_output_group:
    
    @pytest.fixture()
    def mediaconvertjobconstructor(self):
        return job_constructor.MediaConvertJobConstructor(QUEUE_ARN, ROLE_ARN)
    

    def test__construct_output_group_1(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_output_group({ "bitrate": 12, "modifier": "name", "width": 64, "crop": True, "bitrate": "^5.0.0", "bucket": "data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%3Ctext%20x%3D%22NaN%22%20y%3D%22NaN%22%20font-size%3D%2220%22%20alignment-baseline%3D%22middle%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%3C%2Fsvg%3E", "height": 8 })

    def test__construct_output_group_2(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_output_group({ "bitrate": 8_000_000, "modifier": "name3", "width": 80.0, "crop": False, "bitrate": "^5.0.0", "bucket": "data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%3Ctext%20x%3D%22NaN%22%20y%3D%22NaN%22%20font-size%3D%2220%22%20alignment-baseline%3D%22middle%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%3C%2Fsvg%3E", "height": 64 })

    def test__construct_output_group_3(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_output_group({ "bitrate": 345364321, "modifier": "name563", "width": 48000, "crop": True, "bitrate": "v1.2.4", "bucket": "data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%3Ctext%20x%3D%22NaN%22%20y%3D%22NaN%22%20font-size%3D%2220%22%20alignment-baseline%3D%22middle%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%3C%2Fsvg%3E", "height": 99 })

    def test__construct_output_group_4(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_output_group({ "bitrate": 74567567, "modifier": "name5464", "width": 576, "crop": False, "bitrate": "4.0.0-beta1\t", "bucket": "data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%3Ctext%20x%3D%22NaN%22%20y%3D%22NaN%22%20font-size%3D%2220%22%20alignment-baseline%3D%22middle%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%3C%2Fsvg%3E", "height": 30 })

    def test__construct_output_group_5(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_output_group({ "bitrate": 6666555, "modifier": "anothername", "width": 24, "crop": True, "bitrate": "4.0.0-beta1\t", "bucket": "data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%3Ctext%20x%3D%22NaN%22%20y%3D%22NaN%22%20font-size%3D%2220%22%20alignment-baseline%3D%22middle%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%3C%2Fsvg%3E", "height": 800 })


class Test_Mediaconvertjobconstructor__construct_input_group:
    
    @pytest.fixture()
    def mediaconvertjobconstructor(self):
        return job_constructor.MediaConvertJobConstructor(QUEUE_ARN, ROLE_ARN)
    

    def test__construct_input_group_1(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_input_group({ "name": "Edmond" })

    def test__construct_input_group_2(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_input_group({ "name": "Michael" })

    def test__construct_input_group_3(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_input_group({ "name": "Pierre Edouard" })

    def test__construct_input_group_4(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_input_group({ "name": "Jean-Philippe" })

    def test__construct_input_group_5(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_input_group({ "name": "George" })

    def test__construct_input_group_6(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor._construct_input_group({ "name": "" })


class Test_Mediaconvertjobconstructor_Create:
    
    @pytest.fixture()
    def mediaconvertjobconstructor(self):
        return job_constructor.MediaConvertJobConstructor(QUEUE_ARN, ROLE_ARN)
    

    def test_create_1(self, mediaconvertjobconstructor):
        mediaconvertjobconstructor.create()

