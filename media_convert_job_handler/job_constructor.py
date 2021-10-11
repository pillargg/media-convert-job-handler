
class MediaConvertJobConstructor:

    @staticmethod
    def create_crop(x: int, y: int, width: int, height: int):
        return {"X": x, "Y": y, "Width": width, "Height": height}

    def __init__(self, queue_arn: str, role_arn: str, status_update_interval: str = "SECONDS_10", priority: int = 1):
        self.inputs = []
        self.outputs = []
        self.queue_arn = queue_arn
        self.role_arn = role_arn
        self.overlay = None
        self.n = 0
        self.task_token = None
        self.priority = 0
        self.status_update_interval = "SECONDS_10"
        self.acceleration_settings = {
            "Mode": "DISABLED"
        }
        self.settings = {
            "TimecodeConfig": {
                "Source": "ZEROBASED"
            },
        }

    def add_task_token(self, task_token: str):
        self.task_token = task_token

    def add_input(self, input_name: str):
        self.inputs.append({"name": input_name})

    def add_overlay(
    self,
    location: str,
    x: int,
    y: int,
    w: int,
    h: int,
    layer: int = 1,
    opacity: int = 50,):
        self.overlay = {
            "InsertableImages": [{
                "Width": w,
                "Height": h,
                "ImageX": x,
                "ImageY": y,
                "Layer": layer,
                "ImageInserterInput": location,
                "Opacity": opacity
            }]
        }

    def add_output(
            self,
            bucket: str,
            output_name: str,
            width: int,
            height: int,
            bitrate: int = 12_000_000,
            crop: dict = None):
        self.outputs.append({"bucket": bucket,
                             "modifier": output_name,
                             "width": width,
                             "height": height,
                             "bitrate": bitrate,
                             "crop": crop})

    def _construct_output_group(self, output: dict):
        self.n += 1
        return {
            "Name": f"File Group {self.n}",
            "Outputs": [{
                "ContainerSettings": {
                    "Container": "MP4",
                    "Mp4Settings": {}
                },
                "VideoDescription": {
                    "CodecSettings": {
                        "Codec": "H_264",
                        "H264Settings": {
                            "MaxBitrate": output["bitrate"],
                            "RateControlMode": "QVBR",
                            "SceneChangeDetect": "TRANSITION_DETECTION"
                        },
                    },
                    "Crop": output["crop"],
                    "Width": output["width"],
                    "Height": output["height"],
                    "ScalingBehavior": "DEFAULT",
                    "TimecodeInsertion": "DEFAULT",
                    "VideoPreprocessors": {},
                    "AntiAlias": "ENABLED",
                    "Sharpness": 50,
                },
                "AudioDescriptions": [{
                    "CodecSettings": {
                        "Codec": "AAC",
                        "AacSettings": {
                            "Bitrate": 96000,
                            "CodingMode": "CODING_MODE_2_0",
                            "SampleRate": 48000
                        }
                    }
                }],
                "NameModifier": output["modifier"],
            }],
            "OutputGroupSettings": {
                "Type": "FILE_GROUP_SETTINGS",
                "FileGroupSettings": {
                    "Destination": f"s3://{output['bucket']}/"
                }
            }
        }

    def _construct_input_group(self, input_video: dict):
        return {
            "AudioSelectors": {
                "Audio Selector 1": {
                    "Offset": 0,
                    "DefaultSelection": "DEFAULT",
                    "ProgramSelection": 1
                }
            },
            "VideoSelector": {
                "ColorSpace": "FOLLOW",
                "Rotate": "DEGREE_0",
                "AlphaBehavior": "DISCARD"
            },
            "FilterEnable": "AUTO",
            "PsiControl": "USE_PSI",
            "FilterStrength": 0,
            "DeblockFilter": "DISABLED",
            "DenoiseFilter": "DISABLED",
            "InputScanType": "AUTO",
            "TimecodeSource": "ZEROBASED",
            "FileInput": input_video["name"]
        }

    def create(self):
        job = {}

        if self.task_token:
            task_token1 = self.task_token[0:256]
            task_token2 = self.task_token[256:512]
            task_token3 = self.task_token[512:768]
            job['UserMetadata'] = {
                "TaskToken1": task_token1,
                "TaskToken2": task_token2,
                "TaskToken3": task_token3
            }

        job['Role'] = self.role_arn
        job['Queue'] = self.queue_arn
        job['AccelerationSettings'] = self.acceleration_settings
        job['Priority'] = self.priority
        job['StatusUpdateInterval'] = self.status_update_interval
        job['Settings'] = self.settings
        job['Settings']['Inputs'] = []
        job['Settings']['OutputGroups'] = []


        # add inputs
        for input in self.inputs:
            job["Settings"]["Inputs"].append(
                self._construct_input_group(input))

        # add outputs
        for output in self.outputs:
            group = self._construct_output_group(output)
            if self.overlay:
                group['OutputGroups'][0]['Outputs'][0]['VideoDescription']['VideoPreprocessors'] = self.overlay
            job["Settings"]["OutputGroups"].append()

        return job
